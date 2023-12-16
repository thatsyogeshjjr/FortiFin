from lib.db_conn import *
import datetime
from lib.comm_functions import *

cur = db.cursor()

def register(fname,lname,email,pword,date):
    try:
        cust_id = gen_id()    
        query = f'''insert into customers(customer_id, name, email, dob) values('{cust_id}', '{fname+' '+lname}','{email}','{date}');'''
        print(query)
        cur.execute(query)    
        query = f'''insert into accounts values('{gen_id()}', '{cust_id}','{pword}','Savings',100.00, "{datetime.datetime.now().strftime("%Y-%m-%d")}")'''
        print(query)
        cur.execute(query)
        db.commit()
    except:
        print('Error: Failure in inserting data. Rolling Back')
        db.rollback()