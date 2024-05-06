from manim import *


class Retrofitting(Scene):
    def construct(self):
        retrofitting = Tex("Retrofitting", color=BLUE, stroke_width=2).scale(3)
        self.play(Write(retrofitting))
        definition = Tex('the addition of new technology or features to older systems', color=WHITE)
        definition.shift(DOWN)
        self.wait()
        self.play(retrofitting.animate.shift(UP),
            Write(definition))
        self.wait()
        self.play(Unwrite(retrofitting),
            Unwrite(definition))
        self.wait()
        cog = ImageMobject("images/cog.png").scale(0.1).shift(UP * 2)
        professional = ImageMobject("images/professional.png").scale(1.2)
        inaccurate = ImageMobject("images/inaccurate.png").scale(1.2).shift(DOWN * 2)
        self.play(FadeIn(cog, shift=RIGHT))
        self.wait()
        self.play(FadeIn(professional, shift=LEFT))
        self.wait()
        self.play(FadeIn(inaccurate, shift=RIGHT))
        self.wait()
        self.play(FadeOut(cog, shift=UP),
            FadeOut(professional, shift=UP),
            FadeOut(inaccurate, shift=UP))
        self.wait()
        survey = Tex('2021 Opinions and Lifestyle', color=BLUE).scale(2)
        survey.shift(UP * 3)
        self.play(Write(survey))
        self.wait()
        energy_ratio = Tex('1 ', 'out of 5', color=WHITE).set_color_by_tex(
            '1', GREEN
        ).scale(2)
        energy_efficiency = Tex('considered improving home energy efficiency', color=WHITE)
        energy_efficiency.shift(DOWN * 2)
        self.play(Write(energy_efficiency),
                  Write(energy_ratio))
        self.wait()
        self.play(Unwrite(energy_efficiency),
                  Unwrite(energy_ratio))
        of_those = Tex('Of those who were not considering any improvements:', color=WHITE)
        costs_ratio = Tex('1 ', 'out of 4', color=WHITE).set_color_by_tex(
            '1', YELLOW
        ).scale(2)
        prohibitive_costs = Tex('considered prohibitive costs as the primary deterrent', color=WHITE)
        prohibitive_costs.shift(DOWN * 3)
        of_those.shift(DOWN)
        costs_ratio.shift(DOWN)
        self.play(Write(of_those))
        self.wait()
        self.play(of_those.animate.shift(UP * 2))
        self.wait()
        self.play(Write(costs_ratio),
            Write(prohibitive_costs))
        self.wait()
        self.play(Unwrite(survey),
            Unwrite(of_those),
            Unwrite(prohibitive_costs),
            Unwrite(costs_ratio))
        self.wait()


class House(ThreeDScene):
    def construct(self):
        dot = Dot()
        line = Rectangle(width=2, height=0.0000001)
        rect = Rectangle(width=2, height=2)
        cuboid = Prism([2, 2, 2], stroke_color=BLUE, color=BLUE_E).rotate(-90 * DEGREES, X_AXIS).rotate(45 * DEGREES, Y_AXIS).shift([0, -1, 0])
        vertex_coords = [
            [1.3, 1.3, 0],
            [1.3, -1.3, 0],
            [-1.3, -1.3, 0],
            [-1.3, 1.3, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list).rotate(-90 * DEGREES, X_AXIS).rotate(45 * DEGREES,Y_AXIS).shift([0, 11, 0])
        self.play(Create(dot))
        self.wait(1.5)
        self.play(ReplacementTransform(dot, line))
        self.wait(1.5)
        self.play(ReplacementTransform(line, rect))
        self.wait(1.5)
        self.play(rect.animate.shift([0, -2, 0]))
        self.play(Rotate(rect, -90 * DEGREES, X_AXIS))
        self.wait(0.000000001)
        self.play(Rotate(rect, 45 * DEGREES, Y_AXIS))
        self.play(Transform(rect, cuboid))
        self.wait()
        self.add(pyramid)
        self.remove(pyramid.graph)
        self.wait(1)
        self.play(pyramid.animate.shift([0, -10, 0]))
        self.wait()
        self.play(Rotating(pyramid, radians=PI * 1.25, axis=UP),
                  Rotating(rect, radians=PI * 1.25, axis=UP))
        self.play(pyramid.animate.set_color(GREEN),
                  rect.animate.set_color(GREEN))
        self.wait(1)