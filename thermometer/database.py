import sqlite3

class Database:
  def __init__(self, database_name):
    self.connection = sqlite3.connect(database_name)
    self.connection.row_factory = sqlite3.Row

  def create_table(self, sql):
    self.execute_and_commit(sql)

  def drop_table(self, table_name):
    self.execute_and_commit("DROP TABLE IF EXISTS " + table_name)

  def insert(self, sql, variables):
    self.execute_and_commit(sql, variables)

  def select_one(self, sql):
    cursor = self.__execute(sql)
    return cursor.fetchone()

  def execute_and_commit(self, *args):
    self.__execute(*args)
    self.connection.commit()

  def __execute(self, *args):
    cursor = self.connection.cursor()
    cursor.execute(*args)
    return cursor

