import os
import psycopg2
from urllib.parse import *


class DB:
    m_connection = None
    m_debug = False
    LOCALCONNECTIONSTRING = 'postgres://lpxwpbyxzaimtq:' \
                            'fc712f2b7cff6d6a1757ea8c99dd9f39e30345d61ab394e421bcdf327f626be7@' \
                            'ec2-54-75-229-201.eu-west-1.compute.amazonaws.com:5432/d5lh5hdl6s3klp'

    # Table headers are hardcoded
    VALUES_FORMAT = "(%(AquantID)s,%(CustomerID)s,%(CreatedDate)s,%(LastModified)s,%(WorkOrder)s," \
                    "%(ProductType_Name)s,%(ProductType_ID)s,%(Manufacturer_Name)s,%(Manufacturer_ID)s," \
                    "%(Product_Name)s,%(Product_ID)s,%(Observation_Name)s,%(Observation_ID)s," \
                    "%(Observation_Value)s,%(Solution_Name)s,%(Solution_ID)s,%(Part_Name)s," \
                    "%(Part_ID)s,%(PartDescription)s)"

    ONCONFLICT_UPDATE = 'DO UPDATE SET '\
                        '"CustomerID"=EXCLUDED."CustomerID", "LastModified"=EXCLUDED."LastModified",'\
                        '"WorkOrder"=EXCLUDED."WorkOrder", "ProductType_Name"=EXCLUDED."ProductType_Name",'\
                        '"ProductType_ID"=EXCLUDED."ProductType_ID","Manufacturer_Name"=EXCLUDED."Manufacturer_Name",'\
                        '"Manufacturer_ID"=EXCLUDED."Manufacturer_ID", "Product_Name"=EXCLUDED."Product_Name",'\
                        '"Product_ID"=EXCLUDED."Product_ID", "Observation_Name"=EXCLUDED."Observation_Name",'\
                        '"Observation_ID"=EXCLUDED."Observation_ID","Observation_Value"=EXCLUDED."Observation_Value",'\
                        '"Solution_Name"=EXCLUDED."Solution_Name", "Solution_ID"=EXCLUDED."Solution_ID",'\
                        '"Part_Name"=EXCLUDED."Part_Name", "Part_ID"=EXCLUDED."Part_ID", "PartDescription"=EXCLUDED."PartDescription"'\
                        'where public."Stark"."AquantID"=EXCLUDED."AquantID";'

    ONCONFLICT_NOTHING = 'DO NOTHING'

    TABLESCHEMA_FORMAT = 'INSERT INTO %(schema)s.%(table)s VALUES {} ON CONFLICT ("AquantID") {}'

    DELETE_RECORDS = 'delete from %(schema)s.%(table)s'


    def connect(self, i_debug=False):
        try:
            url = urlparse(os.environ["DATABASE_URL"])
        except:
            url = urlparse(self.LOCALCONNECTIONSTRING)

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

    def insertSingleRow(self, jsonParams):
        with self.m_connection:
            with self.m_connection.cursor() as curs:
                curs.execute('INSERT INTO %(schema)s.%(table)s ("Col1", "Col2") VALUES (%(col1)s, %(col2)s);', jsonParams)

    def insertBulkRows(self, jsonParamsArray):
        with self.m_connection:
            with self.m_connection.cursor() as curs:
                valuesArray = jsonParamsArray.get('valueArray')
                args_str = (curs.mogrify(self.VALUES_FORMAT, x).decode('utf-8-sig') for x in valuesArray)
                args_str = ','.join(args_str)
                if jsonParamsArray['AllowUpdate'] is not None:
                    query = self.TABLESCHEMA_FORMAT.format(args_str, self.ONCONFLICT_UPDATE)
                else:
                    query = self.TABLESCHEMA_FORMAT.format(args_str, self.ONCONFLICT_NOTHING)
                curs.execute(query, jsonParamsArray)

    def deleteRecords(self, params):
        with self.m_connection:
            with self.m_connection.cursor() as curs:
                curs.execute(self.DELETE_RECORDS, params)
