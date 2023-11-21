import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_conn = mysql.connector.connect(host="kafkaprod1.westus3.cloudapp.azure.com", user="root",
password=os.getenv('db_pwd'), database="events")


db_cursor = db_conn.cursor()

db_cursor.execute('''
DROP TABLE power_usage, temperature_readings
''')

db_conn.commit()
db_conn.close()