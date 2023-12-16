
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from lib.NavigationBar import *
from lib.NotificationFrames import *
from lib.db_conn import *
import pandas as pd


def Notifications(window, account_id):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/notification_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#272829",
        height = 500,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    NavBar(window, canvas)

    global image_image_7
    image_image_7 = PhotoImage(file=relative_to_assets('image_7.png'))
    image_7 = canvas.create_image(
        123.0,
        68.0,
        image=image_image_7
    )
    
    canvas.create_rectangle(
        306.0,
        77.0,
        651.0,
        78.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        307.0,
        31.0,
        anchor="nw",
        text="Notifications",
        fill="#FFFFFF",
        font=("Inter Bold", 31 * -1)
    )

    notif_canvas = NotificationFrames()
    notif_canvas.create_notification_canvas(window)


    '''
    Usage : create_notif( type, data_in_field_1, data_in_field_2, data_in_field_3)
    fields depend on what type you use

    ------------------------------------------
    | type     |        fields               |
    ------------------------------------------
    | emi      | loan id,    amt,    message |
    | transfer | to,         amt,    message |
    | receive  | from,       amt,    message |
    ------------------------------------------
    
    '''


    '''
    note,
    PROBLEM: WITH MULTIPLE NOTIFICATIONS THE BACKGROUND GOES CRAZZY :)
    I'M DEAD <3
    '''

    #create_notif('emi', 'hello','world','69696')
    #get_notif_data('rjl2l9xg8iee')
    get_notif_data(account_id)
    #get_notif_data(account_id)
    # notif_canvas.create_notif('emi', 'hello', 'world' ,'this')
    # notif_canvas.create_notif('receive', 'hello', 'world' ,'this')
    # notif_canvas.create_notif('transfer', 'hello', 'world' ,'this')
    # notif_canvas.create_notif('emi', 'hello', 'world' ,'this')



def get_notif_data(account_id):
    q = f'select * from notifications where account_id = "{account_id}"'
    cur = db.cursor()
    cur.execute(q)
    data = pd.DataFrame(cur)
    # get type

    for i in range(len(data)):
        if data[5][i] == 1:
            values = data[3][i].split('###')
            type = data[2][i]
            create_notif(type, values[0], values[1] ,values[2])
    
