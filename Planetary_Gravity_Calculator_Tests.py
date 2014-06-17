"""Tests for Planetary_Gravity_Calculator.py"""
import unittest
from Planetary_Gravity_Calculator import Planet
from math import pi


class testPlanet(unittest.TestCase):

    def setUp(self):
        # self.earth = Planet('Earth', 6367445, 5515, 100)
        self.mercury = Planet('Mercury', 2439700, 5427, 100)


    def test_if_i_can_create_a_planet(self):
        self.assertEqual(self.earth.radius, 6367445)
        self.assertEqual(self.earth.density, 5515)
        self.assertEqual(self.earth.volume, 8.110459869484416e+20)

    # def test_if_planet_calculates_planet_mass(self):
    #     self.assertEqual(self.earth.planet_mass, (((4 / 3) * pi *
    #                      (self.earth.radius ** 3)) * self.earth.density))

    def test_if_weight_is_calculated_correctly(self):
        self.assertEqual(self.mercury.thing_weight, 277.4418389317911)

    # def test_if_planet_calculates_thing_weight(self):
    #     self.assertEqual(self.earth.light_thing, )

if __name__ == '__main__':
    unittest.main()