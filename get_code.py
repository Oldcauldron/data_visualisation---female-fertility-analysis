
from pygal.maps.world import COUNTRIES
import json
import unittest
# pip install pygal_maps_world


def get_code(country):
    for a, b in COUNTRIES.items():
        if b == country:
            return a
    with open('archives/add_correct_cods.json') as adc:
        add = json.load(adc)
        if country in add:
            return add[country]


# class NameTestCase(unittest.TestCase):
#     def testing_country_1(self):
#         code = get_code('Russian Federation')
#         self.assertEqual(code, 'ru')

#     def testing_country_2(self):
#         code = get_code('Antigua and Barbuda')
#         self.assertEqual(code, 'ag')


# unittest.main()


