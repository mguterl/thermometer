import thermometer

def test_persist_temperature():
  t1 = thermometer.Temperature(72.0)
  database = thermometer.Database('temperature.db')
  store = thermometer.Store(database)
  store.reset()
  store.persist(t1)
  t2 = store.current_temperature()
  assert t1 == t2

def test_current_temperature_returns_most_recent_entry():
  database = thermometer.Database('temperature.db')
  store = thermometer.Store(database)
  store.reset()
  t1 = thermometer.Temperature(72.0)
  t2 = thermometer.Temperature(68.0)
  store.persist(t1)
  store.persist(t2)
  assert t2 == store.current_temperature()

