from manim import *


class Deaths(Scene):
    def construct(self):
        sentence = Tex('4', ',706', color=WHITE).scale(3)
        deaths = Tex('Deaths', color=WHITE).scale(3)
        sentence.shift(UP)
        deaths.shift(DOWN)
        self.wait()
        together = VGroup(sentence, deaths)
        for sentence in together:
            for word in sentence:
                self.add(word)
                self.wait()
        red_sentence = Tex('4', ',706', color=PURE_RED).scale(3)
        red_sentence.shift(UP)
        red_deaths = Tex('Deaths', color=PURE_RED).scale(3)
        red_deaths.shift(DOWN)
        red_together = VGroup(red_sentence, red_deaths)
        self.play(Transform(together, red_together))
        self.wait()
        winter_2023 = Tex('Winter 2023', color=BLUE).scale(2)
        winter_2023.shift(UP * 3)
        self.play(Transform(together, winter_2023))
        self.wait()
        uk = ImageMobject("images/uk_map.png")
        uk.scale(0.3)
        self.play(FadeIn(uk))
        self.wait()
        ratio = Tex('1', ' in ', '5 ', 'of ', 'total excess deaths', color=WHITE).set_color_by_tex(
            '1', PURE_RED
        )
        ratio.shift(DOWN * 3)
        self.play(Write(ratio))
        self.wait()
        self.play(FadeOut(uk), Unwrite(ratio), Unwrite(together))
        self.wait()


class Heating(Scene):
    def construct(self):
        self.wait()
        radiator = ImageMobject("images/radiator.png")
        radiator.shift(LEFT * 3)
        central_heating = Tex('700,000', ' without ', 'central heating', color=WHITE).set_color_by_tex(
            '700,000', BLUE
        )
        central_heating.shift(RIGHT * 3)
        self.play(Write(central_heating),
                  FadeIn(radiator), shift=UP)
        self.wait()
        self.play(FadeOut(radiator, shift=DOWN), FadeOut(central_heating, shift=DOWN))
        heating_ratio = Tex('1', ' in ', '10 ', 'elderly and ill', color=WHITE)
        heating_ratio[0].set_color(RED)
        heating_ratio.shift(DOWN * 3)
        self.wait()

        Sector.set_default(inner_radius=0, outer_radius=2, stroke_width=3, fill_opacity=0.7, stroke_color=WHITE)

        init_values = [1, 9]
        colors = [RED, BLUE]
        init_total = sum(init_values)
        init_angles = [360 * value / init_total for value in init_values]
        init_sangles = [sum(init_angles[:i]) for i in range(len(init_angles))]

        final_values = [1, 9]
        final_total = sum(final_values)
        final_angles = [360 * value / final_total for value in final_values]
        final_sangles = [sum(final_angles[:i]) for i in range(len(final_angles))]

        sectors = VGroup()
        for value, init_angle, init_sangle, final_angle, final_sangle, color in zip(init_values, init_angles,
                                                                                    init_sangles, final_angles,
                                                                                    final_sangles, colors):
            sector = Sector(
                start_angle=init_sangle * DEGREES,
                angle=init_angle * DEGREES,
                color=color,
            )
            sector.init_angle = init_angle
            sector.init_sangle = init_sangle
            sector.final_angle = final_angle
            sector.final_sangle = final_sangle
            sectors.add(sector)

        for sector in sectors:
            sector.save_state()

        def update_sector(sector, alpha):
            sector.restore()
            angle = interpolate(sector.init_angle * DEGREES, sector.final_angle * DEGREES, alpha)
            start_angle = interpolate(sector.init_sangle * DEGREES, sector.final_sangle * DEGREES, alpha)
            sector.become(
                Sector(
                    start_angle=start_angle,
                    angle=angle,
                    color=sector.color,
                )
            )

        self.play(Create(sectors), Write(heating_ratio))
        self.add(Circle(radius=2, color=WHITE, stroke_width=2))
        self.wait()

