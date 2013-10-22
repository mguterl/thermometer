import serial
from database import Database
from connection import Connection
from temperature import Temperature
from store import Store

def sensor(serial_port):
  serial_port = serial.Serial(serial_port, 9600)
  serial_port.readline()
  connection = Connection(serial_port)
  return Sensor(connection)

class Sensor:
  def __init__(self, connection):
    self.connection = connection
  def current_temperature(self):
    return Temperature(self.connection.send("temperature:current"))


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
