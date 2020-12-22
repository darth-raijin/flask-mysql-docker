import mysql.connector
from mysql.connector import cursor
import json


class Database:
    # dbConnector is the attribute that allows connection to the database
    def __init__(self):
        self.__db = "__change"
        self.__dbHost = "database"
        self.__dbPort = "3306"
        self.__dbUser = "root"
        self.__dbPassword = "pass"
        self.__dbConnector = None
        self.__connect()

    def __connect(self):
        self.__dbConnector = mysql.connector.connect(
            host=self.__dbHost,
            port=self.__dbPort,
            user=self.__dbUser,
            password=self.__dbPassword,
            database=self.__db
        )

    def __getConnector(self):
        if self.__dbConnector.is_connected() is False:
            self.__connect()
        return self.__dbConnector

    def __getCursor(self):
        connector = self.__getConnector()
        return connector.cursor(dictionary=True)

    def insert(self, dicObj):
        # Example for insert in database
        dbConnector = self.__getConnector()
        cursor = self.__getCursor()
        cursor.execute(
            """
                INSERT INTO __table (
                    name
                ) VALUES ('{}');
            """.format(
                dicObj["name"]
            )
        )
        self.__dbConnector.commit()

    def get_persons(self):
        # Example for select
        dbConnector = self.__getConnector()
        cursor = self.__getCursor()
        
        cursor.execute(
            """
            SELECT * FROM __table;
        """
        )
        # Converts SQL result to JSON
        result = json.dumps(cursor.fetchall())
        return result
