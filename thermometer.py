# -*- coding: utf-8 -*-

import serial
import sqlite3

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

class Database:
  def __init__(self, database_name):
    self.connection = sqlite3.connect(database_name)
    self.connection.row_factory = sqlite3.Row

  def create_table(self, sql):
    self.execute_and_commit(sql)

  def drop_table(self, table_name):
    self.execute_and_commit("DROP TABLE " + table_name)

  def insert(self, sql, variables):
    self.execute_and_commit(sql, variables)

  def select_one(self, sql):
    cursor = self.__execute(sql)
    return cursor.fetchone()

  def execute_and_commit(self, *args):
    self.__execute(*args)
    self.connection.commit()

  def __execute(self, *args):
    cursor = self.connection.cursor()
    cursor.execute(*args)
    return cursor

class Store:
  def __init__(self, database):
    self.database = database

  def persist(self, temperature):
    self.database.insert("INSERT INTO temperatures (farenheit) VALUES (?)", [str(temperature.farenheit)])

  def current_temperature(self):
    result = self.database.select_one("SELECT temperatures.farenheit FROM temperatures ORDER BY id DESC LIMIT 1")
    return Temperature(result["farenheit"])

  def reset(self):
    self.database.drop_table("temperatures")
    self.database.execute_and_commit("CREATE TABLE IF NOT EXISTS temperatures (id INTEGER PRIMARY KEY, farenheit TEXT)")

