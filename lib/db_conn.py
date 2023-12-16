import mysql.connector as conn

pwd =  'yogesh'
db_name = 'banking_project'

db = conn.connect(
    host = 'localhost',
    user = 'root',
    password = f'{pwd}', 
    charset = 'utf8',
    database= f'{db_name}' 
)