import thermometer

class CLI:
  def __init__(self):
    self.app = thermometer.App.start()

  def record(self):
    print self.app.record()

  def display(self):
    print self.app.read()

  def reset(self):
    print "Dropping and creating table temperatures"
    self.app.reset()

  def serve(self):
    thermometer.http.config['APP'] = self.app
    thermometer.http.run()

  def run(self, argv):
    if len(argv) < 2:
      print "usage"
      exit()

    self.execute(argv[1])

  def execute(self, command):
    getattr(self, command, self.unknown_command)()

  def unknown_command(self):
    print "unknown command"
