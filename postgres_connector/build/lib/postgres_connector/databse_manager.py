import os

from psycopg2 import pool


class DatabaseManager(object):
    class __DatabaseManager:
        def __init__(self):
            self.connection_pool = None

        def establish_connection(self, user, password, host, port, database):
            if self.connection_pool:
                return

            self.connection_pool = pool.ThreadedConnectionPool(1, 20,
                                                               user=user,
                                                               password=password,
                                                               host=host,
                                                               port=port,
                                                               database=database)

        def get_conn_from_pool(self):
            return self.connection_pool.getconn()

        def return_conn_to_pool(self, db_conn):
            return self.connection_pool.putconn(db_conn)

        def terminate_connection(self):
            self.connection_pool.closeall()
            print('All database connections terminated')

        def status(self):
            return self.connection_pool.status()

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not DatabaseManager.instance:
            DatabaseManager.instance = DatabaseManager.__DatabaseManager()
        return DatabaseManager.instance
