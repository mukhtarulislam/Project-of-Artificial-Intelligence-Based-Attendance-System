
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2 
import os
import csv
from tkinter import filedialog



#=============================global varibale==============================================
mydata=[]


#class Attendance
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")

        #===================variable=======================

        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
        



        # (first image)Image path of front and resizing
        img =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\smart-attendance.jpg")
        img =img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        #label
        f_lbl = Label(self.root,image =self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        # (Second image)Image path of front and resizing
        img1 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\clg.jpg")
        img1 =img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        #label
        f_lbl = Label(self.root,image =self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        
        # Background image of system
        img3 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\bg.jpg")
        img3 =img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        #label
        bg_img = Label(self.root,image =self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)


        # title label
        title_lbl =Label(bg_img,text=" ATTENDANCE MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #main frame of student(upper background setellment)
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left side label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width =730,height=580)

        # (left side label image) Image path of front and resizing
        img_left =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\student.jpg")
        img_left =img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        #label
        f_lbl = Label(left_frame,image =self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        

        #main frame of student(upper background setellment)
        lef_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        lef_inside_frame.place(x=0,y=135,width=720,height=370)




        # label and entry(Attendance id) of left sid
        attendance_Id_label= Label(lef_inside_frame,text="Attendance Id:",font=("time new roman",13,"bold"),bg="white")
        attendance_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        # attendance entry fill 
        attendance_Id_entry =ttk.Entry(lef_inside_frame,width=20,textvariable=self.var_attend_id,font=("time new roman",12,"bold"))
        attendance_Id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

       
        # Roll (left label frame inside)
        Roll_label =Label(lef_inside_frame,text="Roll:",font=("time new roman",13,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=4,pady=8)
        # Name entry  fill(name) 
        Roll_entry =ttk.Entry(lef_inside_frame,width=20,textvariable=self.var_attend_roll,font=("time new roman",12,"bold"))
        Roll_entry.grid(row=0,column=3,padx=4,pady=8)

        # Name (left label frame inside)
        Name_label =Label(lef_inside_frame,text="Name:",font=("time new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=4,pady=8)
        # date entry  fill(name) 
        Name_entry =ttk.Entry(lef_inside_frame,width=20,textvariable=self.var_attend_name,font=("time new roman",12,"bold"))
        Name_entry.grid(row=1,column=1,padx=4,pady=8)



        #Department (left label frame inside)
        Department_label =Label(lef_inside_frame,text="Department:",font=("time new roman",13,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=4,pady=8)
        #Department entry  fill(name) 
        Department_entry =ttk.Entry(lef_inside_frame,width=20,textvariable=self.var_attend_dep,font=("time new roman",12,"bold"))
        Department_entry.grid(row=1,column=3,padx=4,pady=8)



        #Time (left label frame inside)
        Time_label =Label(lef_inside_frame,text="Time:",font=("time new roman",13,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=4,pady=8)
        #Time entry  fill(name) 
        Time_entry =ttk.Entry(lef_inside_frame,width=20,textvariable=self.var_attend_time,font=("time new roman",12,"bold"))
        Time_entry.grid(row=2,column=1,padx=4,pady=8)


        #Date (left label frame inside)
        Date_label =Label(lef_inside_frame,text="Date:",font=("time new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=4,pady=8)
        #Date entry  fill(name) 
        Date_entry =ttk.Entry(lef_inside_frame,width=20,textvariable=self.var_attend_date,font=("time new roman",12,"bold"))
        Date_entry.grid(row=2,column=3,padx=4,pady=8)


        #Attendance (left label frame inside)
        Attendance_label =Label(lef_inside_frame,text="Attendance Status:",font=("time new roman",13,"bold"),bg="white")
        Attendance_label.grid(row=3,column=0,padx=4,pady=8)
        # attendance comobo box  fill(name) 
        self.attend_status=ttk.Combobox(lef_inside_frame,textvariable=self.var_attend_attendance,font=("time new roman",13,"bold"),state="read only",width=18)
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.current(0)
        self.attend_status.grid(row=3,column =1,padx=4,pady=8)


        # Buttons Frame insid left side
        btn_frame = Frame(lef_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=300,width =715,height=35)

        # import csv button
        import_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        import_btn.grid(row=0,column=0)

        # export csv button
        export_btn=Button(btn_frame,text="Export Csv",command=self.exportCsv,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        export_btn.grid(row=0,column=1)


        # update button
        update_btn=Button(btn_frame,text="Update",width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        update_btn.grid(row=0,column=2)


        # Reset button
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Reset_btn.grid(row=0,column=3)


        


        #Right side label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width =720,height=580)

        # Buttons Frame insid right side
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width =700,height=455)











        #==================scrollbar and table=================================
        #scroll bar right side inside the table frame

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        #hidder show
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        #show for heading
        self.AttendanceReportTable["show"]="headings"

         # bind all update data in software
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #pack all heading in table
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

         #setting of width of right side frame 
        self.AttendanceReportTable.column("id",width=20)
        self.AttendanceReportTable.column("roll",width=20)
        self.AttendanceReportTable.column("name",width=20)
        self.AttendanceReportTable.column("department",width=20)
        self.AttendanceReportTable.column("time",width=20)
        self.AttendanceReportTable.column("date",width=20)
        self.AttendanceReportTable.column("attendance",width=20)




        #======================fetch data========================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #===================import csv function============================
    def importCsv(self):
        global mydata
        mydata.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)


    #===================export csv function============================ 

    def exportCsv(self):
      try:
        if len(mydata) <1:
            messagebox.showerror("No Data","No data found to export",parent=self.root)
            return False
        file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name,"w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your are data exported to"+os.path.basename(file_name)+"Successfully")

      except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root )


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_name.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])



    #=================Reset button or reset function working on curent detail store to reset===================
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_name.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
        

        
        
        

        




if __name__ == "__main__":
    root=Tk()
    obj =Attendance(root)
    root.mainloop()
