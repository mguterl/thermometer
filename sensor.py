from temperature import Temperature

class Sensor:
  def __init__(self, connection):
    self.connection = connection
  def current_temperature(self):
    return Temperature(self.connection.send("temperature:current"))

