from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image
import os

root = Tk()
root.title("QRCode Generator")
root.geometry("400x550")

canvas = Canvas(root, width=400, height=550)
canvas.pack()

app_label = Label(root, text="QRCode Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="ชื่อไฟล์ QR Code (ไม่ต้องใส่ .png)")
canvas.create_window(200, 100, window=name_label)

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)

link_label = Label(root, text="URL ที่จะสร้าง QR")
canvas.create_window(200, 170, window=link_label)

link_entry = Entry(root, width=35)
canvas.create_window(200, 200, window=link_entry)

qr_image_label = None

def generate_qr():
    global qr_image_label
    name = name_entry.get().strip()
    link = link_entry.get().strip()

    if name and link:
        filename = f"{name}.png"
        qr = pyqrcode.create(link)  # ← แก้ตรงนี้
        qr.png(filename, scale=6)
        image = Image.open(filename).resize((200, 200))
        qr_image = ImageTk.PhotoImage(image)

        if qr_image_label:
            canvas.delete(qr_image_label)

        qr_image_label = canvas.create_image(200, 400, image=qr_image)
        canvas.image = qr_image  # ต้องเก็บไว้ไม่ให้ garbage collected

button = Button(text="สร้างคิวอาร์โค้ด", command=generate_qr)
canvas.create_window(200, 250, window=button)

link_entry.insert(0, "https://www.youtube.com/watch?v=MoLODKZ1zb4")

root.mainloop()

