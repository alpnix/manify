
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
