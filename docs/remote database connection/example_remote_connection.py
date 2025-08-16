import psycopg2  # for PostgreSQL
from urllib.parse import quote

# Connection data
user = 'user_crud'  # <<< username, postgres is the default name
password = 'crud'  # <<< database password, don't put your password in you code, it's dangerous
host = '192.168.100.93'  # <<< Host name/address is the database IP
port = '5432'  # port you config, 5432 is a commun port
database = 'rates'  # name of the database

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

cur = conn.cursor()

query = "SELECT * FROM rates"

cur.execute(query)
print(cur.fetchall())
cur.close()

# close connection
conn.close()
