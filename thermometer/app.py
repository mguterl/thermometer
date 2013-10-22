import thermometer

class App:
  @classmethod
  def default(cls):
    database = thermometer.Database('thermometer.db')
    store = thermometer.Store(database)
    sensor = thermometer.sensor('/dev/ttyACM0')

    return cls(store, sensor)

  def __init__(self, store, sensor):
    self.store  = store
    self.sensor = sensor

  def record(self):
    current_temperature = self.current_temperature()
    self.store.persist(current_temperature)
    return current_temperature

  def read(self):
    return self.store.current_temperature()

  def current_temperature(self):
    return self.sensor.current_temperature()
