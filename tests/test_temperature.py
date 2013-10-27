import thermometer
from datetime import datetime, timedelta

def test_temperature_equality():
  now = datetime.now()
  t1 = thermometer.Temperature(70.0, now)
  t2 = thermometer.Temperature(70.0, now)
  assert t1 == t2

def test_temperature_equality_with_different_times():
  now = datetime.now()
  later = now + timedelta(seconds=1)
  t1 = thermometer.Temperature(70.0, now)
  t2 = thermometer.Temperature(70.0, later)
  assert t1 != t2

def test_temperature_conversion_to_celcius():
  temperature = thermometer.Temperature(68.0, datetime.now())
  celcius = 20.0
  assert celcius == temperature.celcius

def test_temperature_conversion_from_string():
  temperature = thermometer.Temperature("68.0", datetime.now())
  assert 68.0 == temperature.farenheit

def test_temperature_truncation_of_celcius():
  temperature = thermometer.Temperature(69.0, datetime.now())
  assert 20.56 == temperature.celcius

