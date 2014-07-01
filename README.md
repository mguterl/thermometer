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

## API

```json
{
  current_temperature: 71.0,
  high_temperature: 80.0,
  low_temperature: 68.5,
  average_temperature: 73.0,
}

{
  start_time: '',
  end_time: '',
  average_temperature: 73.0,
  temperatures: [
    {
      time: '',
      temperature: 71.0
    }
  ]
}

{
  temperatures: [
    {
      date: '',
      average_temperature: 72.0
    },
    {
      date: '',
      average_temperature: 70.0
    }
  ]
}
```
