from tkinter import*
import RPi.GPIO as GPIO
import time

import smbus

bus = smbus.SMBus(1)

SLAVE_ADDRESS_1 = 0x08
SLAVE_ADDRESS_2 = 0x09
SLAVE_ADDRESS_3 = 0x0a

class App:

def __init__(self, master):

def FirstServo(self):
S_1 = scale_first.get()
bus.write_byte_data(SLAVE_ADDRESS_1, S_1, S_1 )

def SecondServo(self):
S_2 = scale_second.get()
bus.write_byte_data(SLAVE_ADDRESS_2, S_2, S_2 )

def ThirdServo(self):
S_3 = scale_third.get()
bus.write_byte_data(SLAVE_ADDRESS_3, S_3, S_3 )

frame = Frame(master)
frame.pack()

scale_first = Scale(frame, label="Клешня", from_=0, to=180, orient=HORIZONTAL, command=FirstServo)
scale_first.grid(row=1, column=1)
scale_second = Scale(frame, label="Сгибание", from_=0, to=180, orient=HORIZONTAL, command=SecondServo)
scale_second.grid(row=2, column=1)
scale_third = Scale(frame, label="Поворот основания" from_=0, to=180, orient=HORIZONTAL, command=ThirdServo)
scale_third.grid(row=3, column=1)

root = Tk()
root.wm_title('Управление роботизированным модулем')
app = App(root)
root.geometry("200x150+0+0")
root.mainloop()