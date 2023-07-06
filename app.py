from flask import Flask
from psycopg2 import connect

app = Flask(__name__)

host = 'localhost'
port = 5432
dbname = 'flask1'
user = 'postgres'
password = 'admin'

def get_connection() :
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@app.get('/api/v1/users')
def get_users():
    return 'getting users'

@app.get('/api/v1/users/1')
def get_user():
    return 'getting user'

@app.post('/api/v1/users')
def create_users():
    return 'creating users'

@app.put('/api/v1/users/1')
def update_users():
    return 'updating users'

@app.delete('/api/v1/users/1')
def delete_users():
    return 'deleting users'


if __name__ == '__main__' :
    app.run(debug=True)