import thermometer

class FakeConnection:
  def __init__(self, command_dictionary):
    self.command_dictionary = command_dictionary

  def send(self, command):
    return self.command_dictionary[command]


def test_current_temperature():
  connection = FakeConnection({ "temperature:current": "72.0" })
  sensor = thermometer.Sensor(connection)
  temperature = sensor.current_temperature()
  assert thermometer.Temperature(72.0) == temperature

