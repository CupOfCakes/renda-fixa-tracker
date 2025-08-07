import psycopg2  # for PostgreSQL
from urllib.parse import quote

# Connection data
user = 'postgres'  # <<< username, postgres is the default name
password = 'password'  # <<< database password, don't put your password in you code, it's dangerous
host = 'IP'  # <<< Host name/address is the database IP
port = '5432'  # port you config, 5432 is a commun port
database = 'name'  # name of the database

# turning password into UTF-8
password = quote(password)

# open connection
conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)

# close connection
conn.close()
