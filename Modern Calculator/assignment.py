import tkinter as tk

def on_button_click(value):
    current = display.get()
    if value == "=":
        try:
            result = str(eval(current))
            display.set(result)
        except Exception:
            display.set("Error")
    elif value == "C":
        display.set("")
    else:
        display.set(current + value)


root = tk.Tk()
root.title("modern Calculator")
root.geometry("360x600")
root.configure(bg="#1c1c1c") 

display = tk.StringVar()


entry = tk.Entry(root, textvariable=display, font=("Helvetica", 40), bg="#1c1c1c", fg="white", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=20)


buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
]


for (text, row, col) in buttons:
    button = tk.Button(
        root, 
        text=text, 
        font=("Helvetica", 24), 
        bg="#333333", 
        fg="white", 
        bd=0, 
        relief="flat", 
        command=lambda value=text: on_button_click(value),
        height=2,
        width=5
    )
    button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
    

equals_button = tk.Button(
    root, 
    text="=", 
    font=("Helvetica", 24), 
    bg="#FF9500", 
    fg="white", 
    bd=0, 
    relief="flat", 
    command=lambda value="=": on_button_click(value),
    height=2,
    width=5
)
equals_button.grid(row=5, column=2, sticky="nsew", padx=10, pady=10)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
