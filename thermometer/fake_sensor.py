from thermometer import Temperature
from datetime import datetime
from random import randint

class FakeSensor:
  def __init__(self, base, clock = datetime):
    self.base = base
    self.current_value = base
    self.clock = clock
    self.max_difference = 10
    self.drift = 3

  def current_temperature(self):
    self.current_value = self.next_value()
    return Temperature(self.current_value, self.clock.now())

  def next_value(self):
    next_amount = randint(0, self.drift)

    if self.current_value + next_amount > self.base + self.max_difference:
      current_value = self.current_value - next_amount
    else:
      current_value = self.current_value + next_amount

    return current_value
