from tkinter import *
#from lib.NavigationBar import NavBar

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def manager(root,window):
    with open('assets\data.txt','r') as datafile:
        account_id=datafile.read()

    from views.Account import Account
    from views.Transactions import Transactions
    from views.Notifications import Notifications
    from views.NetBanking import NetBanking
    from views.AboutUs import AboutUs

    
    if window == 'acc':
        Account(root, account_id=account_id)
    elif window == 'tran':
        Transactions(account_id)
    elif window == 'netb':
        NetBanking(root, account_id=account_id)
    elif window == 'notif':
        Notifications(root, account_id=account_id)
    elif window == 'about':
        AboutUs(root)