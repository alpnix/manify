#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import logging
import random
import glob
from dotenv import dotenv_values
from cartesia import Cartesia
from pydub import AudioSegment, effects

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
# Function to return the improved Manim code.
# -----------------------------------------------------------------------------
def get_manim_code_from_prompt(prompt: str) -> str:
    """
    For demonstration, we are returning a scene named PowerRuleScene
    which demonstrates the power rule and its derivation.
    Components are spaced out to ensure they do not overlap.
    """
    return r'''
from manim import *

class PowerRuleScene(Scene):
    def construct(self):
        # --------------------------------------------------
        # Intro: Title & Statement of the Power Rule
        # --------------------------------------------------
        title = Text("The Power Rule", font_size=72, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        rule = MathTex(r"\frac{d}{dx}x^n = nx^{n-1}", font_size=64, color=BLUE)
        rule.next_to(title, DOWN, buff=0.5)
        self.play(Write(rule))
        self.wait(3)

        # --------------------------------------------------
        # Rigorous Derivation Using the Limit Definition
        # --------------------------------------------------
        step1 = MathTex(r"f(x)=x^n").to_edge(LEFT)
        step2 = MathTex(r"f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}")
        step2.next_to(step1, DOWN, aligned_edge=LEFT, buff=0.5)
        step3 = MathTex(r"=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}")
        step3.next_to(step2, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(step1))
        self.wait(2)
        self.play(Write(step2))
        self.wait(2)
        self.play(Write(step3))
        self.wait(3)

        expansion = MathTex(
            r"(x+h)^n = x^n + nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \cdots + h^n"
        )
        expansion.scale(0.8)
        expansion.next_to(step3, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(expansion))
        self.wait(4)

        subtraction = MathTex(
            r"(x+h)^n - x^n = nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \cdots + h^n"
        )
        subtraction.scale(0.8)
        subtraction.next_to(expansion, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(subtraction))
        self.wait(4)

        factor = MathTex(
            r"\frac{(x+h)^n - x^n}{h} = nx^{n-1} + \binom{n}{2}x^{n-2}h + \cdots + h^{n-1}"
        )
        factor.scale(0.8)
        factor.next_to(subtraction, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(factor))
        self.wait(4)

        limit_expr = MathTex(
            r"f'(x)=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}=nx^{n-1}"
        )
        limit_expr.scale(0.9)
        limit_expr.next_to(factor, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(limit_expr))
        self.wait(4)

        deriv_summary = Text("Thus, by the limit definition, we derive the Power Rule.", font_size=36, color=WHITE)
        deriv_summary.next_to(limit_expr, DOWN, buff=0.5)
        self.play(FadeIn(deriv_summary))
        self.wait(3)

        self.play(FadeOut(VGroup(title, rule, step1, step2, step3, expansion, subtraction, factor, limit_expr, deriv_summary)))
        self.wait(1)

        # --------------------------------------------------
        # Graphical Example: f(x) = x^3 and Its Tangent
        # --------------------------------------------------
        example_text = Text("Example: f(x)=x^3", font_size=48, color=ORANGE).to_edge(UP)
        self.play(Write(example_text))
        self.wait(2)

        # Create coordinate axes.
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-30, 30, 5],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True}
        ).to_edge(DOWN)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))
        self.wait(2)

        # Plot the function f(x)=x^3.
        graph = axes.plot(lambda x: x**3, color=RED, x_range=[-2.5, 2.5])
        graph_label = axes.get_graph_label(graph, label=MathTex("x^3"))
        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        # Introduce a dot on the graph.
        dot = Dot(color=YELLOW)
        x_tracker = ValueTracker(1)
        dot.add_updater(lambda m: m.move_to(axes.c2p(x_tracker.get_value(), (x_tracker.get_value())**3)))
        self.add(dot)

        # Draw the tangent line at the dot.
        # For f(x)=x^3, the derivative is f'(x)=3x^2.
        tangent_line = always_redraw(
            lambda: Line(
                axes.c2p(x_tracker.get_value() - 2, (x_tracker.get_value() - 2)**3),
                axes.c2p(x_tracker.get_value() + 2, (x_tracker.get_value() + 2)**3),
                color=GREEN
            )
        )
        self.add(tangent_line)
        self.wait(2)

        # Animate the dot moving along the curve to show the changing tangent.
        self.play(x_tracker.animate.set_value(-1.5), run_time=6)
        self.wait(3)
        self.play(x_tracker.animate.set_value(2), run_time=6)
        self.wait(3)

        slope_text = MathTex(r"f'(x)=3x^2", font_size=48, color=GREEN).to_edge(UP)
        self.play(Write(slope_text))
        self.wait(5)

        # --------------------------------------------------
        # Final Summary and Wrap-Up
        # --------------------------------------------------
        final_summary = Text("In general, the derivative of x raised to a power is that power times x raised to one less than that power.", font_size=48, color=PURPLE).to_edge(DOWN)
        self.play(Write(final_summary))
        self.wait(6)

        self.play(FadeOut(VGroup(example_text, axes, labels, graph, graph_label, dot, tangent_line, slope_text, final_summary)))
        self.wait(2)
'''

# -----------------------------------------------------------------------------
# Generate and process TTS audio using Cartesia and pydub.
# -----------------------------------------------------------------------------
def speak(text: str, filename="voiceover_intro.wav", trim_ms=200) -> str:
    """
    Generates a voiceover WAV file using Cartesia TTS and applies
    normalization & compression with pydub.
    """
    try:
        tts_client = Cartesia(api_key=cartesia_api_key)
    except Exception as e:
        logging.error("Error initializing Cartesia client: %s", e)
        raise

    logging.info("Generating TTS audio from Cartesia...")
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

    # Write raw TTS to disk
    try:
        with open(filename, "wb") as f:
            f.write(data)
    except Exception as e:
        logging.error("Error writing TTS audio file: %s", e)
        raise

    # Normalize, compress, and optionally trim the audio
    logging.info("Normalizing and compressing TTS audio...")
    try:
        audio = AudioSegment.from_file(filename, format="wav")
        normalized_audio = effects.normalize(audio)
        compressed_audio = effects.compress_dynamic_range(normalized_audio)
        final_audio = compressed_audio.set_frame_rate(44100).set_channels(2).set_sample_width(2)

        # Optionally trim a small portion from the end (to remove TTS trailing silence)
        if len(final_audio) > trim_ms:
            final_audio = final_audio[:-trim_ms]

        # Export the processed audio
        final_audio.export(filename, format="wav", parameters=["-ar", "44100", "-ab", "192k"])
    except Exception as e:
        logging.error("Error processing TTS audio: %s", e)
        raise

    return filename

# -----------------------------------------------------------------------------
# Render a Manim scene and return the path to the output video.
# -----------------------------------------------------------------------------
def render_manim_scene(source_file: str, scene_name: str, media_dir: str = "media_output") -> str:
    """
    Renders a Manim scene in 4K, returning the path to the .mp4 file.
    """
    render_cmd = [
        "manim",
        source_file,
        scene_name,
        "-qk",  # 4K quality rendering
        "--media_dir", media_dir
    ]
    logging.info("Running Manim render command: %s", " ".join(render_cmd))
    try:
        subprocess.run(render_cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error("Manim rendering failed: %s", e)
        raise

    base_name = os.path.splitext(os.path.basename(source_file))[0]
    # Check common output folders (e.g., "1080p60" or "2160p60")
    for quality in ["2160p60", "1080p60"]:
        rendered_folder = os.path.join(media_dir, "videos", base_name, quality)
        rendered_video = os.path.join(rendered_folder, f"{scene_name}.mp4")
        if os.path.exists(rendered_video):
            return rendered_video

    raise FileNotFoundError(f"Rendered video not found in any known quality folders for scene {scene_name}")

# -----------------------------------------------------------------------------
# Main orchestrator
# -----------------------------------------------------------------------------
def main():
    # 1. Retrieve user prompt (or use a default)
    prompt = sys.argv[1] if len(sys.argv) > 1 else "power rule derivation"
    logging.info("User prompt: %s", prompt)

    # 2. Choose the scene name to render (default updated to PowerRuleScene)
    scene_name = sys.argv[2] if len(sys.argv) > 2 else "PowerRuleScene"
    logging.info("Scene to render: %s", scene_name)

    # 3. Get the improved Manim code
    try:
        manim_code = get_manim_code_from_prompt(prompt)
    except Exception as e:
        logging.error("Failed to retrieve Manim code: %s", e)
        sys.exit(1)

    # 4. Write code to a temporary .py file
    temp_filename = "generated_manim_scene.py"
    try:
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(manim_code)
        logging.info("Manim code written to: %s", temp_filename)
    except Exception as e:
        logging.error("Failed to write Manim code: %s", e)
        sys.exit(1)

    # 5. Generate a longer, natural-sounding TTS voiceover transcript
    voiceover_text = (
        "In this video, we will explore the power rule, an essential tool in calculus that helps us differentiate functions with exponents quickly. "
        "The power rule tells us that if you have a function where x is raised to a power, the derivative is simply that exponent multiplied by x raised to one less than that exponent. "
        "We begin by considering the function where x is raised to a certain power. Using the definition of the derivative, we look at the limit of the difference quotient as the small change in x, which we call h, approaches zero. "
        "Next, we expand the expression using the binomial theorem. This expansion shows that the function can be written as x raised to the original power plus the exponent times x raised to one less than that power times h, followed by additional terms involving higher powers of h. "
        "After subtracting the original function and dividing by h, taking the limit as h approaches zero causes all the terms involving h to vanish, leaving us with the elegant result: the derivative is the exponent multiplied by x raised to one less than that exponent. "
        "Along with this derivation, we will also see a graphical example using the function where x is cubed, along with its tangent line at various points. This visual demonstration helps illustrate how the derivative represents the instantaneous rate of change. "
        "Enjoy the demonstration and deepen your understanding of this fundamental concept in calculus."
    )
    voiceover_file = "voiceover_intro.wav"
    try:
        speak(voiceover_text, filename=voiceover_file)
        logging.info("Voiceover generated: %s", voiceover_file)
    except Exception as e:
        logging.error("Failed to generate voiceover: %s", e)
        sys.exit(1)

    # 6. Render the chosen Manim scene (video without audio)
    try:
        logging.info("Rendering Manim scene '%s'...", scene_name)
        rendered_video_path = render_manim_scene(temp_filename, scene_name)
    except Exception as e:
        logging.error("Failed to render Manim scene: %s", e)
        sys.exit(1)

    # 7. Move the rendered video to a known name
    video_no_audio = os.path.join(os.getcwd(), "video_without_audio.mp4")
    try:
        shutil.move(rendered_video_path, video_no_audio)
        logging.info("Rendered video moved to: %s", video_no_audio)
    except Exception as e:
        logging.error("Failed to move rendered video: %s", e)
        sys.exit(1)

    # 8. Optionally combine the voiceover audio with background music and the final video
    combine_audio_and_video = True  # Set to False if you don't want to merge
    if combine_audio_and_video:
        # Choose a random background music file from songs/*.mp3 (if any exist)
        bg_files = glob.glob(os.path.join("songs", "*.mp3"))
        bg_music = random.choice(bg_files) if bg_files else None
        if bg_music:
            logging.info("Background music selected: %s", bg_music)
            # Build ffmpeg command with three inputs: video, voiceover, and background music.
            ffmpeg_cmd = [
                "ffmpeg",
                "-y",
                "-i", video_no_audio,
                "-i", voiceover_file,
                "-i", bg_music,
                "-filter_complex",
                "[1:a]volume=1[a1]; [2:a]volume=0.3[a2]; [a1][a2]amix=inputs=2:duration=first:dropout_transition=2[a]",
                "-map", "0:v",
                "-map", "[a]",
                "-c:v", "copy",
                "-c:a", "aac",
                "-shortest",
                "video.mp4"
            ]
        else:
            logging.info("No background music found in songs/ directory. Using only voiceover.")
            # Build ffmpeg command with two inputs: video and voiceover.
            ffmpeg_cmd = [
                "ffmpeg",
                "-y",
                "-i", video_no_audio,
                "-i", voiceover_file,
                "-c:v", "copy",
                "-c:a", "aac",
                "-shortest",
                "video.mp4"
            ]
        logging.info("Combining video with voiceover (and background music if available) via ffmpeg...")
        try:
            subprocess.run(ffmpeg_cmd, check=True)
            logging.info("Final video with audio saved as: video.mp4")
        except subprocess.CalledProcessError as e:
            logging.error("FFmpeg merge failed: %s", e)
            sys.exit(1)
    else:
        logging.info("Skipping audio-video merge; final video is at %s", video_no_audio)

    # 9. At the end, print the entire voiceover transcript
    print("\n----- Voiceover Transcript -----")
    print(voiceover_text)
    print("----- End Transcript -----\n")

if __name__ == "__main__":
    main()
