from lib.db_conn import *
from lib.comm_functions import *
import datetime

'''
How do I work?

1. Check if receiver exists
2. Check if balance is enough to go through with mainion
3. If yes update the amount in accounts table
    also add row in trasactions column about this mainion.
else block mainion
'''

def validate_receiver(sender_id, receiver_id):
    cur = db.cursor()
    cur.execute(f'select * from accounts where account_id = "{receiver_id}"')
    if cur.fetchall() == [] or sender_id == receiver_id:
        return False
    else:
        return True
    
def validate_balance(sender_id, amount):
    cur = db.cursor()
    cur.execute(f"select balance from accounts where account_id = '{sender_id}';")
    if cur.fetchall()[0][0] < amount:
        return False
    else:
        return True
    

def transact(sender_id, receiver_id, amount):
    cur = db.cursor()
    cur.execute(f"update accounts set balance=balance-{amount} where account_id='{sender_id}';")
    cur.execute(f"update accounts set balance=balance+{amount} where account_id='{receiver_id}';")
    cur.execute(f"insert into transactions values('{gen_id()}','{sender_id}','{receiver_id}',{amount},'{datetime.datetime.now().strftime('%Y-%m-%d')}')")

    
    cur.execute(f'insert into notifications values("{gen_id(6)}", "{sender_id}", "transfer", "{receiver_id}###{amount}###Transaction Successful", NULL,1)')
    cur.execute(f'insert into notifications values("{gen_id(6)}", "{receiver_id}", "receive", "{sender_id}###{amount}###Transaction Successful", NULL,1)')
        
        
    db.commit()

def main(sender_id, receiver_id, amount):
    if validate_receiver(sender_id,receiver_id):
        if validate_balance(sender_id, amount):
            transact(sender_id, receiver_id, amount)
            print('[+] Transaction Successful')
        else:
            print('Amount is larger than balance')

    else:
        print('Reciver Not Valid')
        exit()
    

# main('cph17qeb3gjn','5b5xc5cy7le6',12)