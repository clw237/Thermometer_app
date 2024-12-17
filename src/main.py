from thermometer import Thermometer
from threshold import Threshold

def main():
    """Main function to run the Thermometer application."""
    # Initialize the Thermometer instance
    thermometer = Thermometer()

    # Define thresholds in Celsius or Fahrenheit for freezing and
    # random points. Vary the tolerance and direction.
    freezing_threshold = Threshold(
        name="Freezing Point",
        value=0.0,
        unit="C",
        direction="above",
        tolerance=0.5
    )
    thermometer.add_threshold(freezing_threshold)

    random_threshold = Threshold(
        name="Random Point",
        value=100,
        unit="F"
    )
    thermometer.add_threshold(random_threshold)

    # Simulate temperature readings
    temperature_readings = [(1.0, 'C'), (0.0, 'C'), (-2.0, 'C'), (0.0, 'C'), (0.2, 'C'), (0.0, 'C')]

    results = []
    print("Starting temperature readings... " + str(temperature_readings))

    # Process each temperature reading
    for index, (value, unit) in enumerate(temperature_readings):
        result = thermometer.read_temperature(value, unit, index)
        results.extend(result) if result else None

    print(str(results))

if __name__ == "__main__":
    main()
