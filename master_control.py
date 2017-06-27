import sys
import tkinter
import os
import subprocess
from tkinter import *

root=Tk()
root.title("Master_Control")

bf=Frame(root)
uf=Frame(root)
df=Frame(root)
vf=Frame(root,width=36)
af=Frame(root)

def bright(val2):
	br=subprocess.popen("xbacklight -set "+val2,shell=True)
def print_value(val):
	    p=subprocess.Popen("amixer -q -D pulse sset Master "+val+"%",shell=True)
def toggle(tog=[0]):
	v=subprocess.Popen("amixer -q -D pulse sset Master toggle",shell=True)
	tog[0] = not tog[0]
	if tog[0]:
		t_btn.config(text='Unmute')
		
	else:        	
		t_btn.config(text='Mute')
def capture():
	c=subprocess.Popen("streamer -f jpeg -o /home/$USER/Pictures/$(date +\%Y\%m\%d\%H\%M\%S).jpeg",shell=True)

def screenshot():
	s=subprocess.Popen("gnome-screenshot",shell=True)

def firefox():
	s=subprocess.Popen("firefox",shell=True)
def Libre_Office():
	s=subprocess.Popen("libreoffice",shell=True)
def System_Monitor():
	s=subprocess.Popen("gnome-system-monitor",shell=True)
def Gnome_edit():
	s=subprocess.Popen(" gedit",shell=True)
def Software_Centre():
	s=subprocess.Popen("gnome-software",shell=True)
def Terminal():
	s=subprocess.Popen("gnome-terminal",shell=True)
	
lbl=Label(uf,text="Volume Control: ").pack(side=LEFT)
scale =Scale(uf,orient='horizontal',length=270,width=16,sliderlength=10,tickinterval=15, from_=0, to=100, command=print_value)
scale.pack(side=RIGHT)

lbl2=Label(bf,text="Brightness Control: ").pack(side=LEFT)
scale2 =Scale(bf,orient='horizontal',length=270,width=16,sliderlength=10,tickinterval=15, from_=0, to=100, command=bright)
scale2.pack(side=RIGHT)

t_btn = Button(df,text="Mute", command=toggle)
t_btn.pack(side=RIGHT)

lbl3=Label(vf,text="Display & Camera Control: ").pack(side=LEFT)
btn_cap=Button(vf,text="capture",width=15,command=capture)
btn_cap.pack(side=RIGHT)
btn_screen=Button(vf,text="Screenshot",width=15,command=screenshot)
btn_screen.pack(side=RIGHT)

lbl4=Label(af,text="Applications").pack(fill=X)
Firefox=Button(af,text="Mozilla_Firefox",width=15,command=firefox).pack(fill=X)
Libre_Office=Button(af,text="Libre_Office",width=15,command=Libre_Office).pack(fill=X)
System_Monitor=Button(af,text="System_Monitor",width=15,command=System_Monitor).pack(fill=X)
Gnome_edit=Button(af,text="Gnome_edit",width=15,command=Gnome_edit).pack(fill=X)
Software_Centre=Button(af,text="Software_Centre",width=15,command=Software_Centre).pack(fill=X)
Terminal=Button(af,text="Terminal",width=15,command=Terminal).pack(fill=X)

bf.pack(fill=X)
uf.pack(fill=X)
df.pack(fill=X)
vf.pack(fill=X)
af.pack(fill=X)

root.mainloop()

