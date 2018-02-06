import sqlalchemy
import config


class DBHelper:

    def __init__(self, database):
        self.connect(config.DATABASE_USER, config.DATABASE_PW, database)

    def connect(self, user, password, db, host=config.DATABASE_HOST, port=config.DATABASE_PORT):
        # We connect with the help of the PostgreSQL URL
        # postgresql://federer:grandestslam@localhost:5432/tennis
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)

        # The return value of create_engine() is our connection object
        self.con = sqlalchemy.create_engine(url, client_encoding='utf8')

        # We then bind the connection to MetaData()
        self.meta = sqlalchemy.MetaData(bind=self.con, reflect=True)

    def get_connection(self):
        return self.con

    def insert(self, entry, table_name):
        table = self.meta.tables[table_name]
        statement = table.insert().values(entry)
        self.con.execute(statement)

    def get_table_column_names(self, table_name):
        table = self.meta.tables[table_name]
        table_names = []
        for column in table.c:
            table_names.append(column.key)
        return table_names

    def select_all_entries_where(self, table_name, key, value):
        results = self.meta.tables[table_name]
        statement = results.select().where(getattr(results.c, key) == value)
        return self.con.execute(statement)
