# Thermometer

A python interface for interacting with a temperature sensor connected to an Arduino.

It assumes that communication with the Arduino is done via the serial port and a specific command structure is being used.

[![Build Status](https://travis-ci.org/mguterl/thermometer.png?branch=master)](https://travis-ci.org/mguterl/thermometer)

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

