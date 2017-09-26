from rendering.examples.soccer.dynamics.soccer_player import SoccerPlayer
from rendering.pygame.base import Renderable, DrawingObjects, DrawingCircle, DrawingLine


class SoccerPlayerPygameRenderable(Renderable):

    def __init__(self, soccer_player: SoccerPlayer):
        self.player = soccer_player
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[],
            circles=[ # actual position
                DrawingCircle(
                    center=self.player.pos.as_tuple(),
                    radius=self.player.radius,
                    color=self.player.colour,
                    line_thickness=0)],
            lines=[ # direction
                DrawingLine(
                    begin=self.player.pos.as_tuple(),
                    end=self.player.pos.translate_following(((self.player.radius * 2) * self.player.direction)).as_tuple(),
                    color=self.player.colour,
                    thickness=6)])