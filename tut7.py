import tkinter as tk

mainscreen = tk.Tk()
mainscreen.geometry("300x350")

def printData():
    print("\nCheck your Details\n")
    print("Your Name : ",fname_entry.get())
    print("Father's Name : Mr. ",Fname_entry.get())
    print("Mother's Name : Mrs. ", mname_entry.get())

    if(radiobtn.get()==1):
        print("You are a Male.")
    elif(radiobtn.get()==2):
        print("You are a Female.")
    else:

        print("You are a Transgender")
        
    if(checkbox1_var.get() == 1):
        if(checkbox1_var.get() == 1 and checkbox2_var.get() == 1):
            print("You are good in Studies as well as Sports")
        else:
            print("You are good in Studies")        
    elif(checkbox2_var.get() == 1):
        print("You are good in Sports")
    else:
        print("you are FUDDU person")
        
        
def ext():
       exit()       

title = tk.Label(mainscreen,text = "Registration Form")
title.place (x = 90, y = 30)

fname = tk.Label(mainscreen,text = "First Name : ")
fname.place (x = 35, y = 80)
fname_entry = tk.Entry(mainscreen, bd = 5)
fname_entry.place(x = 125, y = 80)

Fname = tk.Label(mainscreen,text = "Father's Name : ")
Fname.place (x = 35, y = 120)
Fname_entry = tk.Entry(mainscreen, bd = 5)
Fname_entry.place(x = 125, y = 120)

mname = tk.Label(mainscreen,text = "Mother's Name : ")
mname.place (x = 35, y = 160)
mname_entry = tk.Entry(mainscreen, bd = 5)
mname_entry.place(x = 125, y = 160)

gen = tk.Label(mainscreen,text = "Gender : ")
gen.place (x = 35, y = 200)
radiobtn = tk.IntVar()
radiobtn1 = tk.Radiobutton (mainscreen, text = "Male",variable = radiobtn, value = 1)
radiobtn1.place(x = 100, y = 200)
radiobtn2 = tk.Radiobutton (mainscreen, text = "Female",variable = radiobtn, value = 2)
radiobtn2.place(x = 150, y = 200)

lang = tk.Label(mainscreen,text = "Interests : ")
lang.place (x = 35, y = 240)

checkbox1_var = tk.IntVar()
checkbox1 = tk.Checkbutton(mainscreen,text = "Studies", variable = checkbox1_var, onvalue = 1, offvalue = 0)
checkbox1.place(x = 100,y = 240)

checkbox2_var = tk.IntVar()
checkbox2 = tk.Checkbutton(mainscreen,text = "Supports", variable = checkbox2_var, onvalue = 1, offvalue = 0)
checkbox2.place(x = 175,y = 240)


exitbtn = tk.Button(mainscreen, text = "Exit",background = "Purple",foreground = "white",width = "15",height = "1",activebackground = "pink", command = ext)
exitbtn.place(x = 18,y = 300)

submitbtn = tk.Button(mainscreen, text = "Submit",background = "Purple",foreground = "white",width = "15",height = "1",activebackground = "pink", command = printData)
submitbtn.place(x = 165,y = 300)

mainscreen.mainloop()


