class Connection:
  def __init__(self, serial_port):
    self.serial_port = serial_port
  def send(self, command):
    self.write(command)
    return self.read()
  def write(self, command):
    self.serial_port.write("{command}\n".format(command=command))
  def read(self):
    output = self.serial_port.readline()
    return self.parse(output)
  def parse(self, value):
    return value.rstrip().split(':')[-1]

