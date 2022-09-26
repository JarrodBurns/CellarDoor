
import sys
from pathlib import Path

route = str(Path().cwd().parent.joinpath("modules"))
sys.path.append(route)

import unittest
import clock


class TestClock(unittest.TestCase):

    def test_to_seconds_value_is_singal(self):
        """
        Values of one should NOT have an 's' applied to the display.
        """
        self.assertEqual(clock.from_seconds(1), "1 second")

    def test_from_seconds_value_is_plural(self):
        """
        Verify 's' is properly appended when dealing with values which
        are not equal to 1
        """
        self.assertEqual(clock.from_seconds(300), "5 minutes")

    def test_from_seconds_zero_or_less(self):
        """
        Values < 0 should raise an error, no timetravelers
        """
        self.assertRaises(ValueError, clock.from_seconds, -1)

    def test_from_seconds_and_added(self):
        """
        Check if "and" is applied when two or more units are displayed
        """
        self.assertEqual(clock.from_seconds(61), "1 minute and 1 second")

    def test_from_seconds_has_commas(self):
        """
        Commas should appear when three or more units are displayed
        """
        self.assertEqual(
            clock.from_seconds(3_661), "1 hour, 1 minute, and 1 second"
        )

    def test_from_seconds_all_units(self):
        """
        Proper format and display of four unit places.
        """
        self.assertEqual(
            clock.from_seconds(90_061), "1 day, 1 hour, 1 minute, and 1 second"
        )

    def test_to_seconds_all_units(self):
        """
        Veryify all values can be correctly parsed
        """
        self.assertEqual(
            clock.to_seconds("1 day, 1 hour, 1 minute, and 1 second"), 90061
        )

    def test_to_seconds_one_unit(self):
        """
        Verify small values are correctly parsed
        """
        self.assertEqual(clock.to_seconds("1 second"), 1)


unittest.main()
