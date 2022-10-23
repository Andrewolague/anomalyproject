import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\sqlite\pythonsqlite.db")
#This is simply to create the connection the instructions for this are located in the readme
#We are considering an empty string or "" in either first or last name as an anomoly
#We are also considering an address starting with "123" as an anomoly
#Proceed to run the python script to connect then open the command prompt
#Type "sqlite3" in the command prompt       "sqlite>" should appear
#Set mode to CSV to import data(note to set headers in first row beforehand if possible)     .mode csv
#Set a path to the CSV containing the data then add a space with the following syntax follow along
#   .import c:/sqlite/rogue_data.csv Nameoftable
# Validate that the schema is correct for your CSV using .schema Nameoftable
#Begin doing a simple query with small amount of results to validate that the data is correct
# SELECT * FROM Nameoftable LIMIT 5;
# Now set the output for our results of intended data of collecting anomolies
# .output results.csv       This should normally save in the same area that the python script is located
# Final query for intended schema of firstname,lastname,address with table named Userdata
#SELECT * FROM Userdata WHERE firstname='' OR lastname='' OR address LIKE '123%';