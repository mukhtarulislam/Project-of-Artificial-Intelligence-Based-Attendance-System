from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    # install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #-------------------------------------Text variable--------------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()


        # background image in Register system
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\registerbg.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

         #Left side image in Register system
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\left_side login.jpg")
        left_lbl_bg1=Label(self.root,image=self.bg1)
        left_lbl_bg1.place(x=50,y=100,width=470,height=550)



        
        # main frame upper side of the bg image
        frame = Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #label for top image
        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)






        #-----------------------------label and entry----------------------------------------
        
        #first name label
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)
        # first name entry  fill(name) 
        fname_entry =ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)


        #Last name label
        lastname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lastname.place(x=370,y=100)
        # Last name entry  fill(name) 
        lastname_entry =ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lastname_entry.place(x=370,y=130,width=250)


        #contact no label
        contact_no=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact_no.place(x=50,y=170)
        # contact no entry  fill(name) 
        contact_no_entry =ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_no_entry.place(x=50,y=200,width=250)

        #email no label
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        # email no entry  fill(name) 
        email_entry =ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)

        #security Question label
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        #Security Question combo (left label frame inside)
        security_Q_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",13,"bold"),state="read only",width=18)
        security_Q_combo["values"]=("Select", "Birth Place","First pet name","Favourate Color","Birth mark")
        security_Q_combo.place(x=50,y=270,width=250)
        security_Q_combo.current(0)

        
        #security  label
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)
        # Security no entry  fill(name) 
        security_A_entry =ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        security_A_entry.place(x=370,y=270,width=250)


       # password label
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=310)
        # Password no entry  fill(name) 
        password_entry =ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        password_entry.place(x=50,y=340,width=250)

        # confirm_password label
        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_password.place(x=370,y=310)
        # Password no entry  fill(name) 
        confirm_password_entry =ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15,"bold"))
        confirm_password_entry.place(x=370,y=340,width=250)

       
        #------------------------------------check box-----------------------

        self.var_check_btn=IntVar()
        check_btn=Checkbutton(frame,variable=self.var_check_btn,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),fg="black",bg="white",onvalue=1,offvalue=0)
        check_btn.place(x=50,y=380)
        
        #-------------------------------------Buttons image register----------------------------
        img=Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\registerbutton.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=300)

         #-------------------------------------Buttons image login----------------------------
        img1=Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\loginbutton.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=300)





    #=====================================================function declaration====================================================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Field are required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password & confirm pass must be same")
        elif self.var_check_btn.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions")

        else:
            db=mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
            my_cursor=db.cursor()
            query=("select * from register where Email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            data_fetch=my_cursor.fetchone()

            if data_fetch!=None:
                messagebox.showerror("Error","Your already register,Please try another email")
            else:
                my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(

                                                                self.var_fname.get(),
                                                                self.var_lname.get(),
                                                                self.var_contact.get(),
                                                                self.var_email.get(),
                                                                self.var_securityQ.get(),
                                                                self.var_securityA.get(),
                                                                self.var_password.get()
                                                                 
                                                                 ))

            db.commit()
            db.close()
            messagebox.showinfo("Success","Registration completed")



    



       














if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()