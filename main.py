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

import fonctions as f

import threading
import os
import platform
import time


# Global variables
serial_data = ''
filter_data = ''
update_period = 5
serial_object = None
root = tk.Tk()
new_data = False
os_name = ""
Alive = True



#font
font = ("Futura", 12)

#function definition
def connect():
    global serial_object
    global Alive
    port = port_entry.get()
    baud = baud_entry.get()
    
    if os_name == "Linux":
        try:
            try:
                serial_object = serial.Serial('/dev/tty' + str(port), baud, rtscts=False, dsrdtr=False)
                # print info about port connection
                Label(root, text="Connected", fg='green', padx=20).place(x=870, y=220)
                if t1.ident != None:
                    Alive = True
                else :
                    t1.start()
            except:
                print("Cant Open Specified Port")

        except ValueError:
            print("Enter Baud and Port")
            return
        
    elif os_name == "Windows":
        #print("Windows")
        try:
            try:
                serial_object = serial.Serial(str(port), baud, rtscts=False, dsrdtr=False)
                # print info about port connection
                if t1.ident != None:
                    Alive = True
                else :
                    t1.start()
                Label(root, text="Connected", fg='green', padx=20).place(x=870, y=220)
            except:
                print("Cant Open Specified Port")
        except ValueError:
            print("Enter Baud and Port")
            return
    

def disconnect():
    global Alive
    #Standby on threads
    Alive = False
    try:
        serial_object.close()
        Label(root, text="Disconnected", fg='red', padx=10).place(x=870, y=220)
    except AttributeError:
        print
        "Closed without Using it -_-"
        
    #application is closed -> update to only close connection and not kill the interface
    #root.quit()

def send():
    send_data = data_entry.get()
    line = "\r"
    send_data += line
    #print(send_data)

    if not send_data:
        Label(root, text="No data to send", fg='red').place(x=600, y=532)

    serial_object.write(send_data.encode())
    #print(send_data.encode('ascii'))
    a = 0


def update_gui():
    global filter_data
    global update_period
    global new_data

    st.place(x=25, y=260)

    while(1):
        while(Alive):
            if new_data:
                st.insert(END, filter_data)
                st.see('end')
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

    while(1):
        while (Alive):
            try:
                if serial_object.in_waiting > 0:
                    serial_data = serial_object.readline()
                    #print(serial_data)
                    filter_data = serial_data.decode('ascii')
                    if f.is_spy(filter_data):
                        (id, mask) = f.info_filter(filter_data)
                        ttk.Label(root, text=id, font=("Futura", 10), background="white").place(x=630, y=671)
                        ttk.Label(root, text=mask, font=("Futura", 10), background="white").place(x=630, y=720)
                    new_data = True

            except TypeError:
                Label(root, text="ERROR", fg='red').place(x=600, y=220)
                pass

            time.sleep(0.2)

def clean():
    st.delete(1.0, END)


if __name__ == "__main__":
    
    #get operating system
    os_name = platform.system()

    # Window configuration
    root.title('Banc de test cartes de flash v0.1')

    #frames
    frame_banner = tk.Frame(height=185, width=970, bd=3, relief='groove').place(x=15, y=5)
    frame_data = tk.Frame(height=400, width=970, bd=3, relief='groove').place(x=15, y=200)
    frame_input = tk.Frame(height=150, width=480, bd=3, relief='groove').place(x=15, y=615)
    frame_filter = tk.Frame(height=150, width=480, bd=3, relief='groove').place(x=505, y=615) 
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
    dessin.place(x=30, y=17)
    ttk.Label(root, text="Application de Banc de test pour tracker et batterie", font=("Futura", 14)).place(x=300, y=70)
    ttk.Label(root, text="Batconnect - 2022", font=("Futura", 10)).place(x=480, y=100)

    #input
    ttk.Label(root, text="Connect to Testbench", font=font).place(x=25, y=625)
    connect = ttk.Button(root, text="Connect", command=connect).place(x=380, y=670)
    disconnect = ttk.Button(text="Disconnect", command=disconnect).place(x=380, y=720)
    ttk.Label(root, text="Port :", font=("Futura", 10)).place(x=25, y=671)
    port_entry = Entry(width=7)
    port_entry.place(x=65, y=670)
    ttk.Label(root, text="Baudrate :", font=("Futura", 10)).place(x=170, y=671)
    baud_entry = Entry(width=7)
    baud_entry.place(x=250, y=670)

    #ouput
    ttk.Label(root, text="Debug Information", font=font).place(x=25, y=220)
    button1 = ttk.Button(root, text="Send", command=send, width=6).place(x=485, y=530)
    data_entry = Entry(width=43)
    data_entry.place(x=85, y=532)
    ttk.Button(root, text="Clean", command=clean, width=6).place(x=750, y=530)

    #filter information
    ttk.Label(root, text="CAN Filter Configuration", font=font).place(x=525, y=625)
    ttk.Label(root, text="Filter ID", font=("Futura", 10)).place(x=525, y=671)
    ttk.Label(root, text="Filter Mask", font=("Futura", 10)).place(x=525, y=720)

    #main loop
    root.geometry('1000x780+100+50')
    root.mainloop()
