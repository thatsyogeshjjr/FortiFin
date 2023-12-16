from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, Frame, Label
import tkinter as tk
from lib.db_conn import *
import pandas as pd
import subprocess
'''
Developer Notes:

Why use global for variables like PhotoImage?
Answer:
The variable is garbage collected i.e. destroyed
This leads to a empty image box that's white
To avoid this problem, we use a variable with global scope 
i.e long lived and not destroyed after execution
'''
bg_number=0

OUTPUT_PATH = Path(__file__).parent
NOTIF_FRAME_ASSETS = OUTPUT_PATH / Path(r"../assets/notification_assets")


def relative_to_assets(path: str) -> Path:
    return NOTIF_FRAME_ASSETS / Path(path)

entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
image_image_1 = PhotoImage(
    file='assets/notification_assets/image_1.png')


class NotificationFrames:    
    def __init__(self) -> None:
        self.init_x_pos = 263
        self.init_y_pos = 111

    def create_notification_canvas(self, window):
        yval=self.init_y_pos
        global notif_canvas
        notif_canvas = Canvas(
        window,
        bg = "#272829",
        height = 700,
        width = 485,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge",
        scrollregion=(0,0,100000,100000)
    )
        notif_canvas.place(x = 263, y = yval)
        
        
        scrollbar = Scrollbar(window, 
                            orient='vertical', 
                            command=notif_canvas.yview,
                            width=20)
        scrollbar.pack(side='right', fill='both')
        
        def on_mousewheel(event):
            notif_canvas.yview_scroll(-1 * (event.delta // 120), "units")
        window.bind("<MouseWheel>", on_mousewheel)


        #notif_canvas.config(yscrollcommand=scrollbar.set)
    
        global frame
        frame = Frame(notif_canvas,
                    width = 485,
                    height=1000,
                    bg='#272829')
        
        notif_canvas.create_window((0, 0), window=frame, anchor='nw')


        return notif_canvas


def create_notif(type, *args):
    global entry_image_1,entry_image_2, image_image_1, button_image_1,button_image_2


    match type:
            case 'emi':
                title = 'Regarding EMI'
                field1 = 'Loan ID'
                field2 = 'Amount'
                field3 = 'Message'
            case 'loan':
                title = 'Loan Granted'
                field1 = 'Loan ID'
                field2 = 'Amount'
                field3 = 'Message'
            case 'transfer':
                title = 'Transfer Success'
                field1 = 'To'
                field2 = 'Amount'
                field3 = 'Message'
            case 'receive':
                title = 'Money Received'
                field1 = 'From'
                field2 = 'Amount'
                field3 = 'Message'
            case _:
                return 'BAD NOTIF TYPE'


    canvas = Canvas(
        frame,
        bg = "#272829",
        height = 205,
        width = 410,
        bd = 0,
        
        highlightthickness = 0,
        relief = "ridge"
    )




    canvas.create_image(
        205.0,
        102.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        canvas,
        #image=button_image_1,
        text='Acknowledge',
        fg='#D9D9D9',
        font=("Inter Bold",10),
        activeforeground='#D9D9D9',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print('[!] Feature to come: Delete Notification'),
        relief="flat",
        bg='#202020',
        activebackground='#202020'
    )
    button_1.place(
        x=258.0,
        y=155.0,
        width=113.0,
        height=21.0
    )

    # button_image_2 = PhotoImage(
    #     file=relative_to_assets("button_2.png"))
    # button_2 = Button(
    #     canvas,
    #     #image=button_image_2,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_2 clicked"),
    #     relief="flat",
    #     bg='#202020',
    #     activebackground='#202020'
    # )
    # button_2.place(
    #     x=132.0,
    #     y=155.0,
    #     width=113.0,
    #     height=21.0
    # )

####################
####################
####################
####################
####################

    canvas.create_text(
        24.0,
        15.0,
        anchor="nw",
        text=f"{title}",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )


    entry_bg_1 = canvas.create_image(
        218.0,
        56.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        canvas,
        bd=0,
        bg="#202020",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=160.0,
        y=48.0,
        width=116.0,
        height=14.0
    )

    entry_bg_2 = canvas.create_image(
        265.5,
        78.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        canvas,
        bd=0,
        bg="#202020",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=160.0,
        y=70.0,
        width=211.0,
        height=14.0
    )

    entry_bg_3 = canvas.create_image(
        265.5,
        116.0,
        image=entry_image_3
    )
    entry_3 = Text(
        canvas,
        bd=0,
        bg="#202020",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=160.0,
        y=92.0,
        width=211.0,
        height=46.0
    )

    canvas.create_text(
        51.0,
        48.0,
        anchor="nw",
        text=f"{field1}",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        51.0,
        70.0,
        anchor="nw",
        text=f"{field2}",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        51.0,
        92.0,
        anchor="nw",
        text=f"{field3}",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    entry_1.insert(0,f'{args[0]}')
    entry_1.config(state='disabled', disabledbackground='#202020', disabledforeground='#D9D9D9')
    entry_2.insert(0,f'{args[1]}')
    entry_2.config(state='disabled', disabledbackground='#202020', disabledforeground='#D9D9D9')
    entry_3.insert(tk.END, args[2])
    entry_3.config(state='disabled',fg='#D9D9D9')
    canvas.pack(pady=12)


