from tkinter import *
import tkinter.messagebox as tmsg
class Main():
    def __init__(self, master):
        self.master=master
        self.master.geometry('500x400')
        self.master.title("myInformation")
        mainmenu=Menu(master)
        m1=Menu(mainmenu)
        m1.add_command(label="About GUI",command=self.aboutgui)
        m1.add_command(label='About maker',command=self.aboutus)
        master.config(menu=mainmenu)
        mainmenu.add_cascade(label='About',menu=m1)
        self.username=Label(self.master,text="Enter your username")
        self.password=Label(self.master,text="Enter your password")

        self.username.grid(row=1,column=3)
        self.password.grid(row=1,column=6)

        self.uservalue=StringVar()
        self.passvalue=StringVar()

        self.userentry=Entry(self.master,textvariable=self.uservalue)
        self.passentry=Entry(self.master,textvariable=self.passvalue)

        self.userentry.grid(row=1,column=4)
        self.passentry.grid(row=1,column=7)

        self.button=Button(self.master,text="Submit",command=self.checker)
        self.button.grid(row=3,column=7)

    def aboutgui(self):
        tmsg.showinfo("AboutGUI","this gui will help you keep your records")

    def aboutus(self):
        tmsg.showinfo("Aboutmaker","this gui is maked by badrinarayan")
    
    def checker(self):
        if self.uservalue.get()=="Badri" and self.passvalue.get()=="mypassword":

            self.userentry.destroy()
            self.username.destroy()

            self.passentry.destroy()
            self.password.destroy()

            self.button.destroy()

            but1=Button(self.master,text="Add Emloyee",command=self.addemployee)
            but2=Button(self.master,text="Information",command=self.Information)
            but1.grid(row=5,column=5)
            but2.grid(row=5,column=6)
        else:
            tmsg.showerror("Error","Invalid username and password")

    def addemployee(self):
        root2=Toplevel(self.master)
        myGUi=real(root2)
        
    def Information(self):
        root2=Toplevel(self.master)
        myGUi=info(root2)

class info():
    def __init__(self,master):
        self.master=master
        mainmenu=Menu(master)
        m1=Menu(mainmenu)
        m1.add_command(label="About GUI",command=self.aboutgui)
        m1.add_command(label='About maker',command=self.aboutus)
        master.config(menu=mainmenu)
        mainmenu.add_cascade(label='About',menu=m1)
        self.name=Label(self.master,text="Name of candidate:")
        self.name.grid(row=1,column=1)

        self.namevalue=StringVar()

        self.nameentry=Entry(self.master,textvariable=self.namevalue)

        self.nameentry.grid(row=1,column=2)

        Button(self.master,text="Ok",command=self.cadinfo).grid(row=2,column=1)

        self.area=Text(self.master)
        self.area.grid(row=5,column=3)

    def cadinfo(self):
        with open("records.txt","r") as f:
            lst=f.readlines()
        for sentances in lst:
            count=len(self.namevalue.get())+2
            if sentances[2:count]==self.namevalue.get():
                self.area.delete(1.0,END)
                self.area.insert(INSERT,sentances)
            else:
                pass             
    def aboutgui(self):
        tmsg.showinfo("AboutGUI","this gui will help you keep your records")

    def aboutus(self):
        tmsg.showinfo("Aboutmaker","this gui is maked by badrinarayan")
class real():
    def __init__(self,master):
        self.master=master
        mainmenu=Menu(master)
        m1=Menu(mainmenu)
        m1.add_command(label="About GUI",command=self.aboutgui)
        m1.add_command(label='About maker',command=self.aboutus)
        master.config(menu=mainmenu)
        mainmenu.add_cascade(label='About',menu=m1)

        self.name=Label(self.master,text="name: ")
        self.lastname=Label(self.master,text="lastname: ")
        self.Phone=Label(self.master,text="phoneno.: ")
        self.Gmail=Label(self.master,text="Gmail: ")
        self.Date=Label(self.master,text="DateOfJoinig: ")

        self.name.grid(row=1,column=1)
        self.lastname.grid(row=2,column=1)
        self.Phone.grid(row=3,column=1)
        self.Gmail.grid(row=4,column=1)
        self.Date.grid(row=5,column=1)

        self.namevalue=StringVar()
        self.lastnamevalue=StringVar()
        self.Phonevalue=StringVar()
        self.Gmailvalue=StringVar()
        self.datevalue=StringVar()

        self.nameentry=Entry(self.master,textvariable=self.namevalue)   
        self.lastnameentry=Entry(self.master,textvariable=self.lastnamevalue)   
        self.Phoneentry=Entry(self.master,textvariable=self.Phonevalue)   
        self.Gmailentry=Entry(self.master,textvariable=self.Gmailvalue)   
        self.Dateentry=Entry(self.master,textvariable=self.datevalue)  

        self.nameentry.grid(row=1,column=2) 
        self.lastnameentry.grid(row=2,column=2) 
        self.Phoneentry.grid(row=3,column=2) 
        self.Gmailentry.grid(row=4,column=2) 
        self.Dateentry.grid(row=5,column=2) 
     
        Button(self.master,text="submit",command=self.record).grid(row=6,column=2)

    def record(self):
        with open("records.txt","a") as f:
            f.write(f"{self.namevalue.get(),self.lastnamevalue.get(),self.Phonevalue.get(),self.Gmailvalue.get(),self.datevalue.get()}\n")
        Label(self.master,text="Employee Added",fg="green").grid(row=7,column=2)
    def aboutgui(self):
        tmsg.showinfo("AboutGUI","this gui will help you keep your records")

    def aboutus(self):
        tmsg.showinfo("Aboutmaker","this gui is maked by badrinarayan")
        
def main():
    root=Tk()
    myGUIwindow=Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()
