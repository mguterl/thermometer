# Thermometer

A python interface for interacting with a temperature sensor connected to an Arduino.

It assumes that communication with the Arduino is done via the serial port and a specific command structure is being used.

## Usage

```python
import thermometer

sensor = thermometer.sensor('/dev/ttyACM0')
sensor.current_temperature # => 70°F (21.11°C)
```

## Installation

## Dependencies

* pySerial

## Protocol

