from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from lib.comm_functions import *
from lib.auth import *

from views.SignUp import SignUp
from views.Account import Account

OUTPUT_PATH = Path(__file__).parent
LOGIN_ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\login_assets")


'''
Developer Notes:
* To get rid of the 'push-down effect' on tkinter button use activebackground property in Button

'''

def relative_to_assets(path: str) -> Path:
    return LOGIN_ASSETS_PATH / Path(path)

def new_here():
    # window.destroy()
    for widget in window.winfo_children():
        widget.destroy()
    SignUp(window)
    
window = Tk()

window.geometry("800x500")
window.configure(bg = "#272829")
window.title('FortiFin: The Banking Application')

def submit_clicked():
    # with open('assets/data.txt', 'r') as datafile:
    #         Account(window, datafile.read())
    id = auth(uname=id_field.get(), pword=pass_field.get())
    if id == 0 or id == None:
        print('[-] Wrong username or password')
        canvas.create_text(
            460,345,
            text="*Can’t login. Bad email/pass",
            font=('Inter Bold', 8,),
            fill='#B14646',
            state='normal'
            )

    else:
        Account(window, id)
        # save id to file
        with open('assets/data.txt', 'w') as datafile:
            datafile.write(id)
    

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

button_image_1 = PhotoImage(
    file=relative_to_assets("new_btn.png"))
new_btn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    highlightbackground="#272829", 
    highlightcolor="#272829",
    relief="flat",
    cursor='hand2',
    activebackground='#272829',
    command=lambda: new_here(),
)


new_btn.place(
    x=255.0,
    y=339.0,
    width=82.0,
    height=23.0
)

canvas.create_rectangle(
    261.0,
    289.0,
    545.0,
    334.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    261.0,
    230.0,
    545.0,
    275.0,
    fill="#202020",
    outline="")


canvas.create_text(
 460,345,
 text="*Can’t login. Bad email/pass",
 font=('Inter Bold', 8,),
 fill='#B14646',
 state='hidden'
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("id_field.png"))
entry_bg_1 = canvas.create_image(
    408.5,
    261.0,
    image=entry_image_1
)
id_field = Entry(
    bd=0,
    bg="#202020",
    fg="#D9D9D9",
    highlightthickness=0,
    font=("Inter", 10),
)
id_field.place(
    x=283.0,
    y=252.0,
    width=251.0,
    height=16.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("pass_field.png"))
entry_bg_2 = canvas.create_image(
    408.5,
    320.0,
    image=entry_image_2
)
pass_field = Entry(
    bd=0,
    bg="#202020",
    fg="#D9D9D9",
    highlightthickness=0,
    font=("Inter", 10),
)
pass_field.place(
    x=283.0,
    y=311.0,
    width=251.0,
    height=16.0
)

canvas.create_text(
    271.0,
    236.0,
    anchor="nw",
    text="Acc. ID or Email",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    271.0,
    296.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

canvas.create_rectangle(
    282.0,
    268.0,
    534.0000610351562,
    269.98431396484375,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    282.0,
    328.0,
    534.0000610351562,
    329.98431396484375,
    fill="#D9D9D9",
    outline="")

logo_img = PhotoImage(
    file=relative_to_assets("logo.png"))
image_1 = canvas.create_image(
    410.0,
    140.0,
    image=logo_img
)


button_image_2 = PhotoImage(
    file=relative_to_assets("submit_btn.png"))
submit_btn = Button(
    image=button_image_2,
    borderwidth=0,
    background="#272829",
    highlightthickness=0,
    relief="flat",
    command=lambda: submit_clicked(),
    activebackground='#272829'
)
submit_btn.place(
    x=435.0,
    y=370.0,
    width=110.0,
    height=43.0
)


id_field.focus()


window.resizable(False, False)
window.mainloop()
