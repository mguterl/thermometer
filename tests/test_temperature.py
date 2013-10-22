from thermometer import thermometer

def test_temperature_equality():
  print dir(thermometer)
  t1 = thermometer.Temperature(70.0)
  t2 = thermometer.Temperature(70.0)
  assert t1 == t2

def test_temperature_conversion_to_celcius():
  temperature = thermometer.Temperature(68.0)
  celcius = 20.0
  assert celcius == temperature.celcius

def test_temperature_conversion_from_string():
  temperature = thermometer.Temperature("68.0")
  assert 68.0 == temperature.farenheit

def test_temperature_truncation_of_celcius():
  temperature = thermometer.Temperature(69.0)
  assert 20.56 == temperature.celcius

