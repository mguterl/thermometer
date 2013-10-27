import thermometer
from datetime import datetime

class FakeConnection:
  def __init__(self, command_dictionary):
    self.command_dictionary = command_dictionary

  def send(self, command):
    return self.command_dictionary[command]

class FakeClock:
  def __init__(self, value):
    self.value = value

  def now(self):
    return self.value

def test_current_temperature():
  connection = FakeConnection({ "temperature:current": "72.0" })
  clock = FakeClock(datetime.now())
  sensor = thermometer.Sensor(connection, clock)
  temperature = sensor.current_temperature()
  assert thermometer.Temperature(72.0, clock.now()) == temperature

