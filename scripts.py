import psycopg2
import json


class Creating():

    def openData(self):
            self.connection = psycopg2.connect( host = "localhost"
                                , port = "5432"
                                , user = "postgres"
                                , password = "2793ev500"
                                , database = "banking")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

    def createTableClients(self):
        connection = psycopg2.connect( host = "localhost"
                                    , port = "5432"
                                    , user = "postgres"
                                    , password = "2793ev500"
                                    , database = "banking")

        connection.autocommit = True
        cursor = connection.cursor()

        createTableCommand = """
                    CREATE TABLE clients_and_credit_cards (
                        id INT NOT NULL,
                        first_name varchar(20) NOT NULL,
                        last_name varchar(30) NOT NULL,
                        card_number varchar(20) NOT NULL,
                        expiration_date varchar(11) NOT NULL,
                        balance FLOAT NOT NULL
                    );
                """
        cursor.execute(createTableCommand)

        cursor.close()
        connection.close()


    def uploadJSON(self):
        with open("bank_clients.json", "r") as file:
            content = json.loads(file.read())
            for client in content:
                for card in client["credit_cards"]:
                    self.openData()

                    statement = f"""
                        INSERT INTO clients_and_credit_cards
                        (
                            id,
                            first_name,
                            last_name,
                            card_number,
                            expiration_date,
                            balance
                        )
                        VALUES
                        (
                            '{client["id"]}',
                            '{client["first_name"]}',
                            '{client["last_name"].replace("'","''")}',
                            '{card["card_number"]}',
                            '{card["expiration_date"]}',
                            '{card["balance"]}'
                        );
                    """

                    self.cursor.execute(statement)
                    self.cursor.close()
                    self.connection.close()
            

