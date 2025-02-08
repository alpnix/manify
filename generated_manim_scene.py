
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
