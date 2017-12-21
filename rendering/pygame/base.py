# -*- coding: utf-8 -*-
"""Base class for Rendering on pygame.

TODO:

"""

import abc
from typing import List, Tuple
import pygame
from pygame.colordict import THECOLORS

from rendering.base import Color

def base_color_2_pygame_color(base_color: Color) -> Tuple[(int, int, int)]:
    return THECOLORS[base_color.value]

class DrawingRect(object): # pylint: disable=too-few-public-methods
    """What to draw in a rectangle."""

    def __init__(self, top: float, left: float, width: float, height: float, color: Color, lines_thickness: int):
        self.shape = pygame.rect.Rect(left, top, width, height)
        self.color = base_color_2_pygame_color(color)
        self.lines_thickness = lines_thickness

class DrawingCircle(object): # pylint: disable=too-few-public-methods
    """What to draw in a circle."""

    def __init__(self, center: Tuple[float, float], radius: float, color: Color, line_thickness: int = 2):
        self.center = tuple(map(int, center))
        self.radius = int(radius)
        self.color = base_color_2_pygame_color(color)
        self.line_thickness = line_thickness

class DrawingLine(object): # pylint: disable=too-few-public-methods
    """What to draw in a line."""

    def __init__(self, begin: Tuple[float, float], end: Tuple[float, float], color: Color, thickness: int = 2):
        self.begin = tuple(map(int, begin))
        self.end = tuple(map(int, end))
        self.color = base_color_2_pygame_color(color)
        self.line_thickness = thickness

class DrawingObjects(object): # pylint: disable=too-few-public-methods
    """What to draw in a serioes of objects."""

    def __init__(self, rects: List[DrawingRect], circles: List[DrawingCircle], lines: List[DrawingLine]):
        self.rects = rects
        self.circles = circles
        self.lines = lines

    def __add__(self, other):
        return DrawingObjects(
            rects=self.rects + other.rects,
            circles=self.circles + other.circles,
            lines=self.lines + other.lines)

def pygame_render(objects_to_draw: DrawingObjects, surface):
    """Render a bunch of objects."""

    for rect in objects_to_draw.rects:
        pygame.draw.rect(surface, rect.color, rect.shape, rect.lines_thickness)
    for circle in objects_to_draw.circles:
        #pygame.draw.circle(surface, circle.color, (2,3), circle.radius, circle.line_thickness)
        pygame.draw.circle(surface, circle.color, circle.center, circle.radius, circle.line_thickness)
    for a_line in objects_to_draw.lines:
        pygame.draw.line(surface, a_line.color, a_line.begin, a_line.end, a_line.line_thickness)


class Renderable(object): # pylint: disable=too-few-public-methods
    """An object that can be rendered."""

    def __init__(self):
        pass

    @abc.abstractmethod
    def representation(self) -> DrawingObjects:
        """How is this object represented, in drawing objects."""
        pass
