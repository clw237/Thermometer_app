class Threshold:
    """Class to represent a temperature threshold."""

    def __init__(self, name, value, unit, direction="any direction", tolerance=0):
        """
        Initialize a Threshold instance.

        Args:
            name (str): The name of the threshold.
            value (float): The threshold value.
            unit (str): The unit of the threshold ('C' for Celsius or 'F' for Fahrenheit).
            direction (str): The direction of the threshold ('above', 'below', or 'any direction').
            tolerance (float): The tolerance level for the threshold.
        """
        self.name = name
        self.value = value
        self.unit = unit.upper()  # Convert unit to uppercase for consistency
        self.direction = direction.lower()  # Convert direction to lowercase for consistency
        self.tolerance = tolerance

    def convert_to_celsius(self):
        """Convert threshold value to Celsius if it's in Fahrenheit.

        Returns:
            float: The threshold value in Celsius.
        """
        if self.unit == 'F':
            return (self.value - 32) * 5 / 9
        return self.value  # Already in Celsius
