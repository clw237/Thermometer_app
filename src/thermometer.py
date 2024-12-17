from temperature import Temperature
from threshold import Threshold

class Thermometer:
    """Class to manage temperature readings and thresholds."""

    def __init__(self):
        """Initialize the Thermometer with default values."""
        self.current_temperature = Temperature(0.0)
        self.thresholds = []
        self.last_notifications = {}
        self.previous_temperature = None  # Track previous temperature for direction checks

    def add_threshold(self, threshold: Threshold):
        """Add a new threshold for notifications.

        Args:
            threshold (Threshold): The threshold to be added.
        """
        self.thresholds.append(threshold)
        self.last_notifications[threshold.name] = None  # Initialize last notification tracking

    def read_temperature(self, new_temperature: float, unit: str, index: int):
        """Update the current temperature and check thresholds.

        Args:
            new_temperature (float): The new temperature value.
            unit (str): The unit of the new temperature ('C' or 'F').
            index (int): The index of the temperature reading.

        Returns:
            list: Notifications triggered by the current temperature reading.
        """
        if unit == 'F':
            self.current_temperature = Temperature.from_fahrenheit(new_temperature)
        else:
            self.current_temperature = Temperature.from_celsius(new_temperature)

        # Check thresholds and return results
        results = self.check_thresholds(new_temperature, index)

        # Update previous temperature
        self.previous_temperature = self.current_temperature.celsius
        
        return results

    def check_thresholds(self, new_temperature: float, index: int) -> list:
        """Check all thresholds against the current temperature and return results.

        Args:
            new_temperature (float): The current temperature reading.
            index (int): The index of the current reading.

        Returns:
            list: A list of notification messages for thresholds that have been reached.
        """
        results = []
        
        for threshold in self.thresholds:
            if self.should_notify(threshold):
                # Constructing the notification message
                notification_message = (
                    f"Threshold '{threshold.name}' "
                    f"({threshold.value:.2f}\u00B0{threshold.unit} "
                    f"with a tolerance of {threshold.tolerance}) "
                    f"reached from {threshold.direction} at index: {index}."
                )
                results.append(notification_message)

        return results

    def should_notify(self, threshold: Threshold) -> bool:
        """Determine if a notification should be sent based on the threshold.

        Args:
            threshold (Threshold): The threshold to check against.

        Returns:
            bool: True if a notification should be sent, False otherwise.
        """
        # Convert threshold to Celsius for comparison
        threshold_value_celsius = threshold.convert_to_celsius()

        # If previous temperature is None, we cannot determine directionality
        if self.previous_temperature is None:
            if self.current_temperature.celsius == threshold_value_celsius:
                # Update last notification to allow tolerance to supress redundant notifications
                self.last_notifications[threshold.name] = self.current_temperature.celsius
                return True  # Always notify if first reading is a match
            return False
        
        condition_met = False

        # Check direction-based conditions
        if threshold.direction == 'above':
            condition_met = (self.previous_temperature > threshold_value_celsius and 
                             self.current_temperature.celsius <= threshold_value_celsius)
        elif threshold.direction == 'below':
            condition_met = (self.previous_temperature < threshold_value_celsius and 
                             self.current_temperature.celsius >= threshold_value_celsius)
        elif threshold.direction == "any direction":
            condition_met = self.current_temperature.celsius == threshold_value_celsius
    
        # Check for tolerance against the last reading
        if condition_met:
            # Check if this is the first time the threshold is reached
            is_first_notification = self.last_notifications[threshold.name] is None

            # Always update last notification
            self.last_notifications[threshold.name] = self.current_temperature.celsius
            
            # If it's the first notification, return True immediately
            if is_first_notification:
                return True

            # Check if current reading is within tolerance of last reading
            if abs(self.current_temperature.celsius - self.previous_temperature) <= threshold.tolerance:
                return False  # Suppress notification

            return True  # Return True for subsequent notifications outside tolerance

