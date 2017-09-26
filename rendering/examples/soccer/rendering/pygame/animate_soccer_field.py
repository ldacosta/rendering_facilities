import pygame
from pygame.color import THECOLORS

from rendering.examples.soccer.dynamics.soccer_field import SoccerField
from rendering.examples.soccer.rendering.pygame.soccer_field import SoccerFieldPygameRenderable
from rendering.pygame.base import pygame_render

if __name__ == "__main__":
    import sys

    WIDTH, HEIGHT = 1200, 800
    FPS = 30

    pygame.init()

    clock = pygame.time.Clock()
    # field
    soccer_field = SoccerField(name = "Estadio Centenario de Montevideo")
    # all renderings
    soccer_field_renderable = SoccerFieldPygameRenderable(soccer_field)

    # Let's get ready to display:
    pygame.display.set_caption(soccer_field.name)
    surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    while True:
        tick_time = clock.tick(FPS)
        surface.fill(THECOLORS['green']) # this is basically a CLEAR. TODO: can we do something better????

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        soccer_field.update_states()
        pygame_render(soccer_field_renderable.representation(), surface)
        pygame.display.update()
