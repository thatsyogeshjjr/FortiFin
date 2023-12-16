'''
This file will be used to store
// functions that are used multiple times
// to avoid redundant functions
'''
import random

def placeholder(widget, text):
    def focus():
        widget.delete(0,'end')
        widget.insert(0,'')

    def not_focus():
        if widget.get() == '':
            widget.delete(0,'end')
            widget.insert(0,text)

    widget.insert(0,text)
    widget.bind("<FocusIn>", lambda args:focus())
    widget.bind("<FocusOut>", lambda args: not_focus())

# class AccountDataFetchingError(Exception):
#     print(''' AccountDataFetchingError: Raised when problems occour when fetching data from database.''')

def gen_id(val=12):
    alpha=list('abcdefghijklmnopqrstuvwxyz0123456789')
    x = []
    for i in range(val):
        x.append(random.choice(alpha))

    return ''.join(str(i) for i in x)


