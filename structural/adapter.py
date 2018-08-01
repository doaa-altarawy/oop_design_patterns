"""
    - Adapter: Converts one interface into another (make them compatible)
               wraps existing class with another interface
    Related:
    - Proxy: wraps an existing object to control/check/simplify its services for
             the callers

    - The example here uses Strategy design pattern (behavioural):
        Encapsulate classes and then make them interchangeable
"""

from abc import abstractmethod, ABC


class MySQL:
    """Handle MySQL DB connection"""

    def connect_to_DB(self, uri):
        print('many steps to connect to DB')

    def run_query(self, query):
        print('Mysql specific query')


class Postgres:
    """Handle Postgres DB connection"""

    def create_connection(self, another_uri):
        print('many steps to connect to DB')

    def query_DB(self, query):
        print('Some Postgres SQL specific query')

# --------------------------------------


class DBAdapter(ABC):

    @abstractmethod
    def connect(self, path, username, password):
        pass

    @abstractmethod
    def query(self, query_text):
        pass


class MySQLAdapter(DBAdapter):
    def __init__(self):
        self.database = MySQL()

    def connect(self, path, username, password):
        uri = '{}:{}/{}'.format(path, username, password)
        self.database.connect_to_DB(uri)

    def query(self, query_text):
        self.database.run_query(query_text)


class PostgresAdapter(DBAdapter):
    def __init__(self):
        self.database = Postgres()

    def connect(self, path, username, password):
        uri = '{}::{}-{}'.format(path, username, password)
        self.database.create_connection(uri)

    def query(self, query_text):
        self.database.query_DB(query_text)
        
# --------------------------------------------------

db = MySQLAdapter()
db = PostgresAdapter()


db.connect('long/path', 'name', 'pass')

db.query('find this item')
