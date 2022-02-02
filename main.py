import tkinter
from helpdesk import Helpdesk
from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Helpdesk
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # (first image)Image path of front and resizing
        img =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\university.jpg")
        img =img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        #label
        f_lbl = Label(self.root,image =self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # (Second image)Image path of front and resizing
        img1 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\facial-recognition.png")
        img1 =img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        #label
        f_lbl = Label(self.root,image =self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # (Third image) Image path of front and resizing
        img2 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\mannu.jpg")
        img2 =img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        #label
        f_lbl = Label(self.root,image =self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # Background image of system
        img3 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\bg.jpg")
        img3 =img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        #label
        bg_img = Label(self.root,image =self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        # title label
        title_lbl =Label(bg_img,text=" FACE RECOGNITION SYSTEM ATTENDANCE",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        #================================ Time function=======================================
        def  time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
            


        # Student button from image
        img4 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\student.jpg")
        img4 =img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command =self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Student Details",command =self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220, height=40)

        # Detect face button from image
        img5 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\face_detector1.jpg")
        img5 =img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220, height=40)


        # Attendance button from image
        img6 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\attendance.png")
        img6 =img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220, height=40)


        # Help support button from image
        img7 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\help.jpg")
        img7 =img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.helpdesk_data)
        b1.place(x=1100,y=100,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.helpdesk_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220, height=40)



        # Train button from image
        img8 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\facetrain.jpg")
        img8 =img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220, height=40)


        # Photos button from image
        img9 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\Photos.png")
        img9 =img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220, height=40)


        # Developer from image
        img10 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\developer.jpg")
        img10 =img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220, height=40)


        # Exit from image
        img11 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\exit_1.jpg")
        img11 =img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit_button)
        b1.place(x=1100,y=380,width=220, height=220)

        #button under detailying
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_button,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220, height=40)


    # defining save image opening from the system
    def open_img(self):
        os.startfile("data")

    # defining here exit button function over here.
    def exit_button(self):
        self.exit_button=tkinter.messagebox.askyesno("Face Recognition","Are you want to exit.",parent=self.root)
        if self.exit_button>0:
            self.root.destroy()
        else:
            return

        
        
    #=====================================Function buttons=============================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)



    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    def helpdesk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpdesk(self.new_window)

    



    
        




# main file
if __name__ == "__main__":
    root=Tk()
    obj =Face_Recognition_System(root)
    root.mainloop()

