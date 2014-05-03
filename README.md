# Thermometer

[![Build Status](https://travis-ci.org/mguterl/thermometer.png?branch=master)](https://travis-ci.org/mguterl/thermometer)

A python interface for interacting with a temperature sensor connected to an Arduino.

It assumes that communication with the Arduino is done via the serial port and a specific command structure is being used.

* API wrapper for reading the current temperature from the sensor
* Storage API for capturing temperatures
* Fake implementations in order to faciliate easier testing
* Command line interface for capturing temperatures
* HTTP / JSON API for accessing data from the storage API
* Basic charts built with highcharts for visualizing data from the HTTP / JSON
  API
* Code for the Arduino that responds to commands sent via the serialport for
  reading the temperature sensor

## Usage

```python
import thermometer

sensor = thermometer.sensor('/dev/ttyACM0')
sensor.current_temperature # => 70°F (21.11°C)
```

## Installation

## Protocol

Currently the Arduino only responds to one command `temperature:current`. In
the future more commands may be implemented following this pattern.
