# Thermometer Application

This project is a simple thermometer application that allows users to monitor temperature readings and set thresholds for notifications. The application can handle temperatures in both Celsius and Fahrenheit. There are optional parameters for the thresholds to allow for directional notification (such as only as the temperature is dropping) and also a tolerance (so that slight variations don't re-trigger threshold notifications).

## Features

- Convert between Celsius and Fahrenheit.
- Set multiple temperature thresholds for notifications.
- Monitor temperature readings and check against defined thresholds parameters.

## Components

The application consists of the following main classes:

1. **Temperature**: Represents temperature in Celsius and Fahrenheit.
2. **Threshold**: Represents a temperature threshold with a specified direction (above or below) and tolerance.
3. **Thermometer**: Manages temperature readings and checks against thresholds.

## Installation

To run this project, ensure you have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository or download the source files.
2. Navigate to the project directory.
3. (Optional) Create a virtual environment
4. Install any required packages (if applicable - I did use pytest for unit testing within the project).

## Usage

To run the thermometer application, execute the `main.py` file:
    ```bash
    python src/main.py
    ```
To run the 7 unit tests created within the test_thermometer.py file, execute:
    ```bash
    export PYTHONPATH=src && python -m unittest discover -s tests
    ```

### Example

The following example demonstrates how to use the thermometer application:

1. Define thresholds: for example, here is freezing point (0°C) from above and with 0.5 tolerance.
    ```bash
    freezing_threshold = Threshold(
        name="Freezing Point",
        value=0.0,
        unit="C",
        direction="above",
        tolerance=0.5
    )
    thermometer.add_threshold(freezing_threshold)
    ```
- Included with the thresholds is the option to define a tolerance (for example: ignore temp variations of 0.5 or less, to reduce notifications)
- Also included in the threshold is an optional field for a direction, meaning was the temperative approaching the threshold from above or below.
2. Simulate temperature readings in Celsius or Fahrenheit.
    ```bash
    # Simulate temperature readings
    temperature_readings = [
        (1.0, 'C'), 
        (0.0, 'C'), 
        (-2.0, 'C'), 
        (0.0, 'C'), 
        (0.2, 'C'), 
        (0.0, 'C')
    ]
    ```
3. The application will notify you when thresholds are reached, according to your defined parameters.
    ```bash
    results = []
    print("Starting temperature readings... " + str(temperature_readings))

    # Process each temperature reading
    for index, (value, unit) in enumerate(temperature_readings):
        result = thermometer.read_temperature(value, unit, index)
        results.extend(result) if result else None

    print(str(results))
    ```
Here is what the terminal output will be:
```bash
Starting temperature readings... [(1.0, 'C'), (0.0, 'C'), (-2.0, 'C'), (0.0, 'C'), (0.2, 'C'), (0.0, 'C')]
["Threshold 'Freezing Point' (0.00°C with a tolerance of 0.5) reached from above at index: 1."]
```


## Classes Overview

### Temperature Class

- **Attributes**: 
  - `celsius`: The temperature in Celsius.
- **Methods**:
  - `fahrenheit`: Converts Celsius to Fahrenheit.
  - `from_fahrenheit`: Creates a Temperature instance from Fahrenheit.

### Threshold Class

- **Attributes**:
  - `name`: The name of the threshold.
  - `value`: The threshold value.
  - `unit`: The unit of measurement ('C' or 'F').
  - `direction`: Indicates if the threshold is 'above' or 'below'.
  - `tolerance`: The allowable deviation from the threshold.

### Thermometer Class

- **Attributes**:
  - `current_temperature`: The current temperature reading.
  - `thresholds`: A list of defined thresholds.
  - `last_notifications`: Tracks the last notification sent for each threshold.
- **Methods**:
  - `add_threshold(threshold: Threshold)`: Adds a new threshold for notifications.
  - `read_temperature(new_temperature: float, unit: str, index: int)`: Updates the current temperature and checks against thresholds.
    - **Parameters**:
      - `new_temperature`: The new temperature value.
      - `unit`: The unit of the new temperature ('C' or 'F').
      - `index`: The index of the temperature reading in the initial array of readings.
  - `check_thresholds(new_temperature, index) -> list`: Checks all thresholds against the current temperature and returns results.
  - `should_notify(threshold: Threshold) -> bool`: Determines if a notification should be sent based on the threshold.
