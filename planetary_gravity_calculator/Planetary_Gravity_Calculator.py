"""
http://www.reddit.com/r/dailyprogrammer/comments/284mep/6142014_challenge_166b_easy_planetary_gravity/
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
        self.volume = 4 / 3 * pi * self.radius**3
        self.planet_mass = self.volume * self.density

    def thing(self, weight):
        self.weight = weight
        return gravity * (weight * self.planet_mass) / self.radius**2

with open('planets.txt', 'r') as f:
    contents = [line.rstrip() for line in f.readlines()]

planets = [contents[i].split() for i in range(2, len(contents) + 1)]
planets = [planets[i].replace(',', '') for i in range(0, len(planets))]
planets = [planets[i].split() for i in range(0, len(planets))]

for i in range(int(contents(1)):
    print "%s: %r Newtons" % planets[i][0], 
