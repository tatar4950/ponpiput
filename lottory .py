import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


def fetch_lottery():
    """ดึงข้อมูลผลสลากจากเว็บ lottery.co.th"""
    try:
        r = requests.get('https://www.lottery.co.th/small')
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text(separator='|').split('|')

        info = {}
        for token in text:
            token = token.strip()
            if 'รางวัลที่ 1' in token:
                info['first'] = token.split('รางวัลที่ 1')[-1].strip()
            elif 'เลขท้าย 2 ตัว' in token:
                info['last2'] = token.split('เลขท้าย 2 ตัว')[-1].strip()
            elif 'เลขหน้า 3 ตัว' in token:
                info['front3'] = token.split('เลขหน้า 3 ตัว')[-1].strip()
            elif 'เลขท้าย 3 ตัว' in token:
                info['back3'] = token.split('เลขท้าย 3 ตัว')[-1].strip()
        return info
    except Exception as e:
        messagebox.showerror("Error", f"ไม่สามารถดึงข้อมูลได้\n{e}")
        return {}


def refresh():
    """อัปเดตผลลอตเตอรี่บน GUI"""
    info = fetch_lottery()
    for key, label in labels.items():
        label.config(text=f"{label_names[key]}: {info.get(key, 'N/A')}")


root = tk.Tk()
root.title("ผลสลากกินแบ่งรัฐบาล (แบบย่อ)")
root.geometry("400x300")
root.configure(bg="#f5f5f5")

title_lbl = tk.Label(root, text="📌 ผลสลากกินแบ่งรัฐบาล", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="blue")
title_lbl.pack(pady=10)

label_names = {
    'first': 'รางวัลที่ 1',
    'last2': 'เลขท้าย 2 ตัว',
    'front3': 'เลขหน้า 3 ตัว',
    'back3': 'เลขท้าย 3 ตัว'
}

labels = {}
for key in label_names:
    lbl = tk.Label(root, text=f"{label_names[key]}: ...", font=("Arial", 16), bg="#f5f5f5")
    lbl.pack(pady=5)
    labels[key] = lbl

btn = tk.Button(root, text="โหลดข้อมูล / Refresh", command=refresh, font=("Arial", 14), bg="green", fg="white")
btn.pack(pady=15)

refresh()
