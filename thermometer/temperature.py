# -*- coding: utf-8 -*-

class Temperature:
  def __init__(self, farenheit, datetime):
    self.farenheit = float(farenheit)
    self.celcius = round(((self.farenheit - 32) * 5) / 9, 2)
    self.datetime = datetime
  def __repr__(self):
    return "{farenheit}°F ({celcius}°C)".format(farenheit=self.farenheit, celcius=self.celcius)
  def __eq__(self, other):
    return self.__dict__ == other.__dict__
