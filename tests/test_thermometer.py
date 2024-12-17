import unittest
from thermometer import Thermometer
from threshold import Threshold

class TestThermometer(unittest.TestCase):

    def setUp(self):
        """Set up the Thermometer instance"""
        self.thermometer = Thermometer()

    def test_above_threshold_c_tol_notification(self):
        """Test notifications for meeting the freezing point threshold from above, in C, 
        with a 0.5 tolerance."""

        self.freezing_threshold = Threshold(name="Freezing Point", value=0.0, unit="C", direction="above", tolerance=0.5)
        self.thermometer.add_threshold(self.freezing_threshold)

        readings = [(1.0, 'C'), (0.4, 'C'), (0.0, 'C'), (-0.4, 'C'), (0.0, 'C'), (0.2, 'C'), (0.0, 'C'), (2.0, 'C'), (0.0, 'C')]
        expected_notifications = [
            "Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from above at index: 2.",
            "Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from above at index: 8."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))
    
    def test_below_threshold_f_tol_notification(self):
        """Test notifications for meeting the boiling point threshold from below, in F,
        with a 1.0 tolerance."""

        self.boiling_threshold = Threshold(name="Boiling Point", value=212, unit="F", direction="below", tolerance=1)        
        self.thermometer.add_threshold(self.boiling_threshold)

        readings = [(300, 'F'), (212,'F'), (200.0, 'F'), (212.0, 'F'), (211.0, 'F'), (212.0, 'F'), (180.0, 'F'), (212.0, 'F'), (211.5, 'F')]
        expected_notifications = [
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 1) reached from below at index: 3.",
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 1) reached from below at index: 7."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))

    def test_below_threshold_f_notification(self):
        """Test notifications for meeting the boiling point threshold from below, in F,
        with a no tolerance."""

        self.boiling_threshold = Threshold(name="Boiling Point", value=212, unit="F", direction="below")        
        self.thermometer.add_threshold(self.boiling_threshold)

        readings = [(300, 'F'), (212,'F'), (200.0, 'F'), (212.0, 'F'), (211.0, 'F'), (212.0, 'F'), (180.0, 'F'), (212.0, 'F'), (211.5, 'F')]
        expected_notifications = [
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 0) reached from below at index: 3.",
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 0) reached from below at index: 5.",
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 0) reached from below at index: 7."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))

    def test_threshold_c_tol_notification(self):
        """Test notifications for meeting the freezing point threshold from any direction, in C, 
        with a 0.5 tolerance."""

        self.freezing_threshold = Threshold(name="Freezing Point", value=0.0, unit="C", tolerance=0.5)
        self.thermometer.add_threshold(self.freezing_threshold)

        readings = [(1.0, 'C'), (0.4, 'C'), (0.0, 'C'), (-0.4, 'C'), (0.0, 'C'), (-4.0, 'C'), (0.0, 'C'), (2.0, 'C'), (0.0, 'C')]
        expected_notifications = [
            "Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from any direction at index: 2.",
            "Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from any direction at index: 6.",
            "Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from any direction at index: 8."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))

    def test_f_notification(self):
        """Test notifications for meeting the freezing point threshold from any direction, in F, 
        with a 0 tolerance."""

        self.freezing_threshold = Threshold(name="Freezing Point", value=32, unit="F")
        self.thermometer.add_threshold(self.freezing_threshold)

        readings = [(35.0, 'F'), (32.0, 'F'), (32.5, 'F'), (32, 'F'), (31.5, 'F'), (32, 'F'), (32, 'F')]
        expected_notifications = [
            "Threshold 'Freezing Point' (32.00°F with a tolerance of 0) reached from any direction at index: 1.",
            "Threshold 'Freezing Point' (32.00°F with a tolerance of 0) reached from any direction at index: 3.",
            "Threshold 'Freezing Point' (32.00°F with a tolerance of 0) reached from any direction at index: 5."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))

    def test_above_random_threshold_mixed_tol_notification(self):
        """Test notifications for meeting a random threshold from above, in C or F, 
        with a 5 tolerance."""

        self.random_threshold = Threshold(name="Random Point", value=86.0, unit="F", direction="above", tolerance=5)
        self.thermometer.add_threshold(self.random_threshold)

        readings = [(30, 'C'), (87, 'F'), (86, 'F'), (40, 'C'), (86, 'F'), (28, 'C'), (30, 'C'), (95, 'F'), (86, 'F')]
        expected_notifications = [
            "Threshold 'Random Point' (86.00°F with a tolerance of 5) reached from above at index: 0.",
            "Threshold 'Random Point' (86.00°F with a tolerance of 5) reached from above at index: 4.",
            "Threshold 'Random Point' (86.00°F with a tolerance of 5) reached from above at index: 8."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))

    def test_any_many_thresholds_mixed_notification(self):
        """Test notifications for meeting multiple thresholds from many directions, in C or F, 
        with a mixed tolerance."""

        self.freezing_threshold = Threshold(name="Freezing Point", value=0.0, unit="C", direction="above", tolerance=0.5)
        self.thermometer.add_threshold(self.freezing_threshold)
        self.boiling_threshold = Threshold(name="Boiling Point", value=212, unit="F", direction="below", tolerance=2)        
        self.thermometer.add_threshold(self.boiling_threshold)
        self.random_threshold = Threshold(name="Random Point", value=100, unit="F")
        self.thermometer.add_threshold(self.random_threshold)

        readings = [(0.0, 'C'), (0.4, 'C'), (0.0, 'C'), (211, 'F'), (212, 'F'), (211, 'F'), (212, 'F'), (100, 'F'), (212, 'F'), (100, 'F')]
        expected_notifications = [
            "Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from above at index: 0.", 
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 2) reached from below at index: 4.", 
            "Threshold 'Random Point' (100.00°F with a tolerance of 0) reached from any direction at index: 7.", 
            "Threshold 'Boiling Point' (212.00°F with a tolerance of 2) reached from below at index: 8.", 
            "Threshold 'Random Point' (100.00°F with a tolerance of 0) reached from any direction at index: 9."
        ]
        
        notifications = []
        for index, reading in enumerate(readings):
            result = self.thermometer.read_temperature(reading[0], reading[1], index)
            notifications.extend(result) if result else None

        self.assertTrue(any(msg in notifications for msg in expected_notifications))

if __name__ == '__main__':
    unittest.main()
