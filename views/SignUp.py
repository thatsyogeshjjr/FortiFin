from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
from lib.register import *
from lib.comm_functions import *
from lib.db_conn import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\signup_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("800x500")
# window.configure(bg = "#272829")


def SignUp(window):
    

    def signup_done():
        s = f'''
        e1: {fname_field.get()}
        e2: {lname_field.get()}
        e3: {email_field.get()}
        e4: {pword_field.get()}
        e5: {dd_dob_field.get()}
        e6: {mm_dob_field.get()}
        e7: {yy_dob_field.get()}

        '''
        print(s)

        register(fname = fname_field.get(),
                 lname = lname_field.get(),
                 email = email_field.get(),
                 pword = pword_field.get(),
                 date = f"{yy_dob_field.get()}-{mm_dob_field.get()}-{dd_dob_field.get()}")
        print('! signup complete')

        window.destroy()
        subprocess.run(['python','./Login.py'])
        


    global button_image_1
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
    canvas.create_text(
        92.0,
        53.0,
        anchor="nw",
        text="Sign Up",
        fill="#D8D9DA",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_rectangle(
        158.0,
        307.0,
        634.0,
        355.0,
        fill="#202020",
        outline="")

    canvas.create_text(
        110.0,
        82.0,
        anchor="nw",
        text="it’s free!",
        fill="#D8D9DA",
        font=("Inter Bold", 13 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("submit_btn.png"))
    submit_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: signup_done(),
        relief="flat",
        background='#272829',
        highlightbackground="#272829", 
        highlightcolor="#272829",
        cursor='hand2',
        activebackground='#272829',
    )
    submit_btn.place(
        x=495.0,
        y=385.0,
        width=143.0,
        height=43.0
    )

    canvas.create_text(
        176.0,
        316.0,
        anchor="nw",
        text="Date of Birth  (Date/Month/Year)",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        283.0,
        336.0,
        anchor="nw",
        text="/",
        fill="#FFFFFF",
        font=("Inter Bold", 13 * -1)
    )

    canvas.create_text(
        390.0,
        335.0,
        anchor="nw",
        text="/",
        fill="#FFFFFF",
        font=("Inter Bold", 13 * -1)
    )

    canvas.create_rectangle(
        162.0,
        253.0,
        638.0,
        301.0,
        fill="#202020",
        outline="")

    canvas.create_text(
        176.0,
        260.0,
        anchor="nw",
        text="Password",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        162.0,
        145.0,
        390.0,
        193.0,
        fill="#202020",
        outline="")

    canvas.create_rectangle(
        162.0,
        199.0,
        638.0,
        247.0,
        fill="#202020",
        outline="")

    canvas.create_text(
        176.0,
        206.0,
        anchor="nw",
        text="Email",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        410.0,
        145.0,
        638.0,
        193.0,
        fill="#202020",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("fname_field.png"))
    entry_bg_1 = canvas.create_image(
        291.0,
        177.5,
        image=entry_image_1
    )
    fname_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    fname_field.place(
        x=200.0,
        y=168.0,
        width=182.0,
        height=17.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("lname_field.png"))
    entry_bg_2 = canvas.create_image(
        539.0,
        177.5,
        image=entry_image_2
    )
    lname_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    lname_field.place(
        x=449.0,
        y=168.0,
        width=180.0,
        height=17.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("email_field.png"))
    entry_bg_3 = canvas.create_image(
        410.0,
        231.5,
        image=entry_image_3
    )
    email_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    email_field.place(
        x=200.0,
        y=222.0,
        width=420.0,
        height=17.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("pword_field.png"))
    entry_bg_4 = canvas.create_image(
        410.0,
        285.5,
        image=entry_image_4
    )
    pword_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    pword_field.place(
        x=200.0,
        y=276.0,
        width=420.0,
        height=17.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("dd_dob_field.png"))
    entry_bg_5 = canvas.create_image(
        238.5,
        341.5,
        image=entry_image_5
    )
    dd_dob_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    dd_dob_field.place(
        x=200.0,
        y=332.0,
        width=77.0,
        height=17.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("mm_dob_field.png"))
    entry_bg_6 = canvas.create_image(
        341.5,
        341.5,
        image=entry_image_6
    )
    mm_dob_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    mm_dob_field.place(
        x=303.0,
        y=332.0,
        width=77.0,
        height=17.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("yy_dob_field.png"))
    entry_bg_7 = canvas.create_image(
        449.0,
        341.5,
        image=entry_image_7
    )
    yy_dob_field = Entry(
        bd=0,
        bg="#202020",
        fg="#D9D9D9",
        highlightthickness=0
    )
    yy_dob_field.place(
        x=410.0,
        y=332.0,
        width=78.0,
        height=17.0
    )

    canvas.create_text(
        423.0,
        151.0,
        anchor="nw",
        text="Last Name",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        176.0,
        152.0,
        anchor="nw",
        text="First Name",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        199.0,
        294.0,
        620.0,
        295.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        199.0,
        186.0,
        382.0,
        187.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        448.0,
        186.0,
        629.0,
        187.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        199.0,
        240.0,
        620.0,
        241.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        409.0,
        350.0,
        488.0,
        351.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        302.0,
        350.0,
        380.0,
        351.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        199.0,
        350.0,
        277.0,
        351.00000762939453,
        fill="#FFFFFF",
        outline="")
