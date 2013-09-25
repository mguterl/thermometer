# -*- coding: utf-8 -*-

import serial

def sensor(serial_port):
  serial_port = serial.Serial(serial_port, 9600)
  serial_port.readline()
  connection = Connection(serial_port)
  return Sensor(connection)

class Connection:
  def __init__(self, serial_port):
    self.serial_port = serial_port
  def send(self, command):
    self.write(command)
    return self.read()
  def write(self, command):
    self.serial_port.write("{command}\n".format(command=command))
  def read(self):
    output = self.serial_port.readline()
    return self.parse(output)
  def parse(self, value):
    return value.rstrip().split(':')[-1]

class Sensor:
  def __init__(self, connection):
    self.connection = connection
  def current_temperature(self):
    return Temperature(self.connection.send("temperature:current"))

class Temperature:
  def __init__(self, farenheit):
    self.farenheit = float(farenheit)
    self.celcius = ((self.farenheit - 32) * 5) / 9
  def __repr__(self):
    return "{farenheit}°F ({celcius}°C)".format(farenheit=self.farenheit, celcius=self.celcius)
  def __eq__(self, other):
    return self.__dict__ == other.__dict__

