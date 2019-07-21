from tkinter import *
from tkinter.ttk import *
import os



def change_dropdown(*args):
    pass

    

# link function to change dropdown




def choice1():
     k = int(v1.get())
     if k==1:
        e2.config(state='enabled')
     else:
        e2.config(state='disabled')



def set_up():
    print("yay")

frame1 =Tk()

frame1.geometry("270x300")
frame1.title("Email Automator")

v1 = IntVar()
tkvar = StringVar()


f1=Frame(frame1)
f1.grid(row=0,padx=30)
f2=Frame(frame1)
f2.grid(row=1,padx=30)
f3=Frame(frame1)
f3.grid(row=2,padx=30)
f4 = Frame(frame1)
f4.grid(row=3,padx=30)

l1 = Label(f1,text ="Please Enter Date for Sending Email")
l1.grid()
le = Label(f1,text ="(dd,mm,yyyy)")
le.grid()
e1 = Entry(f1,width="30")
e1.grid(pady =2)
Label(f1,text="").grid()
Separator(f1).grid(sticky="ew")


l2 = Label(f2,text ="Please select message template")
l2.grid()
choices = ["Meeting","Birthday","General"]
popupMenu = OptionMenu(f2, tkvar,choices[0], *choices)
popupMenu.grid()
tkvar.trace('w', change_dropdown)
e2 = Entry(f2,width="30")
e2.grid(rowspan=2,columnspan=2)
Label(f2,text="").grid()
Separator(f2).grid(sticky="ew")



l3 = Label(f3,text = "Recipients")
l3.grid()
r1 = Radiobutton(f3,text ="All Recipients",variable=v1,value=0,command=choice1)
r1.grid()
r2 = Radiobutton(f3,text="Only These Recipients",variable = v1,value =1,command =choice1)
r2.grid()
e2 = Entry(f3,state='disabled',width="30")
e2.grid()
Label(f3,text="").grid()
Separator(f3).grid(sticky="ew")



b1 = Button(f4,text="Confirm",command=set_up)
b1.grid()



# Dictionary with options

# on change dropdown value





frame1.mainloop()