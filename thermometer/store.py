from temperature import Temperature

class Store:
  def __init__(self, database):
    self.database = database

  def persist(self, temperature):
    self.database.insert("INSERT INTO temperatures (farenheit) VALUES (?)", [str(temperature.farenheit)])

  def current_temperature(self):
    result = self.database.select_one("SELECT temperatures.farenheit FROM temperatures ORDER BY id DESC LIMIT 1")
    return Temperature(result["farenheit"])

  def setup(self):
    self.database.execute_and_commit("CREATE TABLE IF NOT EXISTS temperatures (id INTEGER PRIMARY KEY, farenheit TEXT)")

  def reset(self):
    self.database.drop_table("temperatures")
    self.setup()

