from postgres_connector.databse_manager import DatabaseManager


class ConnectionManager:
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager

    def __enter__(self):
        self.db_conn = self.database_manager.get_conn_from_pool()
        return self.db_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database_manager.return_conn_to_pool(self.db_conn)


