import thermometer

class CLI:
  def __init__(self):
    db = thermometer.Database('thermometer.db')
    self.store = thermometer.Store(db)

  def record(self):
    temperature_sensor = thermometer.sensor("/dev/ttyACM0")
    current = temperature_sensor.current_temperature()
    self.store.persist(current)
    print current

  def display(self):
    print self.store.current_temperature()

  def run(self, argv):
    if len(argv) < 2:
      print "usage"
      exit()

    self.execute(argv[1])

  def execute(self, command):
    getattr(self, command, self.unknown_command)()

  def unknown_command(self):
    print "unknown command"
