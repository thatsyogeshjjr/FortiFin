from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from lib.NavigationBar import NavBar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/aboutus_assets/")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

i=0

def AboutUs(window):
    global image_image_1,image_image_2,button_image_1,button_image_2,button_image_3
    names = ['Yogesh Jajoria', 'Deekshant Dhiman', 'Aryan Bhatt']
    text = [
"""
Meet the prodigious teen 
behind Fortifin, a programming 
virtuoso and visionary. 
Leading the charge, this team
lead breathed life into the project,
providing both the direction and the
spark that ignited its success.

""",
"""
In the creative realm, our maestro 
director orchestrates the Fortifin 
narrative. A beacon of creativity,
they not only lead the documentary's
direction but also weave together
its tapestry through expert editing 
and eloquent writing.
""",
"""
Beyond the code, our introverted thinker
is the silent powerhouse of Fortifin. 
A programming maestro and 
contemplative mind, they contribute 
depth and precision, bringing 
an introspective touch to the project's core.
"""]
    


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
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        123.0,
        68.0,
        image=image_image_1
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
        text="About Us",
        fill="#FFFFFF",
        font=("Inter Bold", 31 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        512.0,
        239.0,
        image=image_image_2
    )

    name = canvas.create_text(
        343.0,
        132.0,
        anchor="nw",
        text=names[i],
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: play_documentary(),
        relief="flat",
        background='#272829',
        activebackground='#272829'
    )
    button_1.place(
        x=415.0,
        y=388.0,
        width=196.0,
        height=54.0
    )

    info= canvas.create_text(
        369.0,
        167.0,
        anchor="nw",
        text=text[i],
        fill="#FFFFFF",
        font=("Inter Bold", 17 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: left_clicked(),
        relief="flat",
        background='#202020',
        activebackground='#202020'
    )
    button_2.place(
        x=316.0,
        y=221.0,
        width=38.0,
        height=37.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: right_clicked(),
        relief="flat",
        background='#202020',
        activebackground='#202020'
    )
    button_3.place(
        x=666.0,
        y=221.0,
        width=38.0,
        height=37.0
    )

    def right_clicked():
        global i
        if i+1==4:
            i=0
        else:
            i+=1
        canvas.itemconfig(name,text=names[i])
        canvas.itemconfig(info,text=text[i])
    def left_clicked():
        global i
        if i-1==-1:
            i=3
        else:i-=1
        canvas.itemconfig(name,text=names[i])
        canvas.itemconfig(info,text=text[i])


    def play_documentary():
        import os
        video_path = r"assets/FortiFin.mp4"
        os.system(f'start {video_path}')

