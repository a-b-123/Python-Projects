#Basic Python GUI Port Scanner to scan the Default Gateway on your Network OR your own host, "localhost"
#Learned how to do this (especially using tkinter for GUI) with help from a great tutorial by CodeOnBy on YouTube: https://www.youtube.com/watch?v=W4dqliRCtaw
#THIS IS INTENDED FOR EDUCATIONAL PURPOSES ONLY

import pyfiglet
import socket
import sys
import threading
import time
from tkinter import *

banner = pyfiglet.figlet_format("PEEK")
print("---------------")
print(banner) 
print("---------------")

PortStart = 1
PortFin = 1024
OpenPorts = []
Target = '192.168.1.254' 

def Scan(Target, ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        conn = s.connect_ex((Target,ports))
        if conn == 0:
            out = "Port %d \t is: OPEN" % (ports)
            OpenPorts.append(ports)
            listbox.insert("end",str(out))
            Open()
        s.close()
    except KeyboardInterrupt: print("Operation was interrupted because of input from keyboard")
    except: conn.close()
    sys.exit()

def Open():
    result = "[" + str(len(OpenPorts)) + " out of " + str(PortFin) + "]" + " for IP: " + str(Target)
    L27.configure(text=result)

def BeginScan():
    global OpenPorts, Target, PortFin
    Clean()
    OpenPorts = []
    PortStart = int(L24.get())
    PortFin = int(L25.get())

    try:
        Target = socket.gethostbyname(str(L22.get()))
        while PortStart <= PortFin:
            try:
                scan = threading.Thread(target=Scan,args=(Target,PortStart))
                scan.setDaemon(True)
                scan.start()
            except: time.sleep(0.01)
            PortStart += 1
    except: NotFound = 'Target' + str(L22.get()) + 'was not found, not able to scan.'
    

def Clean():
    listbox.delete(0,'end')

GUI = Tk()
GUI.title("PEEK Port Scanner")
GUI.geometry("400x600+20+20")

C1 = '#00ee00'
bcgkd = '#222222'
dbg = '#000000'
fgrd = '#111111'

GUI.tk_setPalette(background=bcgkd,foreground=C1,activeBackground=fgrd,activeForeground=bcgkd,highlightColor=C1)

L11 = Label(GUI, text = pyfiglet.figlet_format("P E E K")) #font = ("Helvetica", 16, 'underline'))
L11.place(x=130,y=10)

L21 = Label(GUI,text="Target To Scan:")
L21.place(x=16,y=110)

L22 = Entry(GUI, text='Gateway')
L22.place(x=180, y = 110)
L22.insert(0, '*Gateway Address*')

L23 = Label(GUI,text = "Ports:")
L23.place(x=16,y=158)

L24 = Entry(GUI,text = '1')
L24.place(x=180,y=158,width=95)
L24.insert(0,"1")

L25 = Entry(GUI, text = "1024")
L25.place(x=290,y=158,width=95)
L25.insert(0,'1024')

L26 = Label(GUI, text = "Results:")
L26.place(x=16,y=220)


frame = Frame(GUI)
frame.place(x=16,y=275,width=370,height=215)

listbox = Listbox(frame,width=59,height=6)
listbox.place(x=0,y=0)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

B11 = Button(GUI,text = "Start Scan",command=BeginScan)
B11.place(x=16,y=500,width=170)

GUI.mainloop()
