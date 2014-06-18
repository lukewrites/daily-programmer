"""Tests for Planetary_Gravity_Calculator.py"""
import unittest
from Planetary_Gravity_Calculator import Planet


class testPlanet(unittest.TestCase):

    def setUp(self):
        self.earth = Planet('Earth', 6367445, 5515)
        self.mercury = Planet('Mercury', 2439700, 5427)
        self.mercury.thing = self.mercury.thing(100)

    def test_if_i_can_create_a_planet(self):
        self.assertEqual(self.earth.radius, 6367445)
        self.assertEqual(self.earth.density, 5515)
        self.assertEqual(self.earth.volume, 8.110459869484416e+20)

    def test_if_weight_is_calculated_correctly(self):
        self.assertEqual(self.mercury.thing, 277.4418389317911)


if __name__ == '__main__':
    unittest.main()