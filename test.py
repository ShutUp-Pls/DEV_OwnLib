import psycopg2

conn = psycopg2.connect(user='tu_usuario', password='tu_contraseña', host='localhost')
cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
for db in cur.fetchall():
    print(db[0])
cur.close()
conn.close()
