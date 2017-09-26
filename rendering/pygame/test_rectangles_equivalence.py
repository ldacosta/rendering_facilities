# -*- coding: utf-8 -*-
"""Unit Tests for Player.

This module tests all there is a for an abstract Player.

Attributes:
    None

TODO:

"""

import unittest

from coordinates import CoordinatesDirection
from point import Point as OurPoint
from shapes import Rect as OurOwnRect

from rendering.pygame import Rect as PygameRect

# Field coordinates.
WIDTH, HEIGHT = 1200, 800
TOP_LEFT = (50, 50)
WIDTH_HEIGHT = (1050, 720)


class TestRectangles(unittest.TestCase):
    """Simple sanity check for Rectangles equivalence."""

    def test_eq(self):
        a_rect_pygame = PygameRect(TOP_LEFT, WIDTH_HEIGHT)
        top_left_pt = OurPoint.from_tuple(TOP_LEFT)
        a_rect = OurOwnRect(direction=CoordinatesDirection.SCREEN_DIRECTION, pt1=top_left_pt,
                            pt2=OurPoint(x=top_left_pt.x + WIDTH_HEIGHT[0],
                                         y=top_left_pt.y + WIDTH_HEIGHT[1]))

        #
        print("Rect Pygame bottom => ")
        print(a_rect_pygame.bottom)
        print(a_rect.bottom)
        #
        print("Rect Pygame center => ")
        print(a_rect_pygame.center)
        print(a_rect.center)
        #
        print("Rect Pygame bottomright => ")
        print(a_rect_pygame.bottomright)
        print(a_rect.bottomright)
        #
        print("Rect Pygame bottomleft => ")
        print(a_rect_pygame.bottomleft)
        print(a_rect.bottomleft)
        #
        print("Rect Pygame topleft => ")
        print(a_rect_pygame.topleft)
        print(a_rect.topleft)
        #
        print("Rect Pygame topright => ")
        print(a_rect_pygame.topright)
        print(a_rect.topright)
        #
        print("Rect Pygame top => ")
        print(a_rect_pygame.top)
        print(a_rect.top)
        #
        print("Rect Pygame midbottom => ")
        print(a_rect_pygame.midbottom)
        print(a_rect.midbottom)
        #
        print("Rect Pygame height => ")
        print(a_rect_pygame.height)
        print(a_rect.height)
        #
        print("Rect Pygame width => ")
        print(a_rect_pygame.width)
        print(a_rect.width)
        #
        print("Rect Pygame midleft => ")
        print(a_rect_pygame.midleft)
        print(a_rect.midleft)
        #
        print("Rect Pygame midright => ")
        print(a_rect_pygame.midright)
        print(a_rect.midright)
        #
        print("Rect Pygame midtop => ")
        print(a_rect_pygame.midtop)
        print(a_rect.midtop)

        # print("[pygame's Rect] x = %f,  y = %f" % (a_rect_pygame.x, a_rect_pygame.y))
        # print("[OurOwnRect   ] x = %f,  y = %f" % (a_rect., a_rect.y))
