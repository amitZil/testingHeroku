import os
import psycopg2
from urllib.parse import *


class DB:
    m_connection = None
    m_debug = False;
    LOCALCONNECTIONSTRING = 'postgres://lpxwpbyxzaimtq:fc712f2b7cff6d6a1757ea8c99dd9f39e30345d61ab394e421bcdf327f626be7@ec2-54-75-229-201.eu-west-1.compute.amazonaws.com:5432/d5lh5hdl6s3klp'

    def connect(self, i_debug=False):
        if i_debug:
            url = urlparse(self.LOCALCONNECTIONSTRING)
        else:
            url = urlparse(os.environ["DATABASE_URL"])

        con = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        return con

    def sample_query(self, query):

        with self.m_connection:
            with self.m_connection.cursor() as curs:
                curs.execute('select "Col1" from public."Test"')
                value = curs.fetchone()
        return value

    def __init__(self, debug):
        self.m_connection = self.connect(debug)
        self.m_debug = debug

