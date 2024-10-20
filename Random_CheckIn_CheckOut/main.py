import pandas as pd
import random
import string
import tkinter as tk
from tkinter import filedialog

def generate_random_string(length=6):
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

hari_awal = int(input("Masukkan hari awal: "))
hari_akhir = int(input("Masukkan hari akhir: "))

data = []

for hari in range(hari_awal, hari_akhir + 1):
    check_in = generate_random_string()
    check_out = generate_random_string()
    data.append([f"Day {hari}", check_in, check_out])

df = pd.DataFrame(data, columns=['Hari', 'Check In', 'Check Out'])

root = tk.Tk()
root.withdraw()

root.attributes("-topmost", True)

file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])

root.attributes("-topmost", False)

if file_path:
    df.to_excel(file_path, index=False)
    print(f"Data berhasil disimpan ke dalam '{file_path}'")
else:
    print("Penyimpanan file dibatalkan.")