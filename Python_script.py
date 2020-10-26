import os
import random 
import time
import winsound
cont = 1

path="E:\\PP&DT"
files=os.listdir(path)

for i in range(10):
	d=random.choice(files)
	os.startfile(d)
	cont = int(input("Do you want to continue with this?(1/0)"))
	if cont = 1:
		time.sleep(15)
		winsound.Beep(300, 10000)
