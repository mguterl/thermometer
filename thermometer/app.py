import thermometer

class App:
  def __init__(self):
    self.db = thermometer.Database('thermometer.db')
    self.store = thermometer.Store(self.db)
    self.sensor = thermometer.sensor('/dev/ttyACM0')

  def record(self):
    current_temperature = self.current_temperature()
    self.store.persist(current_temperature)
    return current_temperature

  def read(self):
    return self.store.current_temperature()

  def current_temperature(self):
    return self.sensor.current_temperature()
