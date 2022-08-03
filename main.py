import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import serial
import fonctions as f
from PIL import Image, ImageTk

#create object to view objects
root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

#base font and variables
font = ("Futura", 12)
serial_port = tk.StringVar()

#attributes of the window
root.title('Banc de test cartes de flash v0.1')
root.geometry('600x400+100+50')

#Importation de l'image avec PIL et conversion
im = Image.open('logo-batconnect-vertical(1).png')
logo = ImageTk.PhotoImage(im, master=root)

#Création du canevas et affichage de l'image
dessin = tk.Canvas(root, width = im.size[0], height = im.size[1])
logo1 = dessin.create_image(0,0, anchor = tk.NW, image = logo)
dessin.grid()

#ajout du logo batconnect à la fenêtre
root.iconbitmap("logo-batconnect-vertical_1_.ico")

# place labels and buttons on the root window
ttk.Label(root, text="Application de Banc de test pour tracker et batterie", font=("Futura", 14)).grid(row=0,column=0, columnspan=2, ipady=10, sticky=tk.NS)

ttk.Label(root, text="Choisir Mode", font=font).grid(row=1, column=0)
mode = tk.StringVar(value=("Mode Supervision", "Mode Simulation"))
mode = tk.Listbox(root, listvariable=mode, height=2, selectmode='browse').grid(row=1, column=1, pady=30)

ttk.Label(root, text="Port Serial", font=font).grid(row=2, column=0, pady=30)
textbox = ttk.Entry(root, textvariable=serial_port).grid(row=2, column=1)
ttk.Button(root, text="Se Connecter", command=lambda : f.connect(serial_port.get())).grid(row=3, column=0, columnspan=2, pady=30)


ttk.Label(root, text="Andrea Pérez Fernández, Léa Scheer - 2022", font=("Futura", 8)).grid(column=0, row=4, pady=40, sticky=tk.SW)


#f.read_serial()
#Maintain window open

root.mainloop()
