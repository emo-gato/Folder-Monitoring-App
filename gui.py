from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mirun\Downloads\practica\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        display_folder_contents(folder_selected)


def display_folder_contents(folder_path):
    contents = os.listdir(folder_path)
    # Clear previous folder contents
    for widget in display_frame.winfo_children():
        widget.destroy()
    # Display folder contents
    for idx, item in enumerate(contents):
        item_label = Label(display_frame, text=item, bg="#FFFFFF", fg="#000000", font=("PlusJakartaSansRoman", 14), anchor='w')
        item_label.pack(anchor='nw')


window = Tk()

window.geometry("928x612")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=612,
    width=928,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    220.0,
    0.0,
    928.0,
    612.0,
    fill="#FFFFFF",
    outline=""
)

canvas.create_rectangle(
    0.0,
    0.0,
    220.0,
    612.0,
    fill="#000000",
    outline=""
)

canvas.create_text(
    248.0,
    39.0,
    anchor="nw",
    text="Folder Monitoring App",
    fill="#000000",
    font=("PlusJakartaSansRoman SemiBold", 33 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=20.0,
    y=280.0,
    width=187.29383850097656,
    height=51.49781799316406
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=20.0,
    y=376.0,
    width=187.29383850097656,
    height=51.49781799316406
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=select_folder,
    relief="flat"
)
button_3.place(
    x=20.0,
    y=185.0,
    width=187.29383850097656,
    height=51.49781799316406
)

display_frame = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=680,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
display_frame.place(x=248, y=100)

window.resizable(False, False)
window.mainloop()
