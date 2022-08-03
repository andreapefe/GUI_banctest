import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import serial

font = ("Futura", 12)

def connect(input):
    popup = tk.Tk()
    popup.title('Banc de test cartes de flash v0.1')
    popup.geometry('600x400+100+50')

    ttk.Label(popup, text="Connect to port {0}".format(input)).pack()

#fonctions attached
# def click() :
#     scroll = tk.Tk()
#     st = ScrolledText(popup, width=50, height=10)
#     st.grid(column=0, row=0)
#     for i in range(0,10):
#         st.insert('{0}.0'.format(i), 'Try numero {0}\n'.format(i))
#     print('Clicked')



#ouverture du port série
def read_serial(port):

    port_serie = serial.Serial(port = port, baudrate = 9600)
    print(port_serie.readline())
   # port_serie.close()
