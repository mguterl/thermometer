import unittest
import thermometer
from datetime import datetime

class TestPersistence(unittest.TestCase):
  def test_persist_temperature(self):
    t1 = thermometer.Temperature(72.0, datetime.now())
    db = thermometer.Database('thermometer.db')
    store = thermometer.Store(db)
    store.reset()
    store.persist(t1)
    t2 = store.current_temperature()
    print t1.datetime
    print t2.datetime
    assert t1 == t2

  def test_current_temperature_returns_most_recent_entry(self):
    db = thermometer.Database('thermometer.db')
    store = thermometer.Store(db)
    store.reset()
    t1 = thermometer.Temperature(72.0, datetime.now())
    t2 = thermometer.Temperature(68.0, datetime.now())
    store.persist(t1)
    store.persist(t2)
    assert t2 == store.current_temperature()

  def test_does_not_error_with_no_previous_entries(self):
    db = thermometer.Database('thermometer.db')
    store = thermometer.Store(db)
    store.reset()

    try:
      temperature = store.current_temperature()
    except:
      self.fail("store#current_temperature() should not return an error when no values are present")

    assert None == temperature
