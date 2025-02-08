from manim import *

config["media_dir"] = "."
config["video_dir"] = "."

class TriangularNumberProofCentered(Scene):
    def construct(self):
        # --- Title ---
        title = Text("Proof: 1 + 2 + ... + n = n(n+1)/2", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # ----------------------------------------------------------------
        # 1) Build the first triangle, largest row at the bottom.
        # ----------------------------------------------------------------
        n = 6
        square_size = 0.5
        buff = 0.06  # spacing so squares do not overlap

        triangle_1 = VGroup()
        for row_count in range(n, 0, -1):  # n down to 1
            row = VGroup(*[
                Square(
                    side_length=square_size,
                    stroke_color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.7,
                ) for _ in range(row_count)
            ])
            row.arrange(RIGHT, buff=buff)
            triangle_1.add(row)

        # Stack rows upward; largest row is at the bottom
        triangle_1.arrange(UP, aligned_edge=LEFT, buff=0)

        # Create on screen
        self.play(Create(triangle_1))
        self.wait()

        # ----------------------------------------------------------------
        # 2) Copy, rotate 180°, and place to the right to form the rectangle
        #    so each horizontal row has (n+1) squares total.
        # ----------------------------------------------------------------
        triangle_2 = triangle_1.copy()
        triangle_2.rotate(PI)  # 180 degrees

        # Position triangle_2 so that its bottom row meets the top row of the first
        # in a way that completes each row to (n+1) squares.
        # We'll just place it to the right with no horizontal buff:
        triangle_2.next_to(triangle_1, RIGHT, buff=0)

        self.play(TransformFromCopy(triangle_1, triangle_2))
        self.wait()

        # Group them together
        full_rect_group = VGroup(triangle_1, triangle_2)

        # ----------------------------------------------------------------
        # 3) Surrounding rectangle, dimension arrows, etc.
        # ----------------------------------------------------------------
        box = SurroundingRectangle(full_rect_group, buff=0.15, color=YELLOW)
        self.play(Create(box))
        self.wait()

        # Arrows for dimensions (height = n, width = n+1)
        top_left = box.get_corner(UL)
        top_right = box.get_corner(UR)
        bottom_left = box.get_corner(DL)

        arrow_width = Arrow(top_left, top_right, buff=0.1, color=GREEN)
        label_width = Text("n+1", font_size=32)
        label_width.next_to(arrow_width, UP)

        arrow_height = Arrow(top_left, bottom_left, buff=0.1, color=GREEN)
        label_height = Text("n", font_size=32)
        label_height.next_to(arrow_height, LEFT)

        self.play(Create(arrow_width), Write(label_width))
        self.wait()
        self.play(Create(arrow_height), Write(label_height))
        self.wait()

        # ----------------------------------------------------------------
        # 4) Center everything and finalize
        # ----------------------------------------------------------------
        # Move the entire group (triangles + box + arrows + labels) to the screen center
        # so that the rectangle is nicely centered.
        everything = VGroup(full_rect_group, box, arrow_width, label_width, arrow_height, label_height)
        everything.move_to(ORIGIN)

        # Show final text
        area_text = Text("Area = n(n+1)", font_size=36)
        area_text.next_to(box, DOWN)
        self.play(Write(area_text))
        self.wait()

        eq_text = Text("1 + 2 + ... + n = n(n+1)/2", font_size=40)
        eq_text.next_to(area_text, DOWN, buff=0.4)
        self.play(Write(eq_text))
        self.wait(2)

        closing = Text("Hence, the sum of the first n natural numbers is n(n+1)/2!", font_size=28)
        closing.next_to(eq_text, DOWN)
        self.play(Write(closing))
        self.wait(3)

# --- Automatic Rendering ---
if __name__ == "__main__":
    scene = TriangularNumberProofCentered()
    scene.renderer.file_writer.output_file = "output.mp4"
    scene.render()
