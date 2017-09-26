# -*- coding: utf-8 -*-
"""A Particle.

TODO:

"""

from rendering.examples.dynamics.entity import MovingEntity
from geometry.vector import Vec2d
from geometry.point import Point


class Particle(MovingEntity): # pylint: disable=too-few-public-methods

    def __init__(self,
                 pos: Point,
                 radius: float,
                 velocity: Vec2d,
                 max_speed: Vec2d,
                 heading: Vec2d,
                 mass: float):
        super().__init__(pos, radius, velocity, max_speed, heading, mass)
