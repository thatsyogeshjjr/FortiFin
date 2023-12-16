from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def BaseNotif(frame, title, field1, field2, field3): 
    OUTPUT_PATH = Path(__file__).parent
    BASE_NOTIF_ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/notification_assets")


    def relative_to_assets(path: str) -> Path:
        return BASE_NOTIF_ASSETS_PATH / Path(path)

    canvas = Canvas(
        frame,
        bg = "#FFFFFF",
        height = 205,
        width = 410,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        205.0,
        102.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=258.0,
        y=155.0,
        width=113.0,
        height=21.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=132.0,
        y=155.0,
        width=113.0,
        height=21.0
    )
################################
################################
################################
################################
################################
################################
################################
    canvas.create_text(
        24.0,
        0.0,
        anchor="nw",
        text="Regarding EMI",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        218.0,
        56.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        frame,
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

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        265.5,
        78.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        frame,
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

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        265.5,
        116.0,
        image=entry_image_3
    )
    entry_3 = Text(
        frame,
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
        text=f"{title}",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        51.0,
        70.0,
        anchor="nw",
        text="Amount",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        51.0,
        92.0,
        anchor="nw",
        text="Message",
        fill="#51C926",
        font=("Inter Bold", 12 * -1)
    )

