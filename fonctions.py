import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import serial


font_port = ("Courier", 10)
out = 0


def is_spy(input):
    i = 0;
    while input[i] != ':' and input[i] != '\n':
        i += 1
    i+=1 # out of :
    if input[i:i+3] == "SPY":
        return True
    else :
        return False

def info_filter(input):
    i = 0;
    char0 = '0'
    charsep = '_'
    #GET TO THE INFORMATION
    while input[i] != '>':
        i += 1
    i += 1  # out of >
    j = i
    #ID
    while(input[j] != '_'):
        j+=1
    id = input[i:j]
    #add 0
    while len(id)<4 :
        id = char0 + id

    j +=1
    i = j
    while input[j] != ';':
        j += 1
    idl = input[i:j]
    while len(idl)<4:
        idl = char0 + idl
    id = id + charsep +idl

    #MASK
    while input[i] != '>':
        i += 1
    i += 1  # out of >
    j = i
    while input[j] != '_':
        j +=1

    mask = input[i:j] #get the high
    while len(mask)<4:
        mask = char0 + mask

    j+= 1
    i = j
    while input[j] != '\r':
        j += 1
    maskl = input[i:j]
    while len(maskl)<4:
        maskl = char0 + maskl
    mask = mask + charsep + maskl

    return id, mask


