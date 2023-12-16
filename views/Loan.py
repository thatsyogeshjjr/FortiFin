from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from lib.NavigationBar import NavBar
from lib.db_conn import *
import lib.comm_functions as comm
import datetime
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/loan_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




def Loan(window, account_id):
    global image_image_1, image_image_2,image_image_3,image_image_4,image_image_5, button_image_1,image_image_21
    canvas = Canvas(
        window,
        bg = "#272829",
        height = 500,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    NavBar(window, canvas)
    image_image_7 = PhotoImage(file=relative_to_assets('../login_assets/logo.png'))
    image_7 = canvas.create_image(
        123.0,
        68.0,
        image=image_image_7
    )
    image_image_21 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_2 = canvas.create_image(
        123.0,
        68.0,
        image=image_image_21
    )
    

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        552.0,
        150.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        560.6971435546875,
        159.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#202020",
        fg="#d9d9d9",
        highlightthickness=0
    )
    entry_1.place(
        x=379.30322265625,
        y=150.0,
        width=362.787841796875,
        height=16.0
    )

    canvas.create_text(
        358.0,
        135.0,
        anchor="nw",
        text="I work for / at",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        413.091064453125,
        166.99998474121094,
        742.091064453125,
        168.0,
        fill="#D9D9D9",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        674.0,
        202.0,
        image=image_image_2
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        692.0,
        211.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#202020",
        fg="#d9d9d9",
        highlightthickness=0
    )
    entry_2.place(
        x=633.0,
        y=202.0,
        width=118.0,
        height=16.0
    )

    canvas.create_text(
        602.0,
        186.0,
        anchor="nw",
        text="Requesting amount",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        632.0,
        219.0,
        751.0,
        220.00001525878906,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        347.0,
        181.0,
        555.0,
        226.0,
        fill="#202020",
        outline="")

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        455.232666015625,
        212.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#202020",
        fg="#d9d9d9",
        highlightthickness=0
    )
    entry_3.place(
        x=363.32568359375,
        y=203.0,
        width=183.81396484375,
        height=16.0
    )

    canvas.create_text(
        353.04638671875,
        188.0,
        anchor="nw",
        text="Email",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        451.0,
        203.0,
        image=image_image_3
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        435.0,
        212.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#202020",
        fg="#d9d9d9",
        highlightthickness=0
    )
    entry_4.place(
        x=363.0,
        y=203.0,
        width=144.0,
        height=16.0
    )

    canvas.create_text(
        353.04638671875,
        188.0,
        anchor="nw",
        text="Work Experience",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        362.112548828125,
        219.0,
        506.846923828125,
        220.93695068359375,
        fill="#D9D9D9",
        outline="")



    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: grant_loan(),
        relief="flat",
        bg='#272829',
        activebackground='#272829',
    )
    button_1.place(
        x=413.0,
        y=383.0,
        width=220.0,
        height=29.0
    )

    canvas.create_text(
        602.0,
        204.0,
        anchor="nw",
        text="$",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        552.0,
        256.0,
        image=image_image_4
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        595.4852294921875,
        265.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#202020",
        fg="#d9d9d9",
        highlightthickness=0
    )
    entry_5.place(
        x=448.879150390625,
        y=256.0,
        width=293.212158203125,
        height=16.0
    )

    canvas.create_text(
        358.468505859375,
        238.0,
        anchor="nw",
        text="Monthly (in-hand) salary",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        447.879150390625,
        273.0,
        742.09130859375,
        274.00001525878906,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        364.0,
        258.0,
        anchor="nw",
        text="$",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        552.0,
        310.0,
        image=image_image_5
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        595.4852294921875,
        319.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#202020",
        fg="#d9d9d9",
        highlightthickness=0
    )
    entry_6.place(
        x=448.879150390625,
        y=310.0,
        width=293.212158203125,
        height=16.0
    )

    canvas.create_text(
        358.468505859375,
        292.0,
        anchor="nw",
        text="Existing EMI (if any)",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        447.879150390625,
        327.0,
        742.09130859375,
        328.00001525878906,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        364.0,
        312.0,
        anchor="nw",
        text="$",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
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
        text="Get a Loan",
        fill="#FFFFFF",
        font=("Inter Bold", 31 * -1)
    )

    canvas.create_text(
        514.0,
        206.0,
        anchor="nw",
        text="years",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )


    def grant_loan():
        # I'm quite glad finally someone took time to read this.
        # Due to time constrainsts the loan repayment was not
        # programmed. So enjoy your loans. ~ with love, developer Yogesh (●'◡'●)
        amt = float(entry_2.get())
        q = f'update accounts set balance=balance+{amt} where account_id = "{account_id}";'
        cur = db.cursor()
        cur.execute(q)
        loan_id = comm.gen_id(6)
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days=69)
        q = f'insert into loans values("{loan_id}", "{account_id}", "NOTYPE", {amt}, 12, "{start_date.strftime("%Y-%m-%d")}", "{end_date.strftime("%Y-%m-%d")}")'
        cur.execute(q)

        q = f'insert into notifications values("{comm.gen_id(6)}", "{account_id}", "loan", "{loan_id}###{amt}###Loan was granted.", NULL,1)'
        cur.execute(q)
        
        db.commit()
        messagebox.showinfo(title='Loan granted', message=f'Loan of amt {amt} was granted to {account_id}' )