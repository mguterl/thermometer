import datetime

class FakeClock:
  def __init__(self, now, minutes = 5):
    self.__now__ = now
    self.minutes = minutes

  def now(self):
    self.__now__ = self.__now__ + datetime.timedelta(minutes=self.minutes)
    return self.__now__
