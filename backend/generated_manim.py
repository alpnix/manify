from manim import *

class QuadraticEquation(Scene):
    def construct(self):
        question = Text("What is the quadratic equation?")
        equation = MathTex("ax^2 + bx + c = 0")

        self.play(Write(question))
        self.wait(2)
        self.play(Transform(question, equation))
        self.wait(2)