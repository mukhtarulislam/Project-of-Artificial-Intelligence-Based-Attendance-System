from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2 


#class Helpdesk
class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
 # title label FRONT PAGE OF SOFTWARE
        title_lbl =Label(self.root,text=" HELP DESK",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


#  top Image path of front and resizing
        img_top_1 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\helpdesk.jpeg")
        img_top_1 =img_top_1.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top_1=ImageTk.PhotoImage(img_top_1)
        #label for top image
        f_lbl = Label(self.root,image =self.photoimg_top_1)
        f_lbl.place(x=0,y=55,width=1530,height=720)

# helpdesk label info of email
        email_label =Label(f_lbl,text="Email:Mukhtarulislam88@gmail.com",font=("time new roman",16,"bold"),bg="white")
        email_label.place(x=550,y=220)







if __name__ == "__main__":
    root=Tk()
    obj =Helpdesk(root)
    root.mainloop()
