import sqlite3


class Database:
    def __init__(self, path_to_db="E:\pyBot\data\main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            token varchar(255),
            PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    def create_table_tarif(self):
        sql = """
        CREATE TABLE Tarif (
            Name varchar(50) NOT NULL,
            Disk varchar(50),
            ram varchar(50),
            cpu varchar(50),
            price varchar(50),
            category varchar(50),
            PRIMARY KEY (Name)
            );
        """
        self.execute(sql, commit=True)

    def create_table_os(self):
        sql = """
        CREATE TABLE Os (
            name varchar (50) NOT NULL,
            distribution varchar (50),
            slug varchar (50),
            PRIMARY KEY (slug)
            );
        """
        self.execute(sql, commit=True)

    def create_table_apps(self):
        sql = """
        CREATE TABLE Apps (
            name varchar(50) NOT NULL,
            distribution varchar (50),
            slug varchar(50),
            PRIMARY KEY (slug)
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, token: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, token) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, token), commit=True)

    def add_tarif(self, Name: str, Disk: str, ram: str, cpu: str, price: str, category: str):
        sql = """
        INSERT INTO Tarif( Name, Disk, ram, cpu, price, category) VALUES(?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(Name, Disk, ram, cpu, price, category), commit=True)

    def add_os(self, name: str, distribution: str, slug: str):
        sql = """
        INSERT INTO Os( name, distribution, slug) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(name, distribution, slug), commit=True)

    def add_app(self, name: str, distribution: str, slug: str):
        sql = """
        INSERT INTO Apps( name, distribution, slug) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(name, distribution, slug), commit=True)

    def select_all_os(self):
        sql = """
        SELECT * FROM Os
        """
        return self.execute(sql, fetchall=True)

    def select_all_aps(self):
        sql = """
        SELECT * FROM Apps
        """
        return self.execute(sql, fetchall=True)

    def select_tarif(self, **kwargs):
        sql = "SELECT * FROM Tarif WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_user(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def get_user_token(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT token FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def update_user_token(self, token, id):
        sql = f"""
        UPDATE Users SET token=? WHERE id=?
        """
        return self.execute(sql, parameters=(token, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
