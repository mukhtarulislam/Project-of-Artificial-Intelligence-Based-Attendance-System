import cv2
import mysql.connector
from PIL import Image, ImageTk
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



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

                
                if confidence >77:
                    cv2.putText(img,f"Roll:{ftch_data_r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{ftch_data_n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{ftch_data_d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,"Unknown Face"(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord= draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
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
