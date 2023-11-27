%%manim -v WARNING -qm Start


class Start(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        triangle = Triangle(color=BLACK).rotate(PI/6).set_fill(YELLOW,1)
        line1 = Line(color=BLACK).rotate(PI/6).scale(1/4).shift(LEFT*5/28).shift(DOWN*1/4)
        line2 = Line(color=BLACK).rotate(PI/6).scale(1/4).shift(RIGHT*1/7).shift(UP*3/9)
        text = Tex("FAT PIPE Start 98 Kunratice").shift(DOWN * 2.5).set_color(BLACK,1)
        
        
        self.play(Write(triangle), Write(line1), Write(line2))
        self.play(FadeIn(text))
        
        self.play(FadeOut(text, run_time=3))
        self.play(FadeOut(triangle, run_time=2), FadeOut(line1, run_time=2), FadeOut(line2, run_time=2))
    
