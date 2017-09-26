from rendering.examples.soccer.dynamics.soccer_goal import SoccerGoal
from rendering.pygame.base import DrawingObjects, DrawingLine, Renderable


class SoccerGoalPygameRenderable(Renderable):

    def __init__(self, soccer_goal: SoccerGoal):
        self.goal = soccer_goal
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[],
            circles=[],
            lines=[
                DrawingLine(
                begin=self.goal.left_post.as_tuple(),
                end=self.goal.right_post.as_tuple(),
                color=self.goal.colour,
                thickness=6)])