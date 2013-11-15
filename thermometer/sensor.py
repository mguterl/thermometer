from thermometer import Temperature
from datetime import datetime

class Sensor:
  def __init__(self, connection, clock = datetime):
    self.connection = connection
    self.clock = clock

  def current_temperature(self):
    return Temperature(self.connection.send("temperature:current"),
                       self.clock.now())

