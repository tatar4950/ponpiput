import tkinter as tk

def countdown(time_left):
    if time_left > 0:
        label.config(text=str(time_left))
        root.after(1000, countdown, time_left - 1)
    else:

        label.config(text=
                     "ชื่อ - นามสกุล: พรพิพัฒน์ ตั้งวิโรจนกุล\n"
                     "ชื่อเล่น: ตาต้า\n"
                     "ห้องเรียน: ม.5/8\n"
                     "แผนการเรียน: วิทย์-คณิต\n"
                     "อยากเรียนคณะ: สาธารณสุขศาสตร์")

root = tk.Tk()
root.title("โปรแกรมนับเวลาถอยหลัง")

label = tk.Label(root, text="", font=("Arial", 20))
label.pack(pady=20)

countdown(10)

root.mainloop()