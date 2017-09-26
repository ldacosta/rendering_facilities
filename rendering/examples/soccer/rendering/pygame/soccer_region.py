from rendering.examples.soccer.dynamics.soccer_region import SoccerRegion
from rendering.pygame.base import DrawingObjects, DrawingRect, Renderable
from rendering.base import Color

class SoccerRegionPygameRenderable(Renderable):

    def __init__(self, soccer_region: SoccerRegion):
        self.region = soccer_region
        super().__init__()

    def representation(self) -> DrawingObjects:
        return DrawingObjects(
            rects=[
                DrawingRect(
                    top=self.region.rect.top,
                    left=self.region.rect.left,
                    width=self.region.rect.width,
                    height=self.region.rect.height,
                    color=Color.WHITE,
                    lines_thickness=1)
            ],
            circles=[],
            lines=[])
