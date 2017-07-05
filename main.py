from flask import Flask
import os
import psycopg2
from urllib.parse import *

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "<h1 style='color:blue'>"+os.environ["DATABASE_URL"]+"</h1>"


def connectDB(i_database=None, i_user=None, i_password=None, i_host=None, i_port=None):
    #urlparse.uses_netloc.append("postgres")
    #url = urlparse.urlparse(os.environ["DATABASE_URL"])

    if i_database is None:
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    else:
        conn = psycopg2.connect(
            database=i_database,
            user=i_user,
            password=i_password,
            host=i_host,
            port=i_port
        )
    return conn


conn = connectDB('d5lh5hdl6s3klp', 'lpxwpbyxzaimtq', 'fc712f2b7cff6d6a1757ea8c99dd9f39e30345d61ab394e421bcdf327f626be7',
                'ec2-54-75-229-201.eu-west-1.compute.amazonaws.com', '5432')
cur = conn.cursor()
cur.execute('select "Col1" from public."Test"')
print(cur.fetchone())
