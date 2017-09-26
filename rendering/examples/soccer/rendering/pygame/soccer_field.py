from functools import reduce

from rendering.examples.soccer.rendering.pygame.soccer_goal import SoccerGoalPygameRenderable
from rendering.examples.soccer.rendering.pygame.soccer_region import SoccerRegionPygameRenderable
from rendering.examples.soccer.rendering.pygame.soccer_team import SoccerTeamPygameRenderable

from rendering.base import Color
from rendering.examples.soccer.dynamics.soccer_field import SoccerField
from rendering.examples.soccer.rendering.pygame.soccer_ball import SoccerBallPygameRenderable
from rendering.pygame.base import DrawingObjects, DrawingRect, DrawingCircle, DrawingLine, Renderable

class SoccerFieldPygameRenderable(Renderable):

    def __init__(self, soccer_field: SoccerField):
        self.field = soccer_field
        super().__init__()

    def representation(self) -> DrawingObjects:
        field = DrawingObjects(
            rects=[
                DrawingRect(top=self.field.playing_area.top,left=self.field.playing_area.left,width=self.field.playing_area.width,height=self.field.playing_area.height,
                    color=Color.WHITE,
                    lines_thickness=3)],
            circles=[
                DrawingCircle(
                    center=self.field.playing_area.center.as_tuple(),
                    radius=10,
                    color=Color.WHITE,
                    line_thickness=2),
                DrawingCircle(
                    center=self.field.playing_area.center.as_tuple(),
                    radius=75,
                    color=Color.WHITE,
                    line_thickness=2)],
            lines=[
                DrawingLine(
                    begin=self.field.playing_area.midtop.as_tuple(),
                    end=self.field.playing_area.midbottom.as_tuple(),
                    color=Color.WHITE,
                    thickness=2)])
        ball = SoccerBallPygameRenderable(soccer_ball=self.field.ball).representation()
        goal_1 = SoccerGoalPygameRenderable(soccer_goal=self.field.goals['red']).representation()
        goal_2 = SoccerGoalPygameRenderable(soccer_goal=self.field.goals['blue']).representation()
        team_1 = SoccerTeamPygameRenderable(team=self.field.teams['red']).representation()
        team_2 = SoccerTeamPygameRenderable(team=self.field.teams['blue']).representation()
        regions_list = []
        for key, region in self.field.regions.items():
            regions_list.append(SoccerRegionPygameRenderable(region).representation())
        regions = reduce(lambda repr1, repr2: repr1 + repr2, regions_list)
        return field + ball + goal_1 + goal_2 + team_1 + team_2 + regions


