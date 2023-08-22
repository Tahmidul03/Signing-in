from tkinter import *

def click():
    print("Please Type in your ID information:")

def submit():
    username = text.get()
    print("Hello and Welcome " + username

def delete():
    text.delete(0,END)

def backspace():
    text.delete(len(text.get())-1, END)

#-----------------------------Setting up my GUI--------------------------------

i = Tk()
i.geometry('650x250')
i.title("Your Student Login Page")

#----------------------------Setting up GUI Profile Pic---------------------
pic = PhotoImage(file='img.png')
i.iconphoto(True,pic)


#--------------------------Background color of GUI---------------------------
i.config(background='Cyan')


#-------------------------Main Title----------------------------------
text = Label(i,text="Login to your account",
             font=('Times New Roman', 30, 'bold'),
             foreground='Black',
             background='Blue',
             relief=RAISED,
             bd=10)
text.pack()

#---------------------------Button for GUI Instruction----------------------------
button = Button(i,text="Guide?",
                command=click,
              font=("Times New Roman", 20, 'bold'),
              background='Red',
              foreground = 'Black',
              activeforeground='Red',
              activebackground='Black')
button.pack()


#--------------------Symbol when entering information-------------------------
text = Entry(i,font=("Times new roman", 20, 'bold'),
             show="*",)
text.pack(side=LEFT)


#------------------Submitting your Information-------------------------------
submit = Button(i,font=("Times new roman", 20, 'bold'),
                text='submit',
                command=submit)
submit.pack(side=RIGHT)


#----------------Deleting Information if entered wrong----------------------------
delete = Button(i,font=("Times new roman", 20, 'bold'),
                text='delete',
                command=delete)
delete.pack(side=RIGHT)


#--------------------Backspacing if any errors------------------------------
backspace = Button(i,font=("Times new roman", 20, 'bold'),
                text='backspace',
                command=backspace)
backspace.pack(side=RIGHT)


#--------------------------Initiating the complete GUI------------------------------
i.mainloop()
