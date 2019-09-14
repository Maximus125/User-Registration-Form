from tkinter import *
import tkinter.messagebox
window=Tk()
window.geometry("800x800")
window.title("User Registration Form")

fn=StringVar()
mn=StringVar()
ln=StringVar()
DOB=StringVar()
pro=StringVar()
num=StringVar()
cit=StringVar()
var=StringVar()
c1=StringVar()


def printt():
    first=fn.get()
    mid=mn.get()
    sec=ln.get()
    dob1=DOB.get()
    number=num.get()
    project1=pro.get()
    var1=var.get()
    var2=cit.get()
    gend=c1.get()
    print(f"Your full name is {first+' '}{mid+' '}{sec}")
    print(f"Your DOB is {dob1}")
    print(f"Your contact number is {number}")
    print(f"Your City and State is {var2+' '}{var1}")
    print(f"Your Gender is {gend}")
    print(f"Your Project Name is {project1}")
    tkinter.messagebox.showinfo("Success", "Successfully Registered!\n \nYou can click on EXIT now to close the application.")


def exitt():
    exit()



#HEADER
header=Label(window, text="User Registration", font=("Arial", 20), relief="solid")
header.place(x=280, y=10)

#ENTRYFIELD FOR FIRST NAME
firstname=Label(window, text="First Name : ", font=("Arial",14))
firstname.place(x=10, y=120)
field1=Entry(window,textvar=fn)
field1.place(x=140, y=123)

#ENTRYFIELD FOR MIDDLE NAME
firstname=Label(window, text="Middle Name : ", font=("Arial",14))
firstname.place(x=400, y=120)
field1=Entry(window, textvar=mn)
field1.place(x=550, y=123)

#ENTRYFIELD FOR LAST NAME
lastname=Label(window, text="Last Name : ", font=("Arial",14))
lastname.place(x=10, y=160)
field2=Entry(window,textvar=ln)
field2.place(x=140, y=163)

#ENTRY FIELD FOR  DOB
dob=Label(text="Date of Birth : \n (DD/MM/YYYY) ", font=("Arial",14))
dob.place(x=0, y=200)
field3=Entry(window,textvar=DOB)
field3.place(x=150, y=210)

#ENTRY FIELD FOR GENDER
gender=Label(text="Gender: ", font=("Arial",14))
gender.place(x=400, y=210)

ch1=Radiobutton(window,text="Male", variable=c1, value="Male").place(x=500, y=210)
ch2=Radiobutton(window, text="Female", variable=c1, value="Female").place(x=570, y=210)
ch3=Radiobutton(window, text="Others", variable=c1, value="Others").place(x=650, y=210)

#ENTRYFIELD FOR CITY
city=Label(window, text="City : ", font=("Arial",14))
city.place(x=10, y=270)
field4=Entry(textvar=cit)
field4.place(x=100, y=275)

#ENTRYFIELD FOR STATE
state=Label(window, text="State : ", font=("Arial",14))
state.place(x=10, y=320)
list1=['Andhra Pradesh', 'Arunachal Pradesh','Assam','Bihar', 'Chattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','J&K','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
droplist=OptionMenu(window, var,*list1)
var.set("Select State")
droplist.config(width=20)
droplist.place(x=100, y=320)

#ENTRYFIELD FOR CONTACT NO.
cont=Label(text="Contact No.:      +91 -  ", font=("Arial",14))
cont.place(x=10, y=390)
field5=Entry(textvar=num)
field5.place(x=200, y=395)

#ENTRYFIELD FOR PROJECT DESCRIPTION
proj=Label(text="Project Name: ", font=("Arial",14))
proj.place(x=10, y=460)
field6=Entry(window,textvar=pro)
field6.place(x=180, y=464)


#BUTTONS
but1=Button(text="Submit", width=12, height=2, bg="beige", font=("Arial", 8), command=printt)
but1.place(x=100, y=650)

but2=Button(text="Exit", width=12, height=2, bg="beige", font=("Arial",8), command=exitt)
but2.place(x=600, y=650)

window.mainloop()
