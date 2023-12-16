from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from lib.NavigationBar import *
from lib.comm_functions import *
from lib.db_conn import *




#window = Tk()

#window.geometry("800x500")
#window.configure(bg = "#272829")

def Account(window, account_id):
    
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/account_assets")
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
    NavBar(window,canvas)
    global image_image_1,image_image_2,image_image_3,image_image_4,image_image_5,image_image_7,image_image_8, save_btn_img
    
    
    # button_image_1 = PhotoImage(
    #     file=relative_to_assets("button_1.png"))
    # button_1 = Button(
    #     image=button_image_1,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_1 clicked"),
    #     relief="flat",
    #     bg='#212121'
    # )
    # button_1.place(
    #     x=32.9580078125,
    #     y=151.0,
    #     width=183.0416259765625,
    #     height=37.0
    # )

    # button_image_2 = PhotoImage(
    #     file=relative_to_assets("button_2.png"))
    # button_2 = Button(
    #     image=button_image_2,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_2 clicked"),
    #     relief="flat",
    #     bg='#212121'
    # )
    # button_2.place(
    #     x=32.0,
    #     y=208.0,
    #     width=183.0416259765625,
    #     height=37.0
    # )

    # button_image_3 = PhotoImage(
    #     file=relative_to_assets("button_3.png"))
    # button_3 = Button(
    #     image=button_image_3,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_3 clicked"),
    #     relief="flat",
    #     bg='#212121'
    # )
    # button_3.place(
    #     x=32.0,
    #     y=265.0,
    #     width=183.0416259765625,
    #     height=37.0
    # )

    # button_image_4 = PhotoImage(
    #     file=relative_to_assets("button_4.png"))
    # button_4 = Button(
    #     image=button_image_4,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_4 clicked"),
    #     relief="flat",
    #     bg='#212121'
    # )
    # button_4.place(
    #     x=32.89306640625,
    #     y=323.0,
    #     width=183.0416259765625,
    #     height=37.0
    # )

    # button_image_5 = PhotoImage(
    #     file=relative_to_assets("button_5.png"))
    # button_5 = Button(
    #     image=button_image_5,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_5 clicked"),
    #     relief="flat",
    #     bg='#212121'
    # )
    # button_5.place(
    #     x=32.0,
    #     y=380.0,
    #     width=183.0416259765625,
    #     height=37.0
    # )

    # canvas.create_rectangle(
    #     587.0,
    #     332.0,
    #     689.0,
    #     352.0,
    #     fill="#202020",
    #     outline="")

    # canvas.create_text(
    #     602.5087890625,
    #     338.4285583496094,
    #     anchor="nw",
    #     text="Save Changes",
    #     fill="#D9D9D9",
    #     font=("Inter Bold", 10 * -1)
    # )



    save_btn_img = PhotoImage(
        file=relative_to_assets("save_btn.png"))
    button_6 = Button(
        image=save_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: save_changes(),
        relief="flat",
        bg='#272829'
    )
    button_6.place(
        x=590.0,
        y=338.0,
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        427.0,
        185.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_bg_1.png"))
    entry_bg_1 = canvas.create_image(
        438.0,
        194.0,
        image=entry_image_1
    )
    account_id_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )

    account_id_entry.place(
        x=372.0,
        y=185.0,
        width=132.0,
        height=16.0
    )

    canvas.create_text(
        355.0,
        169.0,
        anchor="nw",
        text="Account ID",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        371.0,
        201.99998474121094,
        504.0,
        203.0,
        fill="#D9D9D9",
        outline="")

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat",
        bg='#212121'
    )
    button_6.place(
        x=453.0,
        y=167.0,
        width=50.0,
        height=17.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_2 = canvas.create_image(
        606.0,
        185.0,
        image=image_image_2
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_bg_1.png"))
    entry_bg_2 = canvas.create_image(
        610.0,
        194.0,
        image=entry_image_2
    )
    account_hold_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    account_hold_entry.place(
        x=537.0,
        y=185.0,
        width=146.0,
        height=16.0
    )

    canvas.create_text(
        534.0,
        169.0,
        anchor="nw",
        text="Account Holder",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        535.78173828125,
        201.0,
        682.6092529296875,
        202.98431396484375,
        fill="#D9D9D9",
        outline="")

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        517.0,
        238.0,
        image=image_image_3
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_bg_3.png"))
    entry_bg_3 = canvas.create_image(
        524.0,
        247.0,
        image=entry_image_3
    )
    email_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    email_entry.place(
        x=372.0,
        y=238.0,
        width=304.0,
        height=16.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_bg_2.png"))
    entry_bg_4 = canvas.create_image(
        400.0,
        300.0,
        image=entry_image_4
    )
    dd_date_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    dd_date_entry.place(
        x=372.0,
        y=291.0,
        width=56.0,
        height=16.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_bg_2.png"))
    entry_bg_5 = canvas.create_image(
        475.5,
        299.0,
        image=entry_image_5
    )
    mm_date_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    mm_date_entry.place(
        x=447.0,
        y=290.0,
        width=57.0,
        height=16.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_bg_2.png"))
    entry_bg_6 = canvas.create_image(
        552.0,
        300.0,
        image=entry_image_6
    )
    yy_date_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    yy_date_entry.place(
        x=524.0,
        y=291.0,
        width=56.0,
        height=16.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_bg_3.png"))
    entry_bg_7 = canvas.create_image(
        559.0,
        422.0,
        image=entry_image_7
    )
    acc_balance_entry = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    acc_balance_entry.place(
        x=442.0,
        y=413.0,
        width=234.0,
        height=16.0
    )

    canvas.create_text(
        355.0,
        223.0,
        anchor="nw",
        text="Email",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        370.64794921875,
        254.0,
        675.6761474609375,
        255.98431396484375,
        fill="#D9D9D9",
        outline="")

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_4 = canvas.create_image(
        517.0,
        413.0,
        image=image_image_4
    )

    canvas.create_text(
        355.0,
        398.0,
        anchor="nw",
        text="Current Balance",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        441.0,
        429.0,
        675.7510986328125,
        430.98431396484375,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        428.0,
        417.0,
        anchor="nw",
        text="$",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_5 = canvas.create_image(
        517.0,
        291.0,
        image=image_image_5
    )

    canvas.create_text(
        355.0,
        276.0,
        anchor="nw",
        text="Date of Birth  (Date/Month/Year)",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        371.0,
        307.0,
        428.0,
        308.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        446.0,
        306.0,
        503.0,
        307.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        446.0,
        307.0,
        503.0,
        308.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        523.0,
        307.0,
        580.0,
        308.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        433.0,
        295.0,
        anchor="nw",
        text="/",
        fill="#FFFFFF",
        font=("Inter Bold", 13 * -1)
    )

    canvas.create_text(
        510.0,
        294.0,
        anchor="nw",
        text="/",
        fill="#FFFFFF",
        font=("Inter Bold", 13 * -1)
    )

    canvas.create_rectangle(
        50.0,
        15.0,
        197.0,
        122.0,
        fill="#FFFFFF",
        outline="")



    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        123.0,
        68.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        516.0,
        92.0,
        image=image_image_8
        )


    def get_balance():
        query= f"select balance from accounts where account_id='{account_id}';"
        cur = db.cursor()
        cur.execute(query)
        
        return cur.fetchone()[0]


    def get_values():
        cur = db.cursor()
        cur.execute(f"select * from customers where customer_id in (select customer_id from accounts where account_id = '{account_id}')")
        return cur.fetchone()

    def add_values():
        account_data = get_values()
        # account_id_entry.insert(0,account_data[0])
        # account_id_entry.config(state="disabled", disabledbackground='#202020')
        # account_hold_entry.insert(0,'account_hold_entry')
        # email_entry.insert(0,'email_entry')
        # dd_date_entry.insert(0,'dd_date_entry')
        # mm_date_entry.insert(0,'mm_date_entry')
        # yy_date_entry.insert(0,'yy_date_entry')
        # acc_balance_entry.insert(0,'acc_balance_entry')
        import pyperclip

        placeholder(account_id_entry, account_id)
        account_id_entry.config(state="disabled", disabledbackground='#202020', disabledforeground='#D9D9D9')
        account_id_entry.bind('<Button-1>', lambda x:pyperclip.copy(account_id))
        placeholder(acc_balance_entry, get_balance())
        acc_balance_entry.config(state="disabled", disabledbackground='#202020', disabledforeground='#D9D9D9')
        placeholder(account_hold_entry, account_data[1])
        placeholder(email_entry, account_data[2])
        placeholder(dd_date_entry, account_data[3].strftime('%d'))
        placeholder(mm_date_entry, account_data[3].strftime('%m'))
        placeholder(yy_date_entry, account_data[3].strftime('%Y'))
        


    def save_changes():
        query_name = f'update customers set name="{account_hold_entry.get()}" where customer_id in (select customer_id from accounts where account_id = "{account_id}")'
        query_email = f'update customers set email="{email_entry.get()}" where customer_id in (select customer_id from accounts where account_id = "{account_id}")' 
        query_dob = f'update customers set dob="{yy_date_entry.get()}-{mm_date_entry.get()}-{dd_date_entry.get()}" where customer_id in (select customer_id from accounts where account_id = "{account_id}")' 
        cur = db.cursor()
        for i in [query_name,query_dob,query_email]:
            cur.execute(i)
        db.commit()
            

    add_values()