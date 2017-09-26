#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dynamics of a Soccer Team.

TODO:

"""

import random
from rendering.examples.dynamics.entity import Container
from rendering.base import Color

from rendering.examples.soccer.dynamics.soccer_player import SoccerPlayer

class SoccerTeam(Container):
    "Soccer Team."

    def __init__(self, name: str, colour: Color, num_players: int, soccer_field):
        super().__init__()
        self.name = name
        self.colour = colour
        self.players = []
        self.soccer_field = soccer_field

        random.seed()
        populated_regions = []

        for i in range(0, num_players):
            assigned_region = False
            # we don't 2 players on same region:
            while not assigned_region:
                if name == 'red':
                    region = random.randint(0, 11)
                elif name == 'blue':
                    region = random.randint(16, 27)
                if not region in populated_regions:
                    assigned_region = True
            populated_regions.append(region)

            # Player's center position is the center of the rectangle:
            pos = soccer_field.regions[region].rect.center
            self.players.append(SoccerPlayer(name, colour, i, pos, soccer_field))

    def move_players(self):
        """Calls all players to move."""

        for player in self.players:
            player.move()

    def update_states(self):
        self.move_players()
