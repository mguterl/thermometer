from temperature import Temperature
from datetime import datetime

class Store:
  def __init__(self, database):
    self.database = database

  def persist(self, temperature):
    self.database.insert("INSERT INTO temperatures (farenheit, created_at) VALUES (?, ?)", [str(temperature.farenheit), self.format_datetime(temperature.datetime)])

  def current_temperature(self):
    result = self.database.select_one("SELECT temperatures.farenheit, temperatures.created_at FROM temperatures ORDER BY id DESC LIMIT 1")
    return Temperature(result["farenheit"], self.parse_datetime(result["created_at"]))

  def setup(self):
    self.database.execute_and_commit("CREATE TABLE IF NOT EXISTS temperatures (id INTEGER PRIMARY KEY, created_at TEXT, farenheit TEXT)")

  def reset(self):
    self.database.drop_table("temperatures")
    self.setup()

  def format_datetime(self, datetime):
    return datetime.isoformat(" ")

  def parse_datetime(self, string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")
