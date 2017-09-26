#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Soccer Goal Definition.

TODO:

"""

from geometry.point import Point
from rendering.base import Color

class SoccerGoal:

    def __init__(self, team, colour: Color, position: Point, soccer_field):

        self.team = team
        self.colour = colour
        self.soccer_field = soccer_field

        aux = self.soccer_field.playing_area.height / 6

        self.left_post = position - Point(0, aux)
        self.right_post = position + Point(0, aux)
