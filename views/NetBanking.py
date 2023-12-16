from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from lib.NavigationBar import NavBar
import lib.transact 
from views.Loan import Loan
from lib.db_conn import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/netbank_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def NetBanking(window, account_id):
    global image_image_1, image_image_2, image_image_3,image_image_4, button_image_1, button_image_2,image_image_21
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
    NavBar(window,canvas)

    button_image_1 = PhotoImage(
        file=relative_to_assets("transfer_btn.png"))
    transfer_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transaction(),
        relief="flat",
        bg='#272829',
        activebackground='#272829'
    )
    transfer_btn.place(
        x=554.0,
        y=255.0,
        width=137.0,
        height=29.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        429.0,
        150.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("acc_entry.png"))
    entry_bg_1 = canvas.create_image(
        433.0,
        159.0,
        image=entry_image_1
    )
    acc_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0,
    )
    acc_entry.place(
        x=365.0,
        y=150.0,
        width=146.0,
        height=16.0
    )

    canvas.create_text(
        357.0,
        134.0,
        anchor="nw",
        text="Account ID / Email",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        373.0,
        166.99998474121094,
        506.0,
        168.0,
        fill="#D9D9D9",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        608.0,
        150.0,
        image=image_image_2
    )

    image_image_21 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_2 = canvas.create_image(
        123.0,
        68.0,
        image=image_image_21
    )



    entry_image_2 = PhotoImage(
        file=relative_to_assets("amt_entry.png"))
    entry_bg_2 = canvas.create_image(
        626.0,
        159.0,
        image=entry_image_2
    )
    amt_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    amt_entry.place(
        x=567.0,
        y=150.0,
        width=118.0,
        height=16.0
    )

    canvas.create_text(
        536.0,
        134.0,
        anchor="nw",
        text="Amount",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        566.0,
        167.0,
        685.0,
        168.00000762939453,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        347.0,
        181.0,
        691.0,
        226.0,
        fill="#202020",
        outline="")

    entry_image_3 = PhotoImage(
        file=relative_to_assets("msg_entry.png"))
    entry_bg_3 = canvas.create_image(
        526.0,
        212.0,
        image=entry_image_3
    )
    msg_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    msg_entry.place(
        x=374.0,
        y=203.0,
        width=304.0,
        height=16.0
    )

    canvas.create_text(
        357.0,
        188.0,
        anchor="nw",
        text="Email",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        519.0,
        203.0,
        image=image_image_3
    )


    canvas.create_text(
        357.0,
        188.0,
        anchor="nw",
        text="Message",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        372.64794921875,
        219.0,
        677.67626953125,
        220.98431396484375,
        fill="#D9D9D9",
        outline="")



    funds_err = canvas.create_text(
        350.0,
        243.0,
        anchor="nw",
        text="*Funds not enough",
        fill="#B14646",
        font=("Inter Bold", 12 * -1),
    )
    canvas.itemconfigure(funds_err,state='hidden')
    

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        518.0,
        370.0,
        image=image_image_4
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("loan_btn.png"))
    loan_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_loan_application(),
        relief="flat",
        bg='#202020',
        activebackground='#202020'
    )
    loan_btn.place(
        x=409.0,
        y=357.0,
        width=220.0,
        height=29.0
    )

    canvas.create_text(
        536.0,
        152.0,
        anchor="nw",
        text="$",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        346.0,
        299.0,
        691.0,
        300.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        302.0,
        84.0,
        647.0,
        85.0,
        fill="#D9D9D9",
        outline="")
    

    canvas.create_text(
        303.0,
        39.0,
        anchor="nw",
        text="Net Banking",
        fill="#FFFFFF",
        font=("Inter Bold", 31 * -1)
    )




    def transaction():
        q = f'select balance from accounts where account_id="{account_id}";'
        cur = db.cursor()
        cur.execute(q)
        acc_balance = cur.fetchall()[0][0]
        recepient_id = acc_entry.get()
        #print(f'\n\n\n\n\n{acc_balance}')
        
        if acc_balance < float(amt_entry.get()) :
            canvas.itemconfigure(funds_err,state='normal')
        else:
            if '@' in acc_entry.get():
                query = f'select account_id from accounts where customer_id in (select customer_id from customers where email="{acc_entry.get()}");'
                cur.execute(query)
                print(query)
                recepient_id = cur.fetchone()[0]
                print(recepient_id)
            lib.transact.main(account_id, recepient_id,float(amt_entry.get()))



    def open_loan_application():
        for widget in window.winfo_children():
            widget.destroy()

        Loan(window,account_id)
