import "qrcode"
import tkinter as tk
from tkinter import messagebox


def generate_qr():
    text = entry.get()
    if text.strip() == "":
        messagebox.showwarning("คำเตือน", "กรุณากรอกข้อความก่อนสร้าง QR Code")
    else:
        img = "qrcode".make(text)
        img.save("qrcode.png")
        messagebox.showinfo("สำเร็จ", "สร้าง QR Code เรียบร้อยแล้ว (บันทึกเป็น qrcode.png)")

root = tk.Tk()
root.title("แอพสร้าง QR Code")

label = tk.Label(root, text="กรอกข้อความที่ต้องการสร้าง QR Code:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="สร้าง QR Code", command=generate_qr)
btn.pack(pady=10)

root.mainloop()
