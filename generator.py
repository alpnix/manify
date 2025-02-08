#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import logging
from dotenv import dotenv_values
from cartesia import Cartesia
from pydub import AudioSegment

# -----------------------------------------------------------------------------
# Setup logging
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# -----------------------------------------------------------------------------
# Load and validate configuration from .env
# -----------------------------------------------------------------------------
dotenv_path = ".env"
if not os.path.exists(dotenv_path):
    logging.error("Configuration file '.env' not found.")
    sys.exit(1)

config = dotenv_values(dotenv_path)
cartesia_api_key = config.get("CARTESIA_API_KEY")
if not cartesia_api_key:
    logging.error("CARTESIA_API_KEY not found in .env")
    sys.exit(1)

# -----------------------------------------------------------------------------
# Function to return the Manim code for the sum-of-natural-numbers proof.
#
# In this version:
#   • A random background music track (from songs/*.mp3) is added along with the TTS voiceover.
# -----------------------------------------------------------------------------
def get_manim_code_from_prompt(prompt: str) -> str:
    return r'''
from manim import *
import glob
import random

class GeneratedScene(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # Optionally add random background music from songs/*.mp3
        # ------------------------------------------------------------
        music_files = glob.glob("songs/*.mp3")
        if music_files:
            chosen_music = random.choice(music_files)
            self.add_sound(chosen_music, time_offset=0)
        
        # ------------------------------------------------------------
        # Parameters
        # ------------------------------------------------------------
        n = 6  # Number of rows (change this value for a different triangle size)
        square_size = 0.5
        gap = 0.05

        # ------------------------------------------------------------
        # Create the triangular arrangement of squares
        # Each row i (1 to n) contains i squares.
        # ------------------------------------------------------------
        triangle = VGroup()
        for row in range(1, n + 1):
            # Create a row of 'row' squares
            row_squares = VGroup(*[
                Square(
                    side_length=square_size,
                    fill_color=BLUE,
                    fill_opacity=1,
                    stroke_color=WHITE
                )
                for _ in range(row)
            ])
            row_squares.arrange(RIGHT, buff=gap)
            # Shift each row downward so that they stack like a triangle
            row_squares.shift(DOWN * (row - 1) * (square_size + gap))
            triangle.add(row_squares)
        
        triangle.to_edge(LEFT, buff=1)

        # ------------------------------------------------------------
        # Create a duplicate of the triangle and flip it horizontally.
        # Placing it next to the original triangle forms a rectangle.
        # ------------------------------------------------------------
        triangle_copy = triangle.copy()
        triangle_copy.flip(axis=RIGHT)
        triangle_copy.next_to(triangle, RIGHT, buff=gap)

        # ------------------------------------------------------------
        # Animate the creation of the triangles
        # ------------------------------------------------------------
        self.play(Create(triangle))
        self.wait(0.5)
        self.play(Create(triangle_copy))
        self.wait(0.5)
        
        # Group the two triangles and draw a surrounding rectangle
        rectangle = VGroup(triangle, triangle_copy)
        rect_outline = SurroundingRectangle(rectangle, color=YELLOW, buff=0.1)
        self.play(Create(rect_outline))
        self.wait(1)
        
        # ------------------------------------------------------------
        # Display an explanatory text message
        # ------------------------------------------------------------
        explanation = Text("Two identical triangles form a rectangle", font_size=24)
        explanation.to_edge(UP)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # ------------------------------------------------------------
        # Write the formula for the sum of the first n natural numbers:
        # S = n(n+1)/2
        # ------------------------------------------------------------
        formula = MathTex(r"S = \frac{n(n+1)}{2}")
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(2)
'''

# -----------------------------------------------------------------------------
# Function to generate and process TTS audio using Cartesia and pydub.
# -----------------------------------------------------------------------------
def speak(text: str, filename="voiceover_intro.wav", trim_ms=200) -> str:
    try:
        tts_client = Cartesia(api_key=cartesia_api_key)
    except Exception as e:
        logging.error("Error initializing Cartesia client: %s", e)
        raise

    try:
        data = tts_client.tts.bytes(
            model_id="sonic-preview",
            transcript=text,
            voice_id="3790cf58-070e-48ec-8dbe-6a037065b413",  # Example voice ID
            output_format={
                "container": "wav",
                "encoding": "pcm_s16le",
                "sample_rate": 44100,
            },
        )
    except Exception as e:
        logging.error("Error during TTS generation: %s", e)
        raise

    try:
        with open(filename, "wb") as f:
            f.write(data)
    except Exception as e:
        logging.error("Error writing TTS audio file: %s", e)
        raise

    try:
        audio = AudioSegment.from_file(filename, format="wav")
        normalized_audio = audio.normalize()
        compressed_audio = normalized_audio.compress_dynamic_range()
        final_audio = compressed_audio.set_frame_rate(44100).set_channels(2).set_sample_width(2)
        if len(final_audio) > trim_ms:
            final_audio = final_audio[:-trim_ms]
        final_audio.export(filename, format="wav", parameters=["-ar", "44100", "-ab", "192k"])
    except Exception as e:
        logging.error("Error processing TTS audio: %s", e)
        raise

    return filename

# -----------------------------------------------------------------------------
# Function to render a Manim scene and return the path to the output video.
# -----------------------------------------------------------------------------
def render_manim_scene(source_file: str, scene_name: str, media_dir: str = "media_output") -> str:
    render_cmd = [
        "manim",
        source_file,
        scene_name,
        "-qk",  # 4K quality rendering
        "--media_dir", media_dir
    ]
    try:
        subprocess.run(render_cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error("Manim rendering failed: %s", e)
        raise

    base_name = os.path.splitext(os.path.basename(source_file))[0]
    # Check common output folders (e.g., "1080p60" or "2160p60")
    for quality in ["1080p60", "2160p60"]:
        rendered_folder = os.path.join(media_dir, "videos", base_name, quality)
        rendered_video = os.path.join(rendered_folder, f"{scene_name}.mp4")
        if os.path.exists(rendered_video):
            return rendered_video

    raise FileNotFoundError(f"Rendered video not found in any known quality folders for scene {scene_name}")

# -----------------------------------------------------------------------------
# Main function orchestrating the workflow.
# -----------------------------------------------------------------------------
def main():
    # 1. Retrieve the user prompt (or use a default)
    prompt = sys.argv[1] if len(sys.argv) > 1 else "sum of natural numbers"
    logging.info("User prompt: %s", prompt)

    # 2. Select the Manim code (the geometric proof)
    try:
        logging.info("Selecting Manim code for sum of the first n natural numbers proof...")
        manim_code = get_manim_code_from_prompt(prompt)
    except Exception as e:
        logging.error("Failed to select Manim code: %s", e)
        sys.exit(1)

    # 3. Write the selected code to a temporary file
    temp_filename = "generated_manim_scene.py"
    try:
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(manim_code)
        logging.info("Manim code written to: %s", temp_filename)
    except Exception as e:
        logging.error("Failed to write Manim code to file: %s", e)
        sys.exit(1)

    # 4. Generate a brief TTS voiceover describing the proof
    voiceover_text = (
        "In this video, we will prove that the sum of the first n natural numbers "
        "is n times n plus one, all divided by two. We illustrate this with a triangular "
        "arrangement of blue squares. Then, a copy of the pyramid is rotated by 180 degrees "
        "and shifted to fill the gap, forming a complete rectangle. Finally, we derive that "
        "S equals n times n plus one over two."
    )
    try:
        speak(voiceover_text)
        logging.info("Voiceover generated: voiceover_intro.wav")
    except Exception as e:
        logging.error("Failed to generate voiceover: %s", e)
        sys.exit(1)

    # 5. Render the 'GeneratedScene' using Manim
    scene_name = "GeneratedScene"
    try:
        logging.info("Rendering Manim scene '%s'...", scene_name)
        rendered_video_path = render_manim_scene(temp_filename, scene_name)
    except Exception as e:
        logging.error("Failed to render Manim scene: %s", e)
        sys.exit(1)

    # 6. Move the rendered video to the current directory as 'video.mp4'
    final_video = os.path.join(os.getcwd(), "video.mp4")
    try:
        shutil.move(rendered_video_path, final_video)
        logging.info("Final video saved as: %s", final_video)
    except Exception as e:
        logging.error("Failed to move rendered video: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
