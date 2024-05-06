from manim import *


class HousingStock(Scene):
    def construct(self):
        europe_map = ImageMobject("images/europe_map.png").scale(1.3)
        self.play(FadeIn(europe_map))
        self.wait()
        square_house = Rectangle(height=1.5, width=2, fill_color=GOLD, fill_opacity=1, stroke_width=0)
        point_A = [-1.4, -1, 0]
        point_B = [1.4, -1, 0]
        point_C = [0, 0.4, 0]
        triangle_house = Polygon(point_A, point_B, point_C, fill_color=PURE_RED, fill_opacity=1, stroke_width=0)
        triangle_house.shift(UP * 1.5)
        house = VGroup(square_house, triangle_house)
        house.scale(0.5)
        house.shift(UP * 1.1 + LEFT * 4.4)
        white_rectangle = Rectangle(height=3.55, width=3.3, fill_color=WHITE)
        white_rectangle.shift(UP * 2.2 + LEFT * 5.2)
        self.play(Create(white_rectangle),
                  FadeIn(house, shift=UP))
        self.wait()
        self.play(FadeToColor(square_house, WHITE),
                  FadeToColor(triangle_house, GREY))
        self.play(FadeOut(triangle_house, shift=UP),
                  FadeOut(square_house, shift=DOWN),
                  Uncreate(white_rectangle))
        self.wait()
        self.play(FadeOut(europe_map, scale=0.5))
        self.wait()
        temperature_loss = ImageMobject("images/temperature_loss.png")
        uk_bar = Rectangle(height=0.25, width=5.85, fill_color=ManimColor('#196693'), fill_opacity=1, stroke_width=0);
        uk_bar.shift(UP * 1.8 + RIGHT * 0.15)
        self.play(FadeIn(temperature_loss, scale=0.5))
        self.wait()
        self.play(GrowFromEdge(uk_bar, LEFT))
        self.wait()
        self.play(FadeToColor(uk_bar, PURE_RED))
        self.wait()
        self.play(FadeOut(uk_bar),
                  FadeOut(temperature_loss))
        self.wait()
        epc_ratings = ImageMobject("images/epc_ratings.png").scale(1.5)
        self.play(FadeIn(epc_ratings))
        self.wait()
        self.play(FadeOut(epc_ratings))
        self.wait()
        percentage_carbon = Text('26%', color=PURE_RED).scale(2)
        percentage_carbon.shift(LEFT)
        co2 = Tex('CO2', color=WHITE)
        co2.shift(UP * 0.25 + RIGHT)
        emissions = Tex('emissions', color=WHITE)
        emissions.shift(UP * (-0.25) + RIGHT * 1.55)
        arrow = Arrow(UP * -1 + LEFT, UP * 1 + LEFT, color=PURE_RED, stroke_width=5)
        arrow.shift(LEFT * 2)
        self.play(Write(percentage_carbon),
                  GrowArrow(arrow))
        self.wait()
        self.play(Write(co2),
                  Write(emissions))
        self.wait()
        self.play(Unwrite(percentage_carbon),
                  Uncreate(arrow),
                  Unwrite(co2),
                  Unwrite(emissions))
        energy_bills = Tex(r'$\pounds$6.4 billion', color=GREEN).scale(2)
        self.play(Write(energy_bills))
        self.wait()
        cross = Cross(mobject=energy_bills, stroke_color=PURE_RED, stroke_width=6)
        self.play(Create(cross), run_time=4)
        self.wait()
        self.play(FadeOut(energy_bills, shift=DOWN * 5),
                  FadeOut(cross, shift=DOWN * 5))


class Government(Scene):
    def construct(self):
        self.wait()
        retrofits_graph = ImageMobject("images/retrofits_graph.png").scale(1.5)
        self.play(FadeIn(retrofits_graph))
        self.wait()
        self.play(FadeOut(retrofits_graph))
        green_homes_grant = ImageMobject("images/green_homes_grant.png").scale(2)
        self.play(FadeIn(green_homes_grant))
        self.wait()
        self.play(FadeOut(green_homes_grant))
        self.wait()
