#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Soccer Region Definition.

TODO:

"""

from geometry.shapes import Rect

class SoccerRegion:
    """Region on a Soccer Field."""

    def __init__(self, region_id, rect: Rect, soccer_field):

        self.an_id = region_id
        self.rect = rect
        self.soccer_field = soccer_field
