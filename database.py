import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1029"
        )
        self.cursor = self.db.cursor()

        self.__createAndConnectDatabase()
        self.__createDictionaryTable()
    

    def __createAndConnectDatabase(self):
        create_query = "CREATE DATABASE IF NOT EXISTS app;"
        use_query = "USE app;"
        
        self.cursor.execute(create_query)
        self.cursor.execute(use_query)


    def __createDictionaryTable(self):
        create_query = """
            CREATE TABLE IF NOT EXISTS dictionary (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                ENGLISH VARCHAR(64) NOT NULL,
                UZBEK VARCHAR(64) NOT NULL
            );
        """
        self.cursor.execute(create_query)
    

    def addWord(self, english: str, uzbek: str):
        sql = f"INSERT INTO dictionary (ENGLISH, UZBEK) VALUE (%s, %s);"
        self.cursor.execute(sql, (english, uzbek))
        self.db.commit()
    
    def selectWords(self):
        sql = "SELECT * FROM dictionary;"
        self.cursor.execute(sql)
        words = self.cursor.fetchall()
        return words