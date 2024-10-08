# test_temp_converter.py

import unittest
from temp_converter import convert_temperature

class TestTemperatureConversions(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        # 0°C should be 32°F
        self.assertAlmostEqual(convert_temperature(0, "Celsius", "Fahrenheit"), 32.0)
        # 100°C should be 212°F
        self.assertAlmostEqual(convert_temperature(100, "Celsius", "Fahrenheit"), 212.0)

    def test_fahrenheit_to_celsius(self):
        # 32°F should be 0°C
        self.assertAlmostEqual(convert_temperature(32, "Fahrenheit", "Celsius"), 0.0)
        # 212°F should be 100°C
        self.assertAlmostEqual(convert_temperature(212, "Fahrenheit", "Celsius"), 100.0)

    def test_celsius_to_kelvin(self):
        # 0°C should be 273.15 K
        self.assertAlmostEqual(convert_temperature(0, "Celsius", "Kelvin"), 273.15)
        # -273.15°C should be 0 K (absolute zero)
        self.assertAlmostEqual(convert_temperature(-273.15, "Celsius", "Kelvin"), 0.0)

    def test_kelvin_to_celsius(self):
        # 273.15 K should be 0°C
        self.assertAlmostEqual(convert_temperature(273.15, "Kelvin", "Celsius"), 0.0)
        # 0 K should be -273.15°C (absolute zero)
        self.assertAlmostEqual(convert_temperature(0, "Kelvin", "Celsius"), -273.15)

    def test_fahrenheit_to_kelvin(self):
        # 32°F should be 273.15 K
        self.assertAlmostEqual(convert_temperature(32, "Fahrenheit", "Kelvin"), 273.15)
        # -459.67°F should be 0 K (absolute zero)
        self.assertAlmostEqual(convert_temperature(-459.67, "Fahrenheit", "Kelvin"), 0.0)

    def test_kelvin_to_fahrenheit(self):
        # 0 K should be -459.67°F (absolute zero)
        self.assertAlmostEqual(convert_temperature(0, "Kelvin", "Fahrenheit"), -459.67)
        # 273.15 K should be 32°F
        self.assertAlmostEqual(convert_temperature(273.15, "Kelvin", "Fahrenheit"), 32.0)

    def test_invalid_conversion(self):
        # Test an invalid conversion
        with self.assertRaises(ValueError):
            convert_temperature(100, "Celsius", "UnknownUnit")

if __name__ == "__main__":
    unittest.main()
