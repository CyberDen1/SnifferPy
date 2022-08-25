#/usr/bin/python 
# -*- coding: UTF-8 -*-

from Tkinter import *
import socket

root1 = Tk()
root1.title("Сообщение")
frame = Frame(root1)
frame.pack()
label = Label(frame, text="Нажмите 'Продолжить' и дождитесь завершения работы программы")
label.grid(row=0, column=1)
exit_button = Button(frame, text="Продолжить", width=10, command=root1.destroy)
exit_button.grid(row=1, column=1)
root1.mainloop()

FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])

def dump(src, length=8):
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["%02X"%ord(x) for x in s])
       s = s.translate(FILTER)
       result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
       N+=length
    return result

def main():
  root=Tk()
  text1=Text(root,height=50,width=60,font='Courier 14',wrap=WORD)
  text1.pack()
  root.title(u'ICMP') 
  f1 = open("ICMP.txt", 'w')
  num_of_packets = 1
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
  
  for i in range(0, num_of_packets):
    packet = s.recv(16000)
    
    text1.insert(0.0,"\n")
    text1.insert(0.0,dump(packet))
    text1.insert(0.0,"\n")
    text1.insert(0.0,"Got a %d byte packet\n" % len(packet))
    f1.write("\n")
    f1.write("Got a %d byte packet\n" % len(packet))
    f1.write("\n")
    f1.write(dump(packet))

  root.mainloop()
     
if __name__ == '__main__':
  main()






