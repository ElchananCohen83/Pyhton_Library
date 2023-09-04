import sqlite3
from datetime import date

class Database:

    def __init__(self, db_name: str):
        # Connect to the SQLite database
        self.__connection = sqlite3.connect(db_name + '.db')

    def execute(self , query):
        # Create a cursor object
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        return cursor


    def select(self, table_name):
        # Execute a query to retrieve data
        select_query = f"SELECT * FROM {table_name}"
        cursor = self.execute(select_query)

        # Fetch all the rows as a list of tuples
        rows = cursor.fetchall()
        # Close the cursor and the database connection
        return rows

    def select_field_where(self, table_name, column, row, value):
        # Execute the SQL query
        select_where_query = f"SELECT {column} FROM {table_name} WHERE {row} = {value}"
        cursor = self.execute(select_where_query)
        # Fetch the results
        results = cursor.fetchall()
        if results == []:
            print('row does not exist')
            return None
        elif len(results[0]) == 1:
            return results[0][0]
        else:
            return results

    def insert_lending_book(self, book_id, costumer_id, status=True):
        # Define the SQL query with string formatting
        insert_query = f"INSERT INTO library ('book_id','costumer_id', 'date_of_delivery', 'status' ) VALUES({book_id}, {costumer_id}, '{date.today()}', {status})"
        self.execute(insert_query)

    def delete(self, table_name: str, row_id: int):
        # Define the SQL query with string formatting
        delete_query = f"DELETE FROM {table_name} WHERE id='{row_id}'"
        self.execute(delete_query)


    def update(self,table_name, column, row, value):
        # Define the SQL query with placeholders
        update_query = f"UPDATE {table_name} SET {column} = '{value}' WHERE id = {row}"
        cursor = self.execute(update_query)
        return cursor

    def catalog(self, table_name, column):
        catalog_query = f"SELECT DISTINCT {column} FROM {table_name}"
        cursor = self.execute(catalog_query)
        return cursor
