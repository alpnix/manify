# maker.py
from manim import *
import numpy as np
import sys
import os
import shutil

class ContentCreatorEducationalApp(Scene):
    def __init__(self, prompt="Default Prompt", **kwargs):
        self.prompt = prompt
        super().__init__(**kwargs)

    def construct(self):
        # === Title Screen with the Prompt ===
        title = Text(f"Prompt: {self.prompt}", font_size=56)
        subtitle = Text("Narrated in the style of 3Blue1Brown", font_size=36)
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # === Section 1: Visual Storytelling ===
        heading1 = Text("Visual Storytelling", font_size=48)
        heading1.to_edge(UP)
        self.play(Write(heading1))
        self.wait(1)
        # Morph a circle into a square.
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=4, color=RED)
        square.move_to(circle.get_center())
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(FadeOut(square))
        self.play(FadeOut(heading1))

        # === Section 2: Engaging Explanations with Graphs ===
        heading2 = Text("Engaging Explanations", font_size=48)
        heading2.to_edge(UP)
        self.play(Write(heading2))
        self.wait(1)
        # Plotting a sine wave.
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False
        )
        sine_wave = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[0, 10])
        self.play(Create(axes), run_time=2)
        self.play(Create(sine_wave), run_time=2)
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(sine_wave), FadeOut(heading2))

        # === Conclusion ===
        conclusion = Text("Keep creating. Keep inspiring.", font_size=40)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))

if __name__ == "__main__":
    # Retrieve the prompt from command-line arguments (if provided)
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Default Prompt"
    scene = ContentCreatorEducationalApp(prompt=prompt)
    scene.render()

    # Get the rendered video's path.
    output_path = scene.renderer.file_writer.movie_file_path
    print("Rendered video at:", output_path)

    # Define the destination (save as "video.mp4" in the public directory).
    destination_dir = os.path.join(os.getcwd(), "")
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    destination = os.path.join(destination_dir, "video.mp4")

    # Move the rendered file to the destination.
    shutil.move(output_path, destination)
    print("Video moved/renamed to:", destination)
