from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2 
import os
import numpy as np


#class train
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x7900+0+0")
        self.root.title("Face Recognition System")


        # title label FRONT PAGE OF SOFTWARE
        title_lbl =Label(self.root,text=" TRAIN DATASET",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #  top Image path of front and resizing
        img_top =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\facial-recognition.png")
        img_top =img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        #label for top image
        f_lbl = Label(self.root,image =self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)


        #button in center of between two images
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("time new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=380,width=1530, height=60)




        #  Bottom Image path of front and resizing
        img_bottom =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\bottom face.jpg")
        img_bottom =img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        #label for bottom image
        f_lbl = Label(self.root,image =self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)



    # ==============================Training the data with new function and lbph algorithm===================================================
    def train_classifier(self):
        data_directory =("data")
        path=[os.path.join(data_directory,file) for file in os.listdir(data_directory)]


        faces=[]
        ids=[]
        
        for image in path:
            img =Image.open(image).convert('L') # Gray scale image
            image_np =np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(image_np)
            ids.append(id)

            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==========================Train the classifier and save===========================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data set completed!!")


         


        






if __name__ == "__main__":
    root=Tk()
    obj =Train(root)
    root.mainloop()
