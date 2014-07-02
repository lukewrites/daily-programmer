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
        self.radius = radius
        self.planet_mass = (4 / 3) * pi * (self.radius ** 3) * density

    def thing(self, weight):
        return gravity * (weight * self.planet_mass) / self.radius ** 2


with open('planets.txt', 'r') as f:
    contents = [line.rstrip() for line in f.readlines()]

mass = int(contents[0])

planets = [contents[i].split(',') for i in range(2, len(contents))]

def main():
    for i in range(0, int(len(planets))):
        temp_planet = Planet(planets[i][0], float(planets[i][1]), float(planets[i][2]))
        newts = temp_planet.thing(mass)
        planet = planets[i][0]
        print planet + ": " + str(newts) + " N"


if __name__ == '__main__':
    main()