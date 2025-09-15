import unittest
import bike_app

class TestBikeTurnOnFunction(unittest.TestCase):
    def test_that_the_function_exist(self):
        bike_app.turn_on_power()
    def test_that_the_bike_can_be_turned_on(self):
        result = bike_app.turn_on_power()
        self.assertEqual(result, True)
    def test_that_the_bike_can_work_when_turned_on(self):
        result = bike_app.turn_on_power()
        bike_app.set_speed(3)
        self.assertEqual(result, True)

class TestBikeTurnOffFunction(unittest.TestCase):
    def test_that_the_function_exist(self):
        bike_app.turn_off_power()
    def test_that_the_bike_can_be_turned_off(self):
        result = bike_app.turn_off_power()
        self.assertEqual(result, False)
    def test_that_the_bike_cant_work_when_turned_off(self):
        result = bike_app.turn_off_power()
        bike_app.set_speed(2)
        self.assertEqual(result, 0)

class TestBikeSpeedFunction(unittest.TestCase):
    def test_that_the_function_exist(self):
        bike_app.set_speed(23)
    def test_that_the_function_returns_correct_value(self):
        result = bike_app.set_speed(23)
        self.assertEqual(result, 23)

class TestBikeAccelerationFunction(unittest.TestCase):
    def test_that_the_function_exist(self):
        bike_app.accelerate()
    def test_that_the_bike_can_be_accelerated(self):
        bike_app.turn_on_power()
        bike_app.set_speed(23)
        result = bike_app.accelerate()
        self.assertEqual(result, 25)

class TestBikeDecelerationFunction(unittest.TestCase):
    def test_that_the_function_exist(self):
        bike_app.turn_on_power()
        bike_app.set_speed(42)
        result = bike_app.decelerate()
        self.assertEqual(result, 38)
