from tkinter import *
from pathlib import Path
from lib.win_manager import manager
#import subprocess



class NavBar:
    def __init__(self,root,canvas):
        self.master_root = root
        self.draw_navbar(canvas)

    def draw_navbar(self,canvas, account_id = 'example'):
            
        OUTPUT_PATH = Path(__file__).parent
        #NAV_ASSETS_PATH = OUTPUT_PATH / Path(r"..\new_gui\build\assets\frame0")
        #NAV_ASSETS_PATH = OUTPUT_PATH / Path(r"assets\nav_assets")
        NAV_ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/navbar_assets")
        def relative_to_assets(path: str) -> Path:
            print(NAV_ASSETS_PATH / Path(path))
            return NAV_ASSETS_PATH / Path(path)
        
        global image_image_6, button_image_10,button_image_11,button_image_7,button_image_8,button_image_9

        
        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            123.0,
            282.0,
            image=image_image_6

        )
        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: manager(self.master_root,'acc'),
            relief="flat",
            bg='#212121',
            activebackground='#212121'
        )
        button_7.place(
            x=32.9580078125,
            y=151.0,
            width=183.0416259765625,
            height=37.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: manager(self.master_root,'tran'),
            relief="flat",
            bg='#212121',
            activebackground='#212121'
        )
        button_8.place(
            x=32.0,
            y=208.0,
            width=183.0416259765625,
            height=37.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: manager(self.master_root,'netb'),
            relief="flat",
            bg='#212121',
            activebackground='#212121'
        )
        button_9.place(
            x=32.0,
            y=265.0,
            width=183.0416259765625,
            height=37.0
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: manager(self.master_root,'notif'),
            relief="flat",
            bg='#212121',
            activebackground='#212121'
        )
        button_10.place(
            x=32.89306640625,
            y=323.0,
            width=183.0416259765625,
            height=37.0
        )

        button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: manager(self.master_root,'about'),
            relief="flat",
            bg='#212121',
            activebackground='#212121'
        )
        button_11.place(
            x=32.0,
            y=380.0,
            width=183.0416259765625,
            height=37.0
        )