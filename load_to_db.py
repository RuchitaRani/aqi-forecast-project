import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn=psycopg2.connect(
    dbname="aqi_forecast",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port="5432"
)

cur=conn.cursor()

print("Connected successfully")
