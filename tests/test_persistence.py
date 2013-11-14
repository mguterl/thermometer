import unittest
import thermometer
from datetime import datetime

class TestPersistence(unittest.TestCase):
  def setUp(self):
    db = thermometer.Database('thermometer.db')
    self.store = thermometer.Store(db)
    self.store.reset()

  def test_persist_temperature(self):
    t1 = thermometer.Temperature(72.0, datetime.now())
    self.store.persist(t1)
    t2 = self.store.current_temperature()
    print t1.datetime
    print t2.datetime
    assert t1 == t2

  def test_current_temperature_returns_most_recent_entry(self):
    t1 = thermometer.Temperature(72.0, datetime.now())
    t2 = thermometer.Temperature(68.0, datetime.now())
    self.store.persist(t1)
    self.store.persist(t2)
    assert t2 == self.store.current_temperature()

  def test_does_not_error_with_no_previous_entries(self):
    try:
      temperature = self.store.current_temperature()
    except:
      self.fail("store#current_temperature() should not return an error when no values are present")

    assert None == temperature
