#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Soccer Goal Definition.

TODO:

"""

from rendering.examples.dynamics.particle import Particle
from geometry.vector import Vec2d
from rendering.examples.soccer.dynamics.SteeringBehaviours import SteeringBehaviours
from geometry.point import Point
from rendering.base import Color

class SoccerPlayer(Particle):

    def __init__(self, team, colour: Color, number: int, pos: Point, soccer_field):

        super().__init__(pos, 15, Vec2d(0, 0), Vec2d(4, 4), Vec2d(soccer_field.playing_area.center), 1)

        self.team = team
        self.colour = colour
        self.number = number
        self.initial_pos = pos
        self.soccer_field = soccer_field
        a_pt = soccer_field.playing_area.center - pos

        self.direction = Vec2d(x_or_pair=(a_pt.x, a_pt.y)).normalized()

        self.steering_behaviours = SteeringBehaviours(self, soccer_field.ball)

        self.steering_behaviours.activated['arrive'] = True

    def reset(self, pos): # TODO: this parameter is not used.
        self.pos = self.initial_pos

    def warm_up(self):
        """Runs back and forth between the ball and a random point in the field."""
        self.velocity = self.steering_behaviours.calculate()
        self.pos += self.velocity
        self.pos = Point(int(self.pos.x), int(self.pos.y))
        if not self.is_moving():
            if self.steering_behaviours.target == self.soccer_field.ball.pos:
                # let's go back towards where I was.
                self.steering_behaviours.target = self.initial_pos
            else:
                # let's go towards the ball.
                self.steering_behaviours.target = self.soccer_field.ball.pos
        self.direction = Vec2d(self.steering_behaviours.target - self.pos).normalized()

    def move(self):
        self.warm_up()
