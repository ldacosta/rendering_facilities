# -*- coding: utf-8 -*-
"""An Entity.

Defines an entity for this simulation.

TODO:

"""

import abc

from geometry.vector import Vec2d
from geometry.point import Point


class Entity(object): # pylint: disable=too-few-public-methods
    """The base class for objects in this simulation."""

    def __init__(self, pos: Point, radius: float, mass: float):
        self.pos = pos
        self.radius = radius
        self.mass = mass

class StaticEntity(Entity): # pylint: disable=too-few-public-methods
    """An entity that doesn't move."""

    def __init__(self, pos: Point, radius: float, mass: float):
        super().__init__(pos, radius, mass)

class MovingEntity(Entity): # pylint: disable=too-few-public-methods
    """An entity that can move."""

    def __init__(self,
                 pos: Point,
                 radius: float,
                 velocity: Vec2d,
                 max_speed: Vec2d,
                 heading: Vec2d,
                 mass: float):

        super().__init__(pos, radius, mass)
        self.velocity = velocity
        self.max_speed = max_speed
        self.heading = heading
        # vector perpendicular to the place where I am heading:
        self.side = self.heading.perpendicular()

    @abc.abstractmethod
    def move(self):
        """Definition of movement."""
        pass

    def reset(self, pos: Point):
        """Goes to a certain position, and stays there quietly."""
        self.pos = pos
        self.velocity = Vec2d(0, 0)

    def is_moving(self) -> bool:
        """Is thisentity moving?"""
        return not self.velocity.is_null()

class Container(object):
    """Container of Entities."""

    def __init__(self):
        pass

    @abc.abstractmethod
    def update_states(self):
        pass
