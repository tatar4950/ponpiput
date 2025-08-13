import tkinter as tk

def calculate_area():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        area = 0.5 * base * height
        label_result.config(text=f"พื้นที่สามเหลี่ยม: {area:.2f}")
    except ValueError:
        label_result.config(text="กรุณากรอกตัวเลขเท่านั้น")

root = tk.Tk()
root.title("คำนวณพื้นที่สามเหลี่ยม")

tk.Label(root, text="ฐาน:").grid(row=0, column=0)
entry_base = tk.Entry(root)
entry_base.grid(row=0, column=1)

tk.Label(root, text="สูง:").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

btn_calculate = tk.Button(root, text="คำนวณ", command=calculate_area)
btn_calculate.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()