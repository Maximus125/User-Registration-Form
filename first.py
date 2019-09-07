from tkinter import *
window=Tk()
window.geometry("800x800")
window.title("User Registration Form")

var=StringVar()

#HEADER
header=Label(window, text="User Registration", font=("Arial", 20), relief="solid")
header.place(x=280, y=10)

#ENTRYFIELD FOR FIRST NAME
firstname=Label(window, text="First Name : ", font=("Arial",13))
firstname.place(x=10, y=120)
field1=Entry()
field1.place(x=120, y=123)

#ENTRYFIELD FOR LAST NAME
lastname=Label(window, text="Last Name : ", font=("Arial",13))
lastname.place(x=10, y=160)
field2=Entry()
field2.place(x=120, y=163)

#ENTRY FIELD FOR  DOB
dob=Label(text="Date of Birth : \n (DD/MM/YYYY) ", font=("Arial",13))
dob.place(x=0, y=200)
field3=Entry()
field3.place(x=150, y=210)

#ENTRYFIELD FOR CITY
city=Label(window, text="City : ", font=("Arial",13))
city.place(x=10, y=255)
field4=Entry()
field4.place(x=120, y=260)

#ENTRYFIELD FOR STATE
state=Label(window, text="State : ", font=("Arial",13))
state.place(x=10, y=300)
list1=['Andhra Pradesh', 'Arunachal Pradesh','Assam','Bihar', 'Chattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','J&K','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
droplist=OptionMenu(window, var,*list1)
var.set("Select State")
droplist.config(width=20)
droplist.place(x=120, y=300)


window.mainloop()
