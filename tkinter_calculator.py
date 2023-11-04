from tkinter import *
import tkinter as tk

#from PIL import ImageTk, Image  

mainscreen = tk.Tk()
mainscreen.geometry("270x350")
mainscreen.title("Calculator")

label = tk.Label(mainscreen,text = "Calculator", font = ("Arial",18,"bold"))
label.place (x = 80, y = 30)

entry1 = tk.Entry(mainscreen, bd = 5,textvariable = "inputfield",width = "30")
entry1.place(x = 20, y = 75)

btn = tk.Button(mainscreen,text = "AC", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold"))
btn.place (x = 20, y = 120)
btn = tk.Button(mainscreen,text = "<-", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold"))
btn.place (x = 80, y = 120)
btn = tk.Button(mainscreen,text = "%", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold"))
btn.place (x = 140, y = 120)
btn = tk.Button(mainscreen,text = "/", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold"))
btn.place (x = 200, y = 120)

btn = tk.Button(mainscreen,text = "9", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 20, y = 160)
btn = tk.Button(mainscreen,text = "8", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 80, y = 160)
btn = tk.Button(mainscreen,text = "7", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 140, y = 160)
btn = tk.Button(mainscreen,text = "x", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 200, y = 160)

btn = tk.Button(mainscreen,text = "6", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 20, y = 200)
btn = tk.Button(mainscreen,text = "5", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 80, y = 200)
btn = tk.Button(mainscreen,text = "4", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 140, y = 200)
btn = tk.Button(mainscreen,text = "-", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 200, y = 200)

btn = tk.Button(mainscreen,text = "3", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 20, y = 240)
btn = tk.Button(mainscreen,text = "2", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 80, y = 240)
btn = tk.Button(mainscreen,text = "1", width = "5", activebackground = "lightblue", background = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 140, y = 240)
btn = tk.Button(mainscreen,text = "+", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 200, y = 240)

btn = tk.Button(mainscreen,text = "0", width = "10", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 20, y = 280)
btn = tk.Button(mainscreen,text = "=", width = "10", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 110, y = 280)
btn = tk.Button(mainscreen,text = ".", width = "5", background = "lightblue", activebackground = "pink", bd = 3, height = "1", font = ("arial", 9, "bold") )
btn.place (x = 200, y = 280)

mainscreen.mainloop()
