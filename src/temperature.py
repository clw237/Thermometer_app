class Temperature:
    """Class to represent temperature in Celsius and Fahrenheit."""

    def __init__(self, celsius):
        """
        Initialize a Temperature instance with a Celsius value.

        Args:
            celsius (float): The temperature in degrees Celsius.
        """
        self.celsius = celsius

    @property
    def fahrenheit(self):
        """Convert Celsius to Fahrenheit.

        Returns:
            float: The temperature in degrees Fahrenheit.
        """
        return (self.celsius * 9 / 5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Create a Temperature instance from a Fahrenheit value.

        Args:
            fahrenheit (float): The temperature in degrees Fahrenheit.

        Returns:
            Temperature: A Temperature instance representing the equivalent Celsius value.
        """
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @classmethod
    def from_celsius(cls, celsius):
        """Create a Temperature instance from a Celsius value.

        Args:
            celsius (float): The temperature in degrees Celsius.

        Returns:
            Temperature: A Temperature instance initialized with the given Celsius value.
        """
        return cls(celsius)
