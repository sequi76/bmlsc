import psycopg2

CONN_STR = '''sslmode=verify-ca
sslrootcert=certificates/server-ca.pem
sslcert=certificates/client-cert.pem
sslkey=certificates/client-key.pem
hostaddr=35.247.202.83
port=5432
user=bmlsc-user
password=bmlsc-password
dbname=bmlsc'''

def singleQuery(query):
	connection = psycopg2.connect( CONN_STR )
	cursor = connection.cursor()
	cursor.execute(query)
	data = cursor.fetchall()
	cursor.close()
	connection.close()
	return data


def cursorQuery(query):
	connection = psycopg2.connect( CONN_STR )
	cursor = connection.cursor()
	cursor.execute(query)
	return connection, cursor
	
def aCursor():
	connection = psycopg2.connect( CONN_STR )
	cursor = connection.cursor()
	return connection, cursor
