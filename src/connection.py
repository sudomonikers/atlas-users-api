import mysql.connector
from mysql.connector import Error 
import os
from dotenv import load_dotenv
load_dotenv()

credentials = {
    'user': os.environ['USER'],
    'password': os.environ['PASSWORD'],
    'host': os.environ['HOST'],
    'database': os.environ['DATABASE']
}


def query(query, arguments):
    try:
        cnx = mysql.connector.connect(**credentials)
        cursor = cnx.cursor(buffered=True,dictionary=True)

        cursor.execute(query, (arguments))
        result = cursor.fetchall()

        cursor.close()
        cnx.close()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")





