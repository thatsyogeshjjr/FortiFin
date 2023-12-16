import tkinter

class Setup:
    def __init__(self) -> None:
        print('''

        ██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░██╗███╗░░██╗░██████╗░
        ██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██║████╗░██║██╔════╝░
        ██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░██║██╔██╗██║██║░░██╗░
        ██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██║██║╚████║██║░░╚██╗
        ██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗██║██║░╚███║╚██████╔╝
        ╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░

        ███████╗░█████╗░██████╗░████████╗██╗███████╗██╗███╗░░██╗
        ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝██║████╗░██║
        █████╗░░██║░░██║██████╔╝░░░██║░░░██║█████╗░░██║██╔██╗██║
        ██╔══╝░░██║░░██║██╔══██╗░░░██║░░░██║██╔══╝░░██║██║╚████║
        ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██║██║░░░░░██║██║░╚███║
        ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝
        * Created with Installer draftee by @thatsyogeshjjr         

              
            [!] Make sure you have an internet connection.  
            [!] Any old FortiFin database will be dropped.
''')
        
        confirm = input('               Do you wish to proceed [y/n](default no): ')
        if confirm != ""  and confirm[0].lower() in list('1y') :
            pass
        else:
            print('\n\n            [*] Exiting Installer.')
            exit()

        
        print('''        
        Status:
            [*] Installing Libraries''')    
        self.install_lib()
        self.db_name = 'banking_project'
        self.db = self.define_conn()
        self.setup_db()
        self.add_sample_data()
        self.finish()
        
    def install_lib(self):
        try:
            import subprocess
            subprocess.run("pip install mysql-connector-python".split())
            subprocess.run("pip install pillow".split())
            subprocess.run("pip install pandas".split())
            subprocess.run("pip install pyperclip".split())
        except:
            print('             [-] Install Stalled')
            print('             [-] Libraries could not be installed')
            exit()

    def define_conn(self):
        try: 
            import mysql.connector as mc
            print("                        [*] Setting up MySQL Connection.")
            print('''                      [!] MySQL user info required to setup database.''')
            usr= input("\n                MySQL username (default root):")
            if usr.replace(" ","") == "":
                usr='root'
            pwd= input("                MySQL user password: ")

            db = mc.connect(
                host='localhost',
                user=usr,
                password=pwd,
                charset='utf8'
            )

            return db
        except:
            print('\n\n             [-] Install Stalled')
            print('             [-] MySQL connection Failed')
            print('             [*] If you think the code failed due to setup code err.')
            print('             [*] Visit code lines 50~60')
            exit()
        

    def setup_db(self):
        try:
            print("                        [*] Setting up Databases")
            cur = self.db.cursor()
            cur.execute('show databases;')
            res = cur.fetchall()
            db_list=[res[i][0] for i in range(len(res))]

            if self.db_name in db_list:
                print("                        [*] Dropping older database")
                cur.execute(f'drop database {self.db_name}')
            
            print("                        [*] Creating new database")
            cur.execute(f'''create database {self.db_name}''')
            cur.execute(f'''use {self.db_name}''')


            print("                        [*] Inserting Tables in to database")
            cur.execute('''create table Customers(
                            customer_id char(12) primary key,
                            name varchar(30),
                            email varchar(40),
                            dob date
                            );''')
            cur.execute('''create table Accounts(
                            account_id  char(12) primary key,
                            customer_id char(12),
                            account_pwd varchar(12),
                            account_type varchar(12),
                            balance decimal(65,2),
                            created_date date,
                            foreign key (customer_id) references Customers(customer_id) on delete cascade on update cascade);''')
            cur.execute('''create table Loans(
                            loan_id char(6) primary key,
                            account_id char(12),
                            loan_type varchar(10),
                            loan_amt decimal(32,2),
                            interest_rate decimal(12,2),
                            start_date date,
                            end_date date,
                            foreign key (account_id) references Accounts(account_id) on delete cascade on update cascade);''')
            cur.execute('''create table Transactions (
                            transaction_id char(12) primary key,
                            account_id char(12),
                            receiver_id char(12),
                            amount decimal(65,2),
                            transaction_date date,
                        
                            foreign key (account_id) references Accounts(account_id),
                            foreign key (receiver_id) references Accounts(account_id) on delete cascade on update cascade);
                            ''')
            cur.execute('''create table notifications (
                            notif_id varchar (12) primary key,
                            account_id varchar (12),
                            type varchar (12),
                            content varchar (50),
                            date_added date,
                            show_notif tinyint(1),
                            foreign key (account_id) references Accounts(account_id) on delete cascade on update cascade);''')
            print("                        [*]  5 tables added")
            
        except:
            print("                        [!]  An Error occured during database setup.")
            print("                        [!]  Refer to setup_db function for more info.")


    def add_sample_data(self):
        # if required, add sample data for demo here 
        # though we have skipped this as account creation is in itself an important part of FortiFin
        # to create 2 accounts it would not take too much time.
        pass

    def finish(self):
        print("                        [*] Installation Complete with 0 errors")
        print("                        [*] Run Login.py to start FortiFin")
        
        

Setup()