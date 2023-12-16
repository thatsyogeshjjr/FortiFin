from lib.db_conn import *

try:
    if db.is_connected():
        print('[!] Connection established')
        cur = db.cursor()

except:
    print('[!] Connection failed')


def auth(uname, pword):
    query = f'''select * from accounts where 
    customer_id in (select customer_id from customers where email='{uname}') or 
    customer_id in (select customer_id from accounts where account_id='{uname}') and 
    account_pwd = '{pword}';'''
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    if len(rows) != 0:
        for i in rows:
            return i[0]
    else:
        print('Auth.py: No Account Found')
        return 0

# if id == 0 or id == None:
#     print('[-] Wrong username or password')
# else:
#     print(f'Logging in at {id}')