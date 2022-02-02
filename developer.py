from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2 


#class developer
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
 # title label FRONT PAGE OF SOFTWARE
        title_lbl =Label(self.root,text=" DEVELOPER",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #  top Image path of front and resizing
        img_top =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\dev.jpg")
        img_top =img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        #label for top image
        f_lbl = Label(self.root,image =self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)


        #main frame of student(upper background setellment)
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)


        #  top Image path of front and resizing
        img_top_1 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\islam.jpeg")
        img_top_1 =img_top_1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top_1=ImageTk.PhotoImage(img_top_1)
        #label for top image
        f_lbl = Label(main_frame,image =self.photoimg_top_1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # developer info
        developer_label =Label(main_frame,text="Hello I am Mukhtar Ul Islam:",font=("time new roman",16,"bold"),bg="white")
        developer_label.place(x=0,y=5)

        developer_label =Label(main_frame,text="I am AI engineer:",font=("time new roman",16,"bold"),bg="white")
        developer_label.place(x=0,y=40)

         # (Third image) Image path of front and resizing
        img2 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\student.jpg")
        img2 =img2.resize((500,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        #label
        f_lbl = Label(main_frame,image =self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=300)




if __name__ == "__main__":
    root=Tk()
    obj =Developer(root)
    root.mainloop()
