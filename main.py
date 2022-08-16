'''
GUI Application
Andrea Pérez Fernandez
Based on : https://github.com/pratikguru/Instructables/blob/master/uart_visualizer.py
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import serial
from PIL import Image
from PIL import ImageTk

import threading
import time
import os


# Global variables
serial_data = ''
filter_data = ''
update_period = 5
serial_object = None
root = tk.Tk()
new_data = False



#font
font = ("Futura", 12)

#function definition
def connect():
    global serial_object
    port = port_entry.get()
    baud = baud_entry.get()

    try:
        try:
            serial_object = serial.Serial('/dev/tty' + str(port), baud, rtscts=False, dsrdtr=False)
            # print info about port connection
            Label(root, text="Connected", fg='green').place(x=870, y=220)
        except:
            print("Cant Open Specified Port")
    except ValueError:
        print("Enter Baud and Port")
        return


    t1.start()


def disconnect():
    return 1

def send():
    send_data = data_entry.get()
    line = "\n"
    send_data += line
    #print(send_data)

    if not send_data:
        Label(root, text="No data to send", fg='red').place(x=600, y=532)

    serial_object.write(send_data.encode())
    print(send_data.encode('ascii'))
    a = 0


def update_gui():
    global filter_data
    global update_period
    global new_data

    st.place(x=25, y=260)
    new = time.time()



    while(1):
        if new_data:
            st.insert(END, filter_data)
            new_data = False


def get_data():
    """This function serves the purpose of collecting data from the serial object and storing
    the filtered data into a global variable.
    The function has been put into a thread since the serial event is a blocking function.
    """
    global serial_object
    global filter_data
    global serial_data
    global new_data

    while (1):
        try:
            if serial_object.in_waiting > 0:
                serial_data = serial_object.readline()
                print(serial_data)
                filter_data = serial_data.decode('ascii')
                new_data = True
                Label(root, text="Getting data", fg='green').place(x=600, y=220)

        except TypeError:
            Label(root, text="ERROR", fg='red').place(x=600, y=220)
            pass


if __name__ == "__main__":

    # Window configuration
    root.title('Banc de test cartes de flash v0.1')



    #frames
    frame_banner = tk.Frame(height=185, width=970, bd=3, relief='groove').place(x=15, y=5)
    frame_data = tk.Frame(height=400, width=970, bd=3, relief='groove').place(x=15, y=200)
    frame_input = tk.Frame(height=150, width=970, bd=3, relief='groove').place(x=15, y=615)
    st = ScrolledText(root, width=116,  height=14)

    t1 = threading.Thread(target=get_data)
    t1.daemon = True

    t2 = threading.Thread(target = update_gui)
    t2.daemon = True
    t2.start()

    #banner
    im = Image.open('./assets/logo-batconnect-vertical(1).png')
    logo = ImageTk.PhotoImage(im, master=root)
    dessin = tk.Canvas(root, width = im.size[0], height = im.size[1])
    logo1 = dessin.create_image(0,0, anchor = tk.NW, image = logo)
    dessin.place(x=30, y=18)
    ttk.Label(root, text="Application de Banc de test pour tracker et batterie", font=("Futura", 14)).place(x=300, y=70)
    ttk.Label(root, text="Batconnect - 2022", font=("Futura", 10)).place(x=480, y=100)

    #input
    ttk.Label(root, text="Connect to Testbench", font=font).place(x=25, y=625)
    connect = ttk.Button(root, text="Connect", command=connect).place(x=435, y=670)
    disconnect = ttk.Button(text="Disconnect", command=disconnect).place(x=435, y=720)
    ttk.Label(root, text="Port", font=("Futura", 10)).place(x=25, y=671)
    port_entry = Entry(width=7)
    port_entry.place(x=65, y=670)
    baud_entry = Entry(width=7)
    baud_entry.place(x=270, y=670)
    ttk.Label(root, text="Baudrate", font=("Futura", 10)).place(x=200, y=671)

    #ouput
    ttk.Label(root, text="Debug Information", font=font).place(x=25, y=220)
    button1 = ttk.Button(root, text="Send", command=send, width=6).place(x=485, y=530)
    data_entry = Entry(width=43)
    data_entry.place(x=85, y=532)

    #main loop
    root.geometry('1000x780+100+50')
    root.mainloop()

    #create object to view objects
    # root.columnconfigure(0, weight=1)
    # root.columnconfigure(1, weight=1)
    #
    # #base font and variables
    # font = ("Futura", 12)
    # serial_port = tk.StringVar()
    #
    # #attributes of the window

    # #ajout du logo batconnect à la fenêtre
    # #root.iconbitmap("logo-batconnect-vertical_1_.ico")
    #
    # # place labels and buttons on the root window
    # ttk.Label(root, text="Application de Banc de test pour tracker et batterie", font=("Futura", 14)).grid(row=0,column=0, columnspan=2, ipady=10, sticky=tk.NS)
    #
    # ttk.Label(root, text="Choisir Mode", font=font).grid(row=1, column=0)
    # mode = tk.StringVar(value=("Mode Supervision", "Mode Simulation"))
    # mode = tk.Listbox(root, listvariable=mode, height=2, selectmode='browse').grid(row=1, column=1, pady=30)
    #
    # ttk.Label(root, text="Port Serial", font=font).grid(row=2, column=0, pady=30)
    # textbox = ttk.Entry(root, textvariable=serial_port).grid(row=2, column=1)
    # ttk.Button(root, text="Se Connecter", command=lambda : f.connect(serial_port.get())).grid(row=3, column=0, columnspan=2, pady=30)
    #
    #
    # ttk.Label(root, text="Andrea Pérez Fernández, Léa Scheer - 2022", font=("Futura", 8)).grid(column=0, row=4, pady=40, sticky=tk.SW)
    #
    #
    # #f.read_serial()
    # #Maintain window open
    #
    # while True:
    #     root.update()

