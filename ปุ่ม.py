import tkinter as tk

def show_info():
    label_result.config(text="ชื่อ : พรพิพัฒน์ ตั้งวิโรจน์กุล\nชั้น : ม.5/8\nเลขที่ : 3")

root = tk.Tk()
root.title("โปรแกรมแสดงข้อมูล")
root.geometry("300x200")

btn_show = tk.Button(root, text="แสดงข้อมูล", command=show_info)
btn_show.pack(pady=10)

label_result = tk.Label(root, text="", font=("TH Sarabun New", 14))
label_result.pack(pady=10)

root.mainloop()