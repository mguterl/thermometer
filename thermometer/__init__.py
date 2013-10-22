import serial
from database import Database
from connection import Connection
from temperature import Temperature
from store import Store
from sensor import Sensor
from cli import CLI
from app import App

def sensor(serial_port):
  serial_port = serial.Serial(serial_port, 9600)
  serial_port.readline()
  connection = Connection(serial_port)
  return Sensor(connection)


