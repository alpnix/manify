from manim import *

class PowerRuleExplanation(Scene):
    def construct(self):
        # Title and Introduction
        title = Tex("The Power Rule for Derivatives").scale(1.5)
        subtitle = Tex("If $f(x) = x^n$, then $f'(x) = nx^{n-1}$").next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Step 1: Function Definition
        func_eq = Tex(r"f(x) = x^n").scale(1.5)
        self.play(Write(func_eq))
        self.wait(2)
        
        # Step 2: Derivative Process
        derivative_eq = Tex(r"f'(x) = nx^{n-1}").scale(1.5).next_to(func_eq, DOWN)
        self.play(Transform(func_eq, derivative_eq))
        self.wait(2)
        
        # Step 3: Visualization of the Power Rule
        graph_axes = Axes(
            x_range=[-4, 4],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )
        graph = graph_axes.plot(lambda x: x**3, color=WHITE)  # Example: f(x) = x^3
        graph_label = graph_axes.get_graph_label(graph, label='x^3')
        
        self.play(Create(graph_axes), Create(graph), Write(graph_label))
        self.wait(2)

        # Step 4: Tangent Line and Derivative Visualization
        tangent_line = graph_axes.plot(lambda x: 3*x**2, color=YELLOW)  # Example: derivative of x^3 is 3x^2
        tangent_label = graph_axes.get_graph_label(tangent_line, label='3x^2')
        
        self.play(Transform(graph, tangent_line), Transform(graph_label, tangent_label))
        self.wait(2)
        
        # Step 5: Zoom-In and Focus on the Derivative at a Point
        dot_on_curve = Dot(color=RED).move_to(graph_axes.c2p(2, 2**3))  # Dot at x=2
        tangent_dot = Dot(color=GREEN).move_to(graph_axes.c2p(2, 3*2**2))  # Dot on tangent line at x=2
        self.play(FadeIn(dot_on_curve), FadeIn(tangent_dot))
        self.wait(2)
        
        # Step 6: Animation of Moving Points on the Graph and Derivative
        self.play(
            dot_on_curve.animate.move_to(graph_axes.c2p(3, 3**3)),
            tangent_dot.animate.move_to(graph_axes.c2p(3, 3*3**2))
        )
        self.wait(2)
        
        # Step 7: Conclusion and Recap
        recap_text = Tex(
            "In conclusion, the power rule states that the derivative of $x^n$ is $nx^{n-1}$."
        ).scale(1.2).to_edge(DOWN)
        self.play(Write(recap_text))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(graph_axes), FadeOut(recap_text), FadeOut(dot_on_curve), FadeOut(tangent_dot))
        self.wait(1)