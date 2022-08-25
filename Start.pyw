#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import os

from Tkinter import *
root = Tk()

var = StringVar()
label = Label(root, textvariable=var, height=5, font=("Helvetica", 16))
var.set("Анализатор трафика")
label.pack()

var = StringVar()
label = Label(root, textvariable=var)
var.set("Приложение, предназначенное для мониторинга сетевого трафика локальной сети")
label.pack()

var = StringVar()
label = Label(root, textvariable=var)
var.set("Выберите протокол, по которому будет осуществлен анализ:")
label.pack()

def Ev1(event):
    os.system('python pUDP.py')

btn1 = Button(root,                  
             text="UDP",       
             width=70,height=5,     
             bg="white",fg="black") 
btn1.bind("<Button-1>", Ev1)       
btn1.pack()                          


def Ev2(event):
     os.system('python pTCP.py')

btn2 = Button(root,                  
             text="TCP",       
             width=70,height=5,     
             bg="white",fg="black") 
btn2.bind("<Button-1>", Ev2)       
btn2.pack()                          

def Ev3(event):
     os.system('python pICMP.py')

btn3 = Button(root,                  
             text="ICMP",       
             width=70,height=5,     
             bg="white",fg="black") 
btn3.bind("<Button-1>", Ev3)       
btn3.pack()                          

var = StringVar()
label = Label(root, textvariable=var)
var.set("Внимание! Не закрывайте окно, пока не завершится работа программы!")
label.pack()

var = StringVar()
label = Label(root, textvariable=var)
var.set("Разработчики: Бурый Д.С. и Хрусталев С.А.")
label.pack()

root.title(u'Анализатор трафика')

root.mainloop()
