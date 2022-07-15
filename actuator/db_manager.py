import time
import psycopg2
from credentials import *


class DBManager:
    def connection(self):
        return psycopg2.connect(host=DB_HOST,
                                port=DB_PORT,
                                database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASSWORD)

    def __init__(self):
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime(time.time())) + ' ' +
              f'[INFO] DBManager initialized on \'{DB_HOST}\'.')

    def get_actuators(self):
        self.conn = self.connection()
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT * FROM actuator;')
        colnames = [desc[0] for desc in self.cur.description]
        actuators = self.cur.fetchall()
        self.conn.close()
        return actuators, colnames
