import psycopg2
from datetime import date

class DbConectionBase:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def open(self):
        self.connection = psycopg2.connect( host = "localhost"
                            , port = "5432"
                            , user = "postgres"
                            , password = ""
                            , database = "banking")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()


class DbClient(DbConectionBase):

    def overdrawn(self):
        self.open()

        statement = f"""
            SELECT id
            , first_name
            , last_name
            , card_number
            , expiration_date
            , balance
            FROM clients_and_credit_cards
            WHERE balance < 0;
        """
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return rows

    def balanceGreaterThan(self, amount):
        self.open()

        statement = f"""
            SELECT id
            , first_name
            , last_name
            , card_number
            , expiration_date
            , balance
            FROM clients_and_credit_cards
            WHERE balance > {int(amount)};
        """
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return rows

    def balanceLessThan(self, amount):
        self.open()

        statement = f"""
            SELECT id
            , first_name
            , last_name
            , card_number
            , expiration_date
            , balance
            FROM clients_and_credit_cards
            WHERE balance < {int(amount)};
        """
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return rows

    def expired(self):
        self.open()

        today = date.today()

        statement = f"""
            SELECT id
            , first_name
            , last_name
            , card_number
            , expiration_date
            , balance
            FROM clients_and_credit_cards
            WHERE expiration_date < '{today}';
        """
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return rows


    def overdrawnList(self,addList):
        newList = []
        for client in addList:
            if client[5] < 0:
                newList.append(client)
        return newList


    def balanceGreaterThanList(self,amount,addList):
        newList = []
        for client in addList:
            if client[5] > int(amount):
                newList.append(client)
        return newList

    def balanceLessThanList(self,amount,addList):
        newList = []
        for client in addList:
            if client[5] < int(amount):
                newList.append(client)
        return newList

    def expiredList(self,addList):
        newList = []
        for client in addList:
            if client[4] < str(date.today()):
                newList.append(client)
        return newList

    