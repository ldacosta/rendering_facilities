from rendering.examples.soccer.dynamics.soccer_ball import SoccerBall
from rendering.base import Color
from rendering.pygame.base import DrawingObjects, DrawingCircle, Renderable


class SoccerBallPygameRenderable(Renderable):

    def __init__(self, soccer_ball: SoccerBall):
        self.ball = soccer_ball
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[],
            circles=[
                DrawingCircle(
                    center=self.ball.pos.as_tuple(),
                    radius=self.ball.radius,
                    color=Color.BLACK,
                    line_thickness=2)],
            lines=[])
