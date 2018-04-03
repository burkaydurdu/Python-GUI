from tkinter import Tk, Label, Button, LEFT, RIGHT
#import RPi.GPIO as GPIO

from RPi.GPIO import GPIO
class Rasp:
    def __init__(self, master):
        self.master = master

        master.title("Raspberry GUI")
        #master.geometry('300x300')

        self.led1P = 14
        self.led2P = 18
        self.led3P = 21

        GPIO.setup(led1P, GPIO.OUT)
        GPIO.setup(led2P, GPIO.OUT)
        GPIO.setup(led3P, GPIO.OUT)

        self.label = Label(master, text="LED")
        self.label.pack()

        self.led1_button = Button(master, text="LED1", command=self.led1Func)
        self.led1_button.pack(side=LEFT)

        self.led2_button = Button(master, text="LED2", command=self.led2Func)
        self.led2_button.pack(side=LEFT)

        self.led3_button = Button(master, text="LED3", command=self.led3Func)
        self.led3_button.pack(side=LEFT)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=RIGHT)

    def led1Func(self):
        print("LED1")
        GPIO.output(led1P, GPIO.HIGH)

    def led2Func(self):
        print("LED2")

    def led3Func(self):
        print("LED3")

root = Tk()
my_gui = Rasp(root)
root.mainloop()
