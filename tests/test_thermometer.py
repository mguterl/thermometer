from thermometer import thermometer

class FakeConnection:
  def __init__(self, command_dictionary):
    self.command_dictionary = command_dictionary

  def send(self, command):
    return self.command_dictionary[command]

class FakeSerialPort:
  NO_RESPONSE = ""

  def __init__(self):
    self.__reset__

  def write(self, value):
    if value == "temperature:current\n":
      self.next_response = "temperature:72.0"

  def readline(self):
    next_response = self.next_response
    self.__reset__
    return next_response

  def __reset__(self):
    self.next_response = FakeSerialPort.NO_RESPONSE

def test_current_temperature():
  connection = FakeConnection({ "temperature:current": "72.0" })
  sensor = thermometer.Sensor(connection)
  temperature = sensor.current_temperature()
  assert thermometer.Temperature(72.0) == temperature

def test_connection():
  fake_serial_port = FakeSerialPort()
  connection = thermometer.Connection(fake_serial_port)
  response = connection.send("temperature:current")
  assert "72.0" == response

