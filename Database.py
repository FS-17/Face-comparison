import sqlite3
import random


class database:
    """
    This class is used to interact with the database
    """

    def __init__(self):
        self.conn = sqlite3.connect("faces.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS faces (name TEXT, encoding TEXT)")
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM faces")
        return self.cursor.fetchall()

    def reset(self):
        self.cursor.execute("DELETE FROM faces")
        self.conn.commit()

    def test(self):
        # add test data using the fake data
        for i in range(10):
            self.cursor.execute(
                "INSERT INTO faces (name, encoding) VALUES (?, ?)", (f"test{i}", str(random.random())))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
