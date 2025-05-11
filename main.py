import tkinter as tk
from tkinter import messagebox
from math import pow, gcd

def find_fraction():
    try:
        num = float(entry_num.get())
        kor = int(entry_kor.get())
        max_drop_chisl = int(entry_max_chisl.get())
        max_drop_znam = int(entry_max_znam.get())

        kornl = pow(num, 1 / kor)
        chisl = 0
        znamen = 1
        pogr = abs(kornl - chisl / znamen)

        for i in range(1, max_drop_chisl + 1):
            for j in range(1, max_drop_znam + 1):
                if gcd(j, i) == 1:
                    a = j / i
                    error = abs(kornl - a)
                    if error < pogr:
                        pogr = error
                        chisl = j
                        znamen = i

        result_text = f"Наилучшая несократимая дробь:\n{chisl}/{znamen} ≈ {chisl / znamen:.10f}\nПогрешность: {pogr:.10f}"
        label_result.config(text=result_text)
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Окно
window = tk.Tk()
window.title("Приближение корня дробью")

tk.Label(window, text="Число:").grid(row=0, column=0)
entry_num = tk.Entry(window)
entry_num.grid(row=0, column=1)

tk.Label(window, text="Степень корня:").grid(row=1, column=0)
entry_kor = tk.Entry(window)
entry_kor.grid(row=1, column=1)

tk.Label(window, text="Макс. числитель:").grid(row=2, column=0)
entry_max_chisl = tk.Entry(window)
entry_max_chisl.grid(row=2, column=1)

tk.Label(window, text="Макс. знаменатель:").grid(row=3, column=0)
entry_max_znam = tk.Entry(window)
entry_max_znam.grid(row=3, column=1)

tk.Button(window, text="Найти дробь", command=find_fraction).grid(row=4, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="", justify="left")
label_result.grid(row=5, column=0, columnspan=2)

window.mainloop()