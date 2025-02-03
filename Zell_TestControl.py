from Zell_Control import Control
import time
import unittest

class TestControl(unittest.TestCase):
    def test_push_button(self):
        self.control = Control()
        # Simulate pushing the button
        self.control.car_street_light.set_status('green')
        self.assertEqual(self.control.car_street_light.get_status(), 'green')
        self.control.pedestrian_street_light.set_status('red')
        self.assertEqual(self.control.pedestrian_street_light.get_status(), 'red')

        # Change car street light to yellow, then red
        self.control.car_street_light.set_status('yellow')
        self.assertEqual(self.control.car_street_light.get_status(), 'yellow')
        self.control.car_street_light.set_status('red')
        self.assertEqual(self.control.car_street_light.get_status(), 'red')

        # Change pedestrian street light to green
        self.control.pedestrian_street_light.set_status('green')
        self.assertEqual(self.control.pedestrian_street_light.get_status(), 'green')
        self.control.pedestrian_street_light.set_status('red')
        self.assertEqual(self.control.pedestrian_street_light.get_status(), 'red')

        # Change car street light to green
        self.control.car_street_light.set_status('yellow')
        self.assertEqual(self.control.car_street_light.get_status(), 'yellow')
        self.control.car_street_light.set_status('green')
        self.assertEqual(self.control.car_street_light.get_status(), 'green')


if __name__ == '__main__':
    unittest.main()
