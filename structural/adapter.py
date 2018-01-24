"""
    Converts one interface into another
    wrap existing classs with another interface
"""

from abc import abstractmethod, ABC


class MySQL:
    def connect_to_DB(self, uri):
        print('many steps to connect to DB')

    def run_query(self, query):
        print('Mysql specific')

class Postgres:

    def create_connection(self, another_uri):
        print('many steps to connect to DB')

    def query_DB(self, query):
        print('Mysql specific')

# --------------------------------------

class Adapter(ABC):

    @abstractmethod
    def connect(self, path, username, password):
        pass

    @abstractmethod
    def query(self, query_text):
        pass


class MySQL_Adapter(Adapter):
    def __init__(self):
        self.database = MySQL()

    def connect(self, path, username, password):
        uri = '{}:{}/{}'.format(path, username, password)
        self.database.connect_to_DB(uri)

    def query(self, query_text):
        self.database.run_query(query_text)

class Postgres_Adapter(Adapter):
    def __init__(self):
        self.database = Postgres()

    def connect(self, path, username, password):
        uri = '{}::{}-{}'.format(path, username, password)
        self.database.create_connection(uri)

    def query(self, query_text):
        self.database.query_DB(query_text)
        
# --------------------------------------------------

db = MySQL_Adapter()
db = Postgres_Adapter()


db.connect('long/path', 'name', 'pass')

db.query('find this item')
