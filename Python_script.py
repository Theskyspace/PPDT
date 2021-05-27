import tkinter

import os
import random 
import time
import winsound


top = tkinter.Tk()

cont = 1

path="E:\\Coding zone\\PP&DT\\src"  #Path to your location
files=os.listdir(path)

for i in range(10):
	d=random.choice(files)
	print(d)
	os.startfile(d)
	cont = int(input("Do you want to continue with this?(1/0)"))
	if cont == 1:
		time.sleep(30)
		winsound.Beep(300, 10000)
		
		time.sleep(215)
		winsound.Beep(400, 10000)
		time.sleep(10)
		winsound.Beep(500, 10000)
	else:
		continue
