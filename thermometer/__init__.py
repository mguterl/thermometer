# -*- coding: utf-8 -*-

import serial
from database import Database

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
    self.celcius = round(((self.farenheit - 32) * 5) / 9, 2)
  def __repr__(self):
    return "{farenheit}°F ({celcius}°C)".format(farenheit=self.farenheit, celcius=self.celcius)
  def __eq__(self, other):
    return self.__dict__ == other.__dict__

class Store:
  def __init__(self, database):
    self.database = database

  def persist(self, temperature):
    self.database.insert("INSERT INTO temperatures (farenheit) VALUES (?)", [str(temperature.farenheit)])

  def current_temperature(self):
    result = self.database.select_one("SELECT temperatures.farenheit FROM temperatures ORDER BY id DESC LIMIT 1")
    return Temperature(result["farenheit"])

  def setup(self):
    self.database.execute_and_commit("CREATE TABLE IF NOT EXISTS temperatures (id INTEGER PRIMARY KEY, farenheit TEXT)")

  def reset(self):
    self.database.drop_table("temperatures")
    self.setup()

import database

class CLI:
  def __init__(self):
    db = database.Database('thermometer.db')
    self.store = Store(db)

  def record(self):
    temperature_sensor = sensor("/dev/ttyACM0")
    current = temperature_sensor.current_temperature()
    self.store.persist(current)
    print current

  def display(self):
    print self.store.current_temperature()

  def run(self, argv):
    if len(argv) < 2:
      print "usage"
      exit()

    self.execute(argv[1])

  def execute(self, command):
    getattr(self, command, self.unknown_command)()

  def unknown_command(self):
    print "unknown command"
