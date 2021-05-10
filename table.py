import sqlite3
from sqlite3 import Error
 
#Create Connection 
def create_connection(db_file):
	""" create a database connection to a SQLite database """
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		return conn
	except Error as e:
		print(e)

		return None

if __name__ == '__main__':
	create_connection("C:\SE Project\crime.db")

#Create Table
def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def main():
	database = "C:\SE Project\crime.db"

	sql_create_admin_table = """ CREATE TABLE IF NOT EXISTS admin (
						username text NOT NULL,
						password text NOT NULL
					);"""
	sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
						fname text NOT NULL,
						lname text NOT NULL,
						username text NOT NULL,
						password text NOT NULL
						
						
					);"""
	sql_create_fir_table = """ CREATE TABLE IF NOT EXISTS fir (
						firno text NOT NULL,
						victimfname text NOT NULL,
						victimlname text NOT NULL,
						dateofincident text NOT NULL,
						criminalfname text NOT NULL,
						criminallname text NOT NULL,
						crimecommitted text NOT NULL,
						placeofincident text NOT NULL
						
		
					);"""
		# create a database connection
	conn = create_connection(database)
	if conn is not None:
		# create user table
		create_table(conn, sql_create_admin_table)
		create_table(conn, sql_create_user_table)
		create_table(conn, sql_create_fir_table)
		
	else:
		print("Error! Cannot create the database connection.")

if __name__ == '__main__':
	main()
