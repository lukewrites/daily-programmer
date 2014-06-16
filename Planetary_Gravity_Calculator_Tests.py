"""Tests for Planetary_Gravity_Calculator.py"""
import unittest
from Planetary_Gravity_Calculator import Planet
from math import pi


class testPlanet(unittest.TestCase):

    def setUp(self):
        self.earth = Planet('Earth', 6367445, 5515)
        self.earth.light_thing = self.earth.thing(25)
        self.mercury = Planet('Mercury', 2439700, 5427)
        self.mercury.light_thing = self.mercury.thing(100)


    def test_if_i_can_create_a_planet(self):
        self.assertEqual(self.earth.radius, 6367445)
        self.assertEqual(self.earth.density, 5515)
        self.assertAlmostEqual(self.earth.volume, 20003921.5757297)

    def test_if_planet_calculates_planet_mass(self):
        self.assertEqual(self.earth.planet_mass, (((4 / 3) * pi *
                         (self.earth.radius ^ 3)) / self.earth.density))

    def test_if_weight_is_calculated_correctly(self):
        self.assertAlmostEqual(self.mercury.light_thing.weight, 314.623)

    # def test_if_planet_calculates_thing_weight(self):
    #     self.assertEqual(self.earth.light_thing, )

if __name__ == '__main__':
    unittest.main()