import psycopg2

conn = psycopg2.connect(
    "dbname=postgres_ai user=postgres password=postgres host=localhost port=6543"
)
