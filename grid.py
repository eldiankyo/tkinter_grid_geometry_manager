import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x100')
root.resizable(0, 0)
root.title('Grid Login')
root.configure(bg='#d9d9d9')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

username_label = ttk.Label(root, text='Username:')
username_label.grid(column=0, row=0, sticky='w', padx=5, pady=5)
username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky='ew', padx=5, pady=5)

password_label = ttk.Label(root, text='Password:')
password_label.grid(column=0, row=1, sticky='w', padx=5, pady=5)
password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=1, sticky='ew', padx=5, pady=5)

login_button = ttk.Button(root, text='Login')
login_button.grid(column=1, row=2, sticky="e", padx=5, pady=5)

root.mainloop()