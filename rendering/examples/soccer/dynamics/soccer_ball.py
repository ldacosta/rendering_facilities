#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dynamics of a Soccer Team.

TODO:

"""

from geometry.vector import Vec2d
from geometry.point import Point
from rendering.examples.dynamics.particle import Particle
from rendering.examples.soccer.dynamics import Global


class SoccerBall(Particle):

    def __init__(self, pos: Point, size: float, mass: float, velocity: Vec2d, soccer_field):

        super().__init__(pos, size, velocity, velocity, Vec2d(soccer_field.playing_area.center), mass)

        self.old_pos = pos

        self.soccer_field = soccer_field
        self.walls = soccer_field.walls
        self.direction = Vec2d(20, 0)


    def collides_with_walls(self) -> bool:
        """Checks if ball collides with walls."""
        for a_wall in self.walls:
            if a_wall.dist_to(self.pos) < Global.TOUCHLINE:
                return True
        return False

    def reset_on_wall_collision(self):
        """Behaviour when it collides with walls."""

        if self.collides_with_walls():
            self.reset(self.pos)

    def kick(self, direction: Vec2d, force: Vec2d):
        """Kick of a ball on a certain direction."""
        
        # Normaliza la dirección.
        direction = direction.normalized()
        # Calculo de la aceleración.
        acceleration = (direction * force) / self.mass
        # Actualiza la velocidad.
        self.velocity = acceleration

    # Devuelve la posición del balón en el futuro.
    # TODO: this is serious bad-design.
    def futurePosition(self, time):

        # u = velocidad de inicio.
        # Cálculo del vector ut.
        ut = self.velocity * time

        # Cálculo de 1/2*a*t*t, que es un escalar.
        half_a_t_squared = 0.5 * Global.FRICTION * time * time

        # Conversión del escalar a vector,
        # considerando la velocidad (dirección) de la bola.
        scalar_2_vector = half_a_t_squared * self.velocity.normalized()

        # La posición predicha es la actual
        # más la suma de los dos términos anteriores.
        return self.pos + ut + scalar_2_vector

    def move(self):
        # handle walls first:
        self.old_pos = self.pos
        self.reset_on_wall_collision()
        # Friction of field on wall: if ball goes fast enough, everything is updated
        if self.velocity.get_length_sqrd() > Global.FRICTION ** 2:
            self.velocity += (self.velocity.normalized() * Global.FRICTION)
            self.pos += Point(x=self.velocity.x, y=self.velocity.y)
            self.heading = self.velocity.normalized()
