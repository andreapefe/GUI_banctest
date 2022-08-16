import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import serial


font_port = ("Courier", 10)
out = 0

#reference : https://www.youtube.com/watch?v=-SoEHsNKVpw

def connect(input):
    # popup = tk.Tk()
    # popup.title('Banc de test cartes de flash v0.1')
    # popup.geometry('600x400+100+50')
    # popup.columnconfigure(0, weight=4)
    #
    # popup.rowconfigure(1, weight=5)
    ser = serial.Serial(input, 115000, timeout=20)  # open serial port

    ttk.Label(popup, text="Connected to port {0}".format(input)).grid(column=0, row=0)
    exit = ttk.Button(popup, text="Exit", command=lambda : disconnect(popup))
    exit.grid(column=1, row=0)

    st = ScrolledText(popup, width=500, height=100)
    st.grid(column=0, row=1, columnspan=2)

    input = tk.Text(popup, width=100, height=1)
    input.grid(column=0, row=2, pady=50)

    while True:
        popup.update()
        checkPorts(popup, ser, st)



#CHeck if there are things to print on the scree
def checkPorts(window, port ,text ):
    if port.is_open and port.in_waiting:
        text.insert(1.0, port.readline())

#send what we write in the input bar
def Send():
    a = 0


def disconnect(window):
    window.destroy()
    out = 1

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
