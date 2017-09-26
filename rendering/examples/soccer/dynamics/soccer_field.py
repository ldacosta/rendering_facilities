#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Soccer Field Definition.

TODO:

"""

from rendering.examples.dynamics.entity import Container
from geometry.coordinates import CoordinatesDirection
from rendering.base import Color
from geometry.shapes import Rect
from geometry.point import Point as OurPoint
from rendering.examples.soccer.dynamics import Global
from rendering.examples.soccer.dynamics.Wall2d import Wall2d
from rendering.examples.soccer.dynamics.soccer_ball import SoccerBall
from rendering.examples.soccer.dynamics.soccer_goal import SoccerGoal
from rendering.examples.soccer.dynamics.soccer_team import SoccerTeam

from rendering.examples.soccer.dynamics.soccer_region import SoccerRegion
from geometry.vector import Vec2d


class SoccerField(Container):

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        top_left_pt = OurPoint.from_tuple(Global.TOP_LEFT)
        self.playing_area = Rect(
            direction=CoordinatesDirection.SCREEN_DIRECTION,
            pt1=top_left_pt,
            pt2=OurPoint(x=top_left_pt.x + Global.WIDTH_HEIGHT[0], y=top_left_pt.y + Global.WIDTH_HEIGHT[1]))

        # Walls para detectar cuándo el balón sale del terreno de juego.
        self.walls = []

        top_left = Vec2d(self.playing_area.topleft)
        top_right = Vec2d(self.playing_area.topright)
        bottom_left = Vec2d(self.playing_area.bottomleft)
        bottom_right = Vec2d(self.playing_area.bottomright)

        self.walls.append(Wall2d(top_left, top_right))
        self.walls.append(Wall2d(top_right, bottom_right))
        self.walls.append(Wall2d(top_left, bottom_left))
        self.walls.append(Wall2d(bottom_left, bottom_right))

        # Zonas importantes en el campo.
        self.regions = {}
        for i in range(0, 7):
            for j in range(0, 4):
                an_id = i * 4 + j
                rect = Rect.from_topleft_widthheight(50 + i * 150, 50 + j * 180, 150, 180)
                self.regions[an_id] = SoccerRegion(an_id, rect, self)

        # Balón.
        self.ball = SoccerBall(pos=self.playing_area.center, size=10, mass=2,
                               velocity=Vec2d(1, 10), soccer_field=self)
        # Equipos
        self.teams = {}
        self.teams[Color.RED.value] = SoccerTeam(Color.RED.value, Color.RED, 4, self)
        self.teams[Color.BLUE.value] = SoccerTeam(Color.BLUE.value, Color.BLUE, 4, self)

        # Porterías.
        self.goals = {}
        self.goals[Color.RED.value] = SoccerGoal(Color.RED.value, Color.RED, self.playing_area.midleft, self)
        self.goals[Color.BLUE.value] = SoccerGoal(Color.BLUE.value, Color.BLUE, self.playing_area.midright, self)

    def update_states(self):
        self.ball.move()
        self.teams[Color.RED.value].move_players()
        self.teams[Color.BLUE.value].move_players()
