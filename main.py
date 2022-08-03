import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import serial
import fonctions as f


#create object to view objects
root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

#base font and variables
font = ("Futura", 12)
serial_port = tk.StringVar()

#attributes of the window
root.title('Banc de test cartes de flash v0.1')
root.geometry('600x400+100+50')


# place labels and buttons on the root window
ttk.Label(root, text="Application de Banc de test pour tracker et batterie", font=("Futura", 14)).grid(row=0,column=0, columnspan=2, ipady=10, sticky=tk.NS)

ttk.Label(root, text="Choisir Mode", font=font).grid(row=1, column=0)
mode = tk.StringVar(value=("Mode Supervision", "Mode Simulation"))
mode = tk.Listbox(root, listvariable=mode, height=2, selectmode='browse').grid(row=1, column=1, pady=30)

ttk.Label(root, text="Port Serial", font=font).grid(row=2, column=0, pady=30)
textbox = ttk.Entry(root, textvariable=serial_port).grid(row=2, column=1)
ttk.Button(root, text="Se Connecter", command=lambda : f.connect(serial_port.get())).grid(row=3, column=0, columnspan=2, pady=30)




ttk.Label(root, text="Andrea Pérez Fernández - 2022", font=("Futura", 8)).grid(column=0, row=4, pady=40, sticky=tk.SW)

#Maintain window open
root.mainloop()