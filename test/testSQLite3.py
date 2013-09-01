import sqlite3
import unittest


class TestSqlLiteService(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('resources/example.db')
        self.cursor = self.conn.cursor()

    def setTest(self):
        # Create table
        self.cursor.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
        # Insert a row of data
        self.cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        self.conn.commit()# Save (commit) the changes

    def testValue(self):
        t = ('RHAT',)
        self.cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
        print self.cursor.fetchone()

    def testNotExistentDB(self):
        self.assertRaises(sqlite3.OperationalError,self.cursor.execute,'SELECT * FROM stocks')