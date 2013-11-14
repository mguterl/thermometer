import unittest
from thermometer import FakeClock
import datetime

class TestFakeClock(unittest.TestCase):
  def test_now_returns_last_time_with_desired_interval(self):
    now = datetime.datetime(2013, 4, 30, 16, 5)
    clock = FakeClock(now)

    assert clock.now() == datetime.datetime(2013, 4, 30, 16, 10)
    assert clock.now() == datetime.datetime(2013, 4, 30, 16, 15)
