#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Steering Behaviours.

TODO:

"""

from geometry.vector import Vec2d
from geometry.point import Point

# Deceleration factors.
SLOW = 3
NORMAL = 2
FAST = 1

class SteeringBehaviours:
    """Steering Behaviours."""

    def __init__(self, player, ball):

        self.player = player
        self.ball = ball

        self.target = ball.pos

        # Behaviours dictionary (key: behaviour name, value: is it activated?)
        self.activated = {}
        self.activated['seek'] = False
        self.activated['pursuit'] = False
        self.activated['arrive'] = False
        #
        self.steering_force = self.sum_forces()

    def calculate(self) -> Vec2d:
        """Updates steering force."""
        self.steering_force = self.sum_forces()
        return self.steering_force

    def sum_forces(self) -> Vec2d:

        force = Vec2d(0, 0)
        if self.activated['seek']:
            force += self.seek(self.target)
        if self.activated['pursuit']:
            force += self.pursuit(self.target)
        if self.activated['arrive']:
            force += self.arrive(self.target)
        return force

    def truncate(self, max_force):
        """Truncates steering force."""
        if self.steering_force > max_force:
            self.steering_force = max_force

    def seek(self, target: Point) -> Vec2d:
        """
        Dado un objetivo, este comportamiento devuelve la fuerza
        que orienta al jugador hacia el objetivo y lo mueve.
        :param target: Where am I going to.
        :return: The force vector towards it.
        """

        desired_velocity = (target - self.player.pos).normalized()
        desired_velocity *= self.player.max_speed

        return (desired_velocity - self.player.velocity)

    def arrive(self, target: Point, deceleration=FAST) -> Vec2d:
        """Similar a seek pero llegando con velocidad nula."""

        to_target = Vec2d.origin_to(target - self.player.pos)
        # distance to target
        dist = to_target.get_length()

        if dist > 25:
            # Para ajustar la deceleración...
            decelerationTweaker = 3
            # Cálculo de la velocidad requerida.
            speed = min(dist / (deceleration * decelerationTweaker), self.player.max_speed.get_length())
            # velocity:
            desired_velocity = to_target * speed / dist # Vec2d(to_target * speed / dist)

            ## FIX THIS TYPE :::

            return desired_velocity - self.player.velocity
        else:
            return Vec2d(0, 0)

    def pursuit(self, target) -> Vec2d:
        """Crea una fuerza que mueve al jugador hacia la bola."""

        toBall = self.ball.pos - self.player.pos
        self.direction = toBall.normalized()
        look_ahead_time = 0.0

        if self.ball.velocity.get_length() != 0.0:
            look_ahead_time = toBall.get_length() / self.ball.velocity.get_length()

        # ¿Dónde estará la bola en el futuro?
        target = self.ball.futurePosition(look_ahead_time)

        return self.arrive(target)
