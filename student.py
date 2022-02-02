from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2 


#class student
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")


        #-----==================Variables===============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        self.var_radio1=StringVar()
        





        # (first image)Image path of front and resizing
        img =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\College-Students.jpg")
        img =img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        #label
        f_lbl = Label(self.root,image =self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # (Second image)Image path of front and resizing
        img1 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\clg.jpg")
        img1 =img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        #label
        f_lbl = Label(self.root,image =self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # (Third image) Image path of front and resizing
        img2 =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\student.jpg")
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
        title_lbl =Label(bg_img,text=" STUDENT MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #main frame of student(upper background setellment)
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)


        #left side label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width =730,height=580)


        # (left side label image) Image path of front and resizing
        img_left =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\student.jpg")
        img_left =img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        #label
        f_lbl = Label(left_frame,image =self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course Information (left label frame inside)
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width =720,height=150)

        #department (left label frame inside)
        dep_label= Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        #department combo (left label frame inside)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer Science","Medical Science")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)
        dep_combo.grid(row=0,column =1,padx=2,pady=10)

        #Course (left label frame inside)
        Course_label= Label(current_course_frame,text="Course",font=("time new roman",12,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10)
        #Course combo (left label frame inside)
        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",13,"bold"),state="read only",width=20)
        Course_combo["values"]=("Select Course","BCA","BUMS","MBBS","B.TECH","M.TECH","MCA")
        Course_combo.current(0)
        Course_combo.grid(row=0,column =3,padx=2,pady=10,sticky=W)


        #year (left label frame inside)
        Year_label= Label(current_course_frame,text="Year",font=("time new roman",13,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        #year combo (left label frame inside)
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",13,"bold"),state="read only",width=20)
        Year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1,column =1,padx=2,pady=10,sticky=W)


        #Semester (left label frame inside)
        Semester_label= Label(current_course_frame,text="Semester",font=("time new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        #Semester combo (left label frame inside)
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",13,"bold"),state="read only",width=20)
        Semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column =3,padx=2,pady=10,sticky=W)



        #Class student Information (left label frame inside)
        Class_student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        Class_student_frame.place(x=5,y=250,width =720,height=300)
        
        #Class label(Student id) (left label frame inside)
        StudentId_label= Label(Class_student_frame,text="Student ID:",font=("time new roman",13,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        # student entry fill 
        StudentId_entry =ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=20,font=("time new roman",12,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # student Name (left label frame inside)
        Student_Name_label =Label(Class_student_frame,text="Student Name:",font=("time new roman",13,"bold"),bg="white")
        Student_Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        # student entry  fill(name) 
        StudentName_entry =ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=20,font=("time new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # Class Division (left label frame inside)
        Class_div_label =Label(Class_student_frame,text="Class Division:",font=("time new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #Division combo (left label frame inside)
        Division_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font=("time new roman",13,"bold"),state="read only",width=18)
        Division_combo["values"]=("Select","First","Second","Third")
        Division_combo.current(0)
        Division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        


        # Roll No (left label frame inside)
        Roll_no_label =Label(Class_student_frame,text="Roll No:",font=("time new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        # Roll No entry  fill(name) 
        Roll_no_entry =ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("time new roman",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        
        # Gender (left label frame inside)
        Gender_label =Label(Class_student_frame,text="Gender:",font=("time new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        # gender entry  fill(name) 
        #Gender_entry =ttk.Entry(Class_student_frame,textvariable=self.var_gender,width=20,font=("time new roman",12,"bold"))
        #Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Gender combo (left label frame inside)
        Gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("time new roman",13,"bold"),state="read only",width=18)
        Gender_combo["values"]=("Select Gender","Male","Female","Transgender")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)




        # DOB (left label frame inside)
        Dob_label =Label(Class_student_frame,text="DOB:",font=("time new roman",13,"bold"),bg="white")
        Dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        # DOB entry  fill(name) 
        Dob_entry =ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("time new roman",12,"bold"))
        Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        

        # Email (left label frame inside)
        Email_label =Label(Class_student_frame,text="Email:",font=("time new roman",13,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        # Email entry  fill(name) 
        Email_entry =ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("time new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # Phone Number (left label frame inside)
        Phone_label =Label(Class_student_frame,text="Phone Number:",font=("time new roman",13,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        # Phone Number entry  fill(name) 
        Phone_entry =ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("time new roman",12,"bold"))
        Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        

        # Address (left label frame inside)
        Address_label =Label(Class_student_frame,text="Address:",font=("time new roman",13,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        # Address entry  fill(name) 
        Address_entry =ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("time new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        # Teacher name (left label frame inside)
        Teacher_label =Label(Class_student_frame,text="Teacher Name:",font=("time new roman",13,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        # Teacher name entry  fill(name) 
        Teacher_entry =ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=20,font=("time new roman",12,"bold"))
        Teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)





        # Radio Button for take photo sample
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text='Take photo sample',value='Yes')
        radionbtn1.grid(row=6,column=0)
        # Radio Button for take No photo sample
       
        radionbtn2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text='No photo sample',value='No')
        radionbtn2.grid(row=6,column=1)

        # Buttons Frame insid left side
        btn_frame = Frame(Class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width =715,height=35)

        # save button
        save_btn=Button(btn_frame,text="Save",command = self.add_data,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        save_btn.grid(row=0,column=0)

        # Update button
        Update_btn=Button(btn_frame,text="Update",command = self.update_data,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Update_btn.grid(row=0,column=1)


        # Deleted button
        Deleted_btn=Button(btn_frame,text="Deleted",command=self.delete_data,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Deleted_btn.grid(row=0,column=2)


        # Reset button
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Reset_btn.grid(row=0,column=3)



         # Buttons Frame for photo sample  insid left side
        btn_frame1 = Frame(Class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=0,y=235,width =715,height=70)

        

        # Take photo sample  button
        Take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Take_photo_btn.grid(row=0,column=0)
        # take photo sample update button
        update_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("time new roman",12,"bold"),bg='blue',fg='White')
        update_btn.grid(row=0,column=1)


        
        
        

        
        #Right side label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width =700,height=580)

        #Right side image 
        img_right =Image.open(r"C:\Users\Mukhtar ul Islam\2021 tutorial\project of artificial intelligence\Advance attendance based gui\img\clg.jpg")
        img_right =img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        #label
        f_lbl = Label(Right_frame,image =self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #===================Search System++++++++++++++++++++


        # Search frame  (right label frame inside)
        Search_frame =LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System:",font=("time new roman",13,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)
        #Search label  (right label frame inside)
        Search_label =Label(Search_frame,text="Search By:",font=("time new roman",15,"bold"),bg="red",fg='white')
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #Search Cambo pack  (right label frame inside)
        Search_combo=ttk.Combobox(Search_frame,font=("time new roman",13,"bold"),state="read only",width=15)
        Search_combo["values"]=("Select ","Roll_No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column =1,padx=2,pady=10,sticky=W)

        # Search entry  fill(name) 
        Search_entry =ttk.Entry(Search_frame,width=15,font=("time new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        # search button
        Search_btn=Button(Search_frame,text="Search",width=11,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Search_btn.grid(row=0,column=3,padx=4)
        # Show all  button
        Show_all_btn=Button(Search_frame,text="Show All",width=11,font=("time new roman",12,"bold"),bg='blue',fg='White')
        Show_all_btn.grid(row=0,column=4,padx=4)

        # ==============================Table Frame=====================================

        #table frame right side of se
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        #scroll bar right side inside the table frame

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #hidder show
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone_no")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        #show for heading
        self.student_table["show"]="headings"
        
        #setting of width of right side frame 
        self.student_table.column("dep",width=20)
        self.student_table.column("course",width=20)
        self.student_table.column("year",width=20)
        self.student_table.column("sem",width=20)
        self.student_table.column("id",width=20)
        self.student_table.column("name",width=20)
        self.student_table.column("roll",width=20)
        self.student_table.column("gender",width=20)
        self.student_table.column("div",width=20)
        self.student_table.column("dob",width=20)
        self.student_table.column("email",width=20)
        self.student_table.column("phone",width=20)
        self.student_table.column("address",width=20)
        self.student_table.column("teacher",width=20)
        self.student_table.column("photo",width=20)
        
        #pack all heading in table
        self.student_table.pack(fill=BOTH,expand=1)

        # bind all update data in software
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        # calling fetch data function over here
        self.fetch_data()

    #=================================Function Declaration======================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                db = mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
                my_cursor=db.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                

                                                                                        ))
                db.commit()
                self.fetch_data()
                db.close()
                messagebox.showinfo("Success","Student details add successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root )
           

    #==================== fetching the data from database into software================
    def fetch_data(self):
        db = mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
        my_cursor=db.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            db.commit()
        db.close()


    #======================Get coursor to update enter value of data base======================================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data_1 = content["values"]

        self.var_dep.set(data_1[0])
        self.var_course.set(data_1[1])
        self.var_year.set(data_1[2])
        self.var_semester.set(data_1[3])
        self.var_std_id.set(data_1[4])
        self.var_std_name.set(data_1[5])
        self.var_div.set(data_1[6])
        self.var_roll.set(data_1[7])
        self.var_gender.set(data_1[8])
        self.var_dob.set(data_1[9])
        self.var_email.set(data_1[10])
        self.var_phone.set(data_1[11])
        self.var_address.set(data_1[12])
        self.var_teacher.set(data_1[13])
        self.var_radio1.set(data_1[14])

    #=================updata(button) update function using values already input values========================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update again this student details",parent=self.root)
                if Update > 0:
                    db = mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
                    my_cursor=db.cursor()
                    my_cursor.execute("Update student set Dep=%s , Course=%s , Year=%s , Semester=%s , Name=%s, Division=%s ,Roll_No=%s , Gender=%s , Dob=%s , Email=%s , Phone=%s ,Address=%s , Teacher=%s , PhotoSample=%s where Student_Id=%s",(
                                                                                                                            
                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.var_std_name.get(),
                                                                                                                            self.var_div.get(),
                                                                                                                            self.var_roll.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_teacher.get(),
                                                                                                                            self.var_radio1.get(), 
                                                                                                                            self.var_std_id.get()
                                                                                        
                                                                                                                           
                                                                                                                         ))
                
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                db.commit()
                self.fetch_data()
                db.close( )

            except Exception as es:
                messagebox.showerror("Error" f"Due To:{str(es)}",parent =self.root)


    #================== Deleted(button) and function working inside the software=========
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student must be required!",parent= self.root)
        else:
            try:
                delete= messagebox.askyesno("Student Deleted page","Do you want to deleted this student details",parent=self.root)
                if delete>0:
                    db = mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
                    my_cursor=db.cursor()
                    sql="delete from student where Student_id =%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                db.commit()
                self.fetch_data()
                db.close( )
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error" f"Due To:{str(es)}",parent =self.root)

    
    
    
    #=================Reset button or reset function working on curent detail store to reset===================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")                                                                                                                  


    #==========================Open cv working code and generate data set of photo sample-=========================================             

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                db = mysql.connector.connect(host="localhost",user="root",password ="",database="face_recognizier")
                my_cursor=db.cursor()
                my_cursor.execute("Select * from student")
                my_result=my_cursor.fetchall()
                
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s , course=%s , Year=%s , Semester=%s , Name=%s , Division=%s ,Roll_No=%s , Gender=%s , Dob=%s , Email=%s , Phone=%s ,Address=%s , Teacher=%s , PhotoSample=%s where Student_Id=%s",(
                                                                                                                            
                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.var_std_name.get(),
                                                                                                                            self.var_div.get(),
                                                                                                                            self.var_roll.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_teacher.get(),
                                                                                                                            self.var_radio1.get(), 
                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                     ))
                
                db.commit()
                self.fetch_data()
                self.reset_data()
                db.close()

                #=============Load predefined data on face frontal from opencv====================================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    # scaling factor =1.3
                    #Minimum Neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped

                # For opening web camera(0), for other value differ
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id =0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face =cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path ="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set completed")
            except Exception as es:
                messagebox.showerror("Error" f"Due To:{str(es)}",parent=self.root)
              
                
                                                                                        

if __name__ == "__main__":
    root=Tk()
    obj =Student(root)
    root.mainloop()

