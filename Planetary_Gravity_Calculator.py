"""
You will be given a number M which is the mass of an object in kilograms, on its
own line, for example:
    100

Followed by a number N:
    4

You will then, on separate lines, be given a list of N planets. This will be
given as its name, its radius (in metres), and its average density (in kilograms
per cubic metre), like so:
    Mercury, 2439700, 5427

Print the weight (in Newtons) of the object if it were at the surface of each
planet, like so:

    Mercury: 314.623
"""

from math import pi

gravity = 6.67e-11


class Planet(object):
    """A planet class"""
    def __init__(self, name, radius, density):
        self.name = name
        self.radius = radius  # in meters
        self.density = density  # in kg/m3
        self.volume = ((4 / 3) * pi * (self.radius ^ 3))
        self.planet_mass = self.volume * self.density
        # TODO add in automatic tagging of units.

    def thing(self, mass):
        self.mass = mass  # in kg
        self.weight = gravity * ((self.mass * self.planet_mass) / 1)
        print self.name + ':', self.weight, 'N'
        # TODO add in unit for weight.
