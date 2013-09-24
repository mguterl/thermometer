import unittest

from sensor import Sensor
from temperature import Temperature
from connection import Connection

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

class ThermometerTest(unittest.TestCase):

  def test_temperature_equality(self):
    t1 = Temperature(70.0)
    t2 = Temperature(70.0)
    self.assertEqual(t1, t2)

  def test_temperature_conversion_to_celcius(self):
    temperature = Temperature(68.0)
    celcius = 20.0
    self.assertEqual(celcius, temperature.celcius)

  def test_temperature_conversion_from_string(self):
    temperature = Temperature("68.0")
    self.assertEqual(68.0, temperature.farenheit)

  def test_current_temperature(self):
    connection = FakeConnection({ "temperature:current": "72.0" })
    sensor = Sensor(connection)
    temperature = sensor.current_temperature()
    self.assertEqual(Temperature(72.0), temperature)

  def test_connection(self):
    fake_serial_port = FakeSerialPort()
    connection = Connection(fake_serial_port)
    response = connection.send("temperature:current")
    self.assertEqual("72.0", response)

if __name__ == '__main__':
  unittest.main()
