from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("700x550")
root.title("Квест")

def play():
	button = Button(text="      Играть      ", command=lambda: kvest())
	button.pack()

def kvest():
	text = Label(text="Ты проснулся на другой планете \n1.Улитеть на Землю \n2.Иследовать эту жалкую планету")
	


	text.pack()

play()
root.mainloop()