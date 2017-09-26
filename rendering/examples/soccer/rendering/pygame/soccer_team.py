from functools import reduce

from rendering.examples.soccer.dynamics.soccer_team import SoccerTeam
from rendering.examples.soccer.rendering.pygame.soccer_player import SoccerPlayerPygameRenderable
from rendering.pygame.base import Renderable, DrawingObjects


class SoccerTeamPygameRenderable(Renderable):


    def __init__(self, team: SoccerTeam):
        self.team = team
        super().__init__()

    def representation(self) -> DrawingObjects:
        return reduce(
                    lambda repr_1, repr_2: repr_1 + repr_2,
                    map(lambda player: SoccerPlayerPygameRenderable(player).representation(), self.team.players))