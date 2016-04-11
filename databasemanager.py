import psycopg2
import sqlalchemy as sa


class DatabaseManager():

    def __init__(self, server, database, user, pwd):
        conn_string = str.format('postgresql://{0}:{1}@{2}/{3}', user, pwd, server, database)
        self.engine = sa.create_engine(conn_string)


    def insert_values_into_table(self, table_name, values):
        conn = self.engine.connect()
        metadata = sa.MetaData(self.engine)
        conn.execute(sa.Table(tableName, metadata, autoload=True).insert(values))
        conn.close()