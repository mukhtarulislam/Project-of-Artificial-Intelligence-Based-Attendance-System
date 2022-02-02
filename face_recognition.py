from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2 
import os
import numpy as np
from time import strftime
from datetime import datetime


#class train
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # title label FRONT PAGE OF SOFTWARE of face recgnitions
        title_lbl =Label(self.root,text=" FACE RECOGNITION",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        # (First image) left Image path of front and resizing OF FACE RECOGNITION SYSTEM
        img_top =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\face_detector1.jpg")
        img_top =img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        #label for left image
        f_lbl = Label(self.root,image =self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)



        # (Second image) Right side Image path of front and resizing OF FACE RECOGNITION SYSTEM
        img_bottom =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\face_detetor2.jpg")
        img_bottom =img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        #label for bottom image
        f_lbl = Label(self.root,image =self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        #button in center of between two images
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("time new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=365,y=620,width=200, height=40)
    
    
    
    
    
    #=========================================Attendance function overhere===========================

    def mark_attendance(self,ftch_data_n,ftch_data_r,ftch_data_d,ftch_data_Id):
        with open("Islam.csv","r+",newline="\n") as f:
            myDataList=f.readline()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((ftch_data_Id not in name_list) and (ftch_data_r not in name_list) and (ftch_data_n not in name_list) and (ftch_data_d not in name_list)):
                now=datetime.now()
                d_ate= now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{ftch_data_Id},{ftch_data_r},{ftch_data_n},{ftch_data_d},{dtString},{d_ate},Present")
                

        
    
    
    
    
    
    
    
    #==============================face recognition ===================================#
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict =clf.predict(gray_image[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))

                db = mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
                my_cursor=db.cursor()

                my_cursor.execute("select Name from student where Student_Id="+str(id))
                ftch_data_n =my_cursor.fetchone()
                ftch_data_n="+".join(ftch_data_n)

                my_cursor.execute("select Roll_No from student where Student_Id="+str(id))
                ftch_data_r =my_cursor.fetchone()
                ftch_data_r="+".join(ftch_data_r)

                my_cursor.execute("select Dep from student where Student_Id="+str(id))
                ftch_data_d =my_cursor.fetchone()
                ftch_data_d="+".join(ftch_data_d)
                
                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                ftch_data_Id =my_cursor.fetchone()
                ftch_data_Id="+".join(ftch_data_Id)

                
                if confidence >77:
                    cv2.putText(img,f"Student Id:{ftch_data_Id}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{ftch_data_r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{ftch_data_n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{ftch_data_d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    self.mark_attendance(ftch_data_Id,ftch_data_n,ftch_data_r,ftch_data_d)
                    
                    
                    

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,"Unknown Face"(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture =cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_capture.read()
            img=recognize(img,clf,face_cascade)
            cv2.imshow("Welcome to The face Recognition",img)

            if cv2.waitKey(1)==13:
                break

            video_capture.release()
            cv2.destroyAllWindows



if __name__ == "__main__":
    root=Tk()
    obj =Face_Recognition(root)
    root.mainloop()