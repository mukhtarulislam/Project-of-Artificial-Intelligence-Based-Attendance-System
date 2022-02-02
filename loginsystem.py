from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    # install pillow
from tkinter import messagebox
#import random
#import time
#import datetime
import mysql.connector
from main import Face_Recognition_System
#from register import Register


#=========================connecting two class together by using this function===========================
def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        

        # background image in login system
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\login_background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        # main frame upper side of the bg image
        frame = Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        #top Image path of front and resizing logo on upper side of main frame
        img_top_1 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\admin.png")
        img_top_1 =img_top_1.resize((100,100),Image.ANTIALIAS)
        self.photoimg_top_1=ImageTk.PhotoImage(img_top_1)
        #label for top image
        f_lbl = Label(self.root,image =self.photoimg_top_1)
        f_lbl.place(x=730,y=175,width=100,height=100)

        # label start inside the  main frame
        get_str= Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        
        



        #===================Label and entry fill for user name inside the main frame   ==================
        user_name=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        user_name.place(x=70,y=155)

        # username entry  fill(name) 
        self.txtuser =ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)


         #===================Label and entry fill for password inside the main frame   ==================
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        # password entry  fill(name) 
        self.txtpass =ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        #===================Icon for user name and password====================
        #Icon image of user name
        img2 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\admin.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        #label for top image
        lblimg1 = Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        #Icon image of user password
        img3 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\admin-security-icon.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        #label for top image
        lblimg1 = Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        
        
        #=======================================Button ===================================================
        
        #login button inside the frame
        login_btn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),border=3,relief=RIDGE,foreground="white",background='black',activeforeground='white',activebackground='black')
        login_btn.place(x=110,y=300,width=120,height=35)


        #Register  button inside the frame
        register_btn=Button(frame,text="New User Register",command=self.login,font=("times new roman",10,"bold"),borderwidth=0,foreground="white",background='black',activeforeground='white',activebackground='black')
        register_btn.place(x=20,y=350,width=160)

        #forget password  button inside the frame
        forget_password_btn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,foreground="white",background='black',activeforeground='white',activebackground='black')
        forget_password_btn.place(x=19,y=380,width=160)


    #-----------------------join register window-------------------------------
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    
    
    
    
    #==========================login button function======================================

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required")
        elif self.txtuser.get()=="tiger" and self.txtpass.get()=="lion":
            messagebox.showinfo("Success","Welcome to admin login system")
        else:
            db=mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
            my_cursor=db.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(

                                                                        self.txtuser.get(),
                                                                        self.txtpass.get()


                                                                             ))
            
            data_fetch=my_cursor.fetchone()
            
            if data_fetch== None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main=messagebox.askyesno("Yes or No","Permission Denied")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
            db.commit()
            db.close()

    
    # ------------------------------------------Reset password function inside forgot password window----------------------------------------
    def reset_password(self):
        if self.security_Q_combo.get()=="Select":
            messagebox.showerror("Error","Choose the security question",parent=self.root2)
        elif self.txt_security_A_entry.get()=="":
            messagebox.showerror("Error","Please enter security answer",parent=self.root2)
        elif self.txt_new_password_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)

        else:
            db=mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
            my_cursor=db.cursor()
            kury=("select * from register where Email=%s and SecurityQuestion=%s and SecurityAnswer=%s")
            vllue=(self.txtuser.get(),self.security_Q_combo.get(),self.txt_security_A_entry.get(),)
            my_cursor.execute(kury,vllue)
            ftch_data=my_cursor.fetchone()
            
            if ftch_data==None:
                messagebox.showerror("Error","please correct answer",parent=self.root2)
            else:
                query=("update register set Password=%s where Email=%s")
                value=(self.txt_new_password_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)


                db.commit()
                db.close()
                messagebox.showinfo("Info","Your password has been reset ,please login with new password",parent=self.root2)

                self.root2.destroy()

            







    #--------------------------------------forget button function working over here----------------------------------------

    def forgot_password_window(self):
        if self.txtuser.get=="":
            messagebox.showerror("Error","Please Enter the email address to reset the password")
        else:
            db=mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
            my_cursor=db.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            data_fetch=my_cursor.fetchone()
            #print(data_fetch)

        if data_fetch==N:
            messagebox.showerror("personal Error","Please enter the valid user name")
        else:
            db.close()
            self.root2=Toplevel()
            self.root2.title("Forgot Password")
            self.root2.geometry("340x450+610+170")

            l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="white")
            l.place(x=0,y=10,relwidth=1)


            #security Question label
            security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
            security_Q.place(x=50,y=80)

            #Security Question combo (left label frame inside)
            self.security_Q_combo=ttk.Combobox(self.root2,font=("time new roman",13,"bold"),state="read only",width=18)
            self.security_Q_combo["values"]=("Select", "Birth Place","First pet name","Favourate Color","Birth mark")
            self.security_Q_combo.place(x=50,y=110,width=250)
            self.security_Q_combo.current(0)

            
            #security  label
            security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
            security_A.place(x=50,y=150)
            # Security no entry  fill(name) 
            self.txt_security_A_entry =ttk.Entry(self.root2,font=("times new roman",15,"bold"))
            self.txt_security_A_entry.place(x=50,y=180,width=250)


            # new password label
            new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
            new_password.place(x=50,y=220)
            # new Password no entry  fill(name) 
            self.txt_new_password_entry =ttk.Entry(self.root2,show='*',font=("times new roman",15,"bold"))
            self.txt_new_password_entry.place(x=50,y=250,width=250)

           
            #button for reset new password
            btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="black",bg="white")
            btn.place(x=100,y=290)



            
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



        
        # -----------------------------------main frame upper side of the bg image-----------------------------------------
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
        self.fname_entry =ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)


        #Last name label
        lastname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lastname.place(x=370,y=100)
        # Last name entry  fill(name) 
        self.txt_lastname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lastname.place(x=370,y=130,width=250)


        #contact no label
        contact_no=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact_no.place(x=50,y=170)
        # contact no entry  fill(name) 
        self.txt_contact_no =ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact_no.place(x=50,y=200,width=250)

        #email no label
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        # email no entry  fill(name) 
        self.txt_email_entry =ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email_entry.place(x=370,y=200,width=250)

        #security Question label
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        #Security Question combo (left label frame inside)
        self.security_Q_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",13,"bold"),state="read only",width=18)
        self.security_Q_combo["values"]=("Select", "Birth Place","First pet name","Favourate Color","Birth mark")
        self.security_Q_combo.place(x=50,y=270,width=250)
        self.security_Q_combo.current(0)

        
        #security  label
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)
        # Security no entry  fill(name) 
        self.txt_security_A_entry =ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security_A_entry.place(x=370,y=270,width=250)


       # password label
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=310)
        # Password no entry  fill(name) 
        self.txt_password =ttk.Entry(frame,textvariable=self.var_password,show='*',font=("times new roman",15,"bold"))
        self.txt_password.place(x=50,y=340,width=250)

        # confirm_password label
        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_password.place(x=370,y=310)
        # Password no entry  fill(name) 
        self.txt_confirm_password =ttk.Entry(frame,textvariable=self.var_confirm_password,show='*',font=("times new roman",15,"bold"))
        self.txt_confirm_password.place(x=370,y=340,width=250)

       
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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
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


    #--------------------------function define return to login page------------------------
    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()

