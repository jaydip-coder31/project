from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
import pymysql



import pymysql
from tkinter import messagebox

def connect_database():
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(host='localhost', user='root', password='Jaydip@1234')
        cursor = connection.cursor()
    except :
        messagebox.showerror('Error', f'Database connectivity issue,open mysql command line client')  
        return None,None 
    
    return cursor,connection
    
        
def create_database_table():
    cursor,connection = connect_database()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Dashboard_system')
        
        # Switch to the created database
    cursor.execute('USE Dashboard_system')

        # Create the employee_data table if it doesn't exist
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee_data (
                empid INT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                gender VARCHAR(50),
                dob VARCHAR(30),
                contact VARCHAR(30),
                employement_type VARCHAR(50),
                education VARCHAR(50),
                work_shift VARCHAR(50),
                address VARCHAR(100),
                doj VARCHAR(30),
                salary VARCHAR(50),
                usertype VARCHAR(50),
                password VARCHAR(50)
            )
        ''')

    

        # Commit the changes (important for CREATE DATABASE and CREATE TABLE)
       
   
# Call the function once to connect and set up the database


def treeview_data():
    cursor, connection = connect_database()
    if not cursor or not connection:
        return
    cursor.execute('Use Dashboard_system') 
    
    try:
        cursor.execute('SELECT * FROM employee_data')
        employee_records = cursor.fetchall()
        
        # Clear existing data in the treeview
        employee_treeview.delete(*employee_treeview.get_children())
        
        # Insert the fetched records into the treeview
        for record in employee_records:
            employee_treeview.insert('', END, values=record)
    
    except Exception as e:
        # Show error message if any exception occurs
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()



def select_data(event,empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employeement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,user_type_combobox,password_entry):
   #print('data selected')
   index = employee_treeview.selection()
   
   content = employee_treeview.item(index)
   
   row = content['values']
   clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employeement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,user_type_combobox,password_entry,False)
    
   empid_entry.insert(0, row[0])
   name_entry.insert(0, row[1])
   email_entry.insert(0, row[2])
   gender_combobox.set(row[3])
   try:
        dob = datetime.strptime(row[4], '%Y-%m-%d') if row[4] else None
        dob_date_entry.set_date(dob.strftime('%d/%m/%Y') if dob else "")
   except ValueError:
        dob_date_entry.set_date("")  # Set to blank if invalid or empty date
    # Convert dob and doj to datetime for
   contact_entry.insert(0, row[5])
   employeement_type_combobox.set(row[6]) 
   education_combobox.set(row[7])  
   work_shift_combobox.set(row[8]) 
   address_text.insert(1.0, row[9])
   try:
        doj = datetime.strptime(row[10], '%Y-%m-%d') if row[10] else None
        doj_date_entry.set_date(doj.strftime('%d/%m/%Y') if doj else "")
   except ValueError:
        doj_date_entry.set_date("")  
   salary_entry.insert(0, row[11])
   user_type_combobox.set(row[12])
   password_entry.insert(0, row[13])

   

def add_employee(empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, usertype, password):
    # Check if any required field is empty
    if (empid == '' or name == '' or email == '' or gender == 'select Gender' or contact == '' or employement_type == 'selected type' or 
        education == 'select Education' or work_shift == 'select shift' or address == '\n' or salary == '' or usertype == 'Select User Type' or password == ''):
        messagebox.showerror('Error', 'All fields are required')
        return
    
    cursor = None
    connection = None
    
    try:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        
        cursor.execute('USE Dashboard_system')

        cursor.execute('SELECT empid FROM employee_data WHERE empid = %s', (empid,))
        if cursor.fetchone():
            messagebox.showerror('Error', 'Id already exists')
            return
        
        address = address.strip()
        cursor.execute('INSERT INTO employee_data VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                       (empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, usertype, password))
        connection.commit()
        treeview_data()
        messagebox.showinfo('Success', 'Data is inserted successfully')

    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')

    finally:
        # Ensure cursor and connection are closed if they were initialized
        if cursor:
            cursor.close()
        if connection:
            connection.close()








def clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employeement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,user_type_combobox,password_entry,check):
     
     empid_entry.delete(0,END)
     name_entry.delete(0,END)
     email_entry.delete(0,END)
     gender_combobox.delete(0,END)
     from datetime import date
     dob_date_entry.set_date(date.today())
     gender_combobox.set('Select Gender')
     contact_entry.delete(0,END)
     employeement_type_combobox.set("Select Type")
     education_combobox.set("Select Education")
     work_shift_combobox.set("Select work shift")
     address_text.delete(1.0,END)
     doj_date_entry.set_date(date.today())
     salary_entry.delete(0,END)
     user_type_combobox.set("Select User Type")
     password_entry.delete(0,END)
     if check:
      employee_treeview.selection_remove(employee_treeview.selection())

 

def update_employee(empid,name,email,gender,dob,contact,employement_type,education,work_shift,address,doj,salary,usertype,password):
        selected=employee_treeview.selection()
        if not selected:
            messagebox.showerror('Error','No row is selected')

        else:
            cursor,connection=connect_database()
            if not cursor or not connection:
                 return
          
        cursor.execute('Use Dashboard_system')

        cursor.execute('SELECT * FROM employee_data WHERE empid=%s',(empid,))
        cureent_data=cursor.fetchone()
        cureent_data=cureent_data[1:]
        

        address = address.strip().replace('\n', '').replace('\r', '')
        dob = dob if isinstance(dob, str) else dob.strftime('%Y-%m-%d')  # Ensure dob is in string format
        doj = doj if isinstance(doj, str) else doj.strftime('%Y-%m-%d')  # Ensure doj is in string format

        new_data = (
        name.strip(),
        email.strip(),
        gender.strip(),
        dob,
        contact.strip(),
        employement_type.strip(),
        education.strip(),
        work_shift.strip(),
        address,
        doj,
        str(salary).strip(),
        usertype.strip(),
        password.strip()
    )
        

        new_data = (name,email,gender,dob,contact,employement_type,education,work_shift,address,doj,salary,usertype,password)
        

        if cureent_data==new_data:
            messagebox.showinfo('Information','No changes detected')
            return
        
           

        cursor.execute('UPDATE employee_data  SET name=%s,email=%s,gender=%s,dob=%s,contact=%s,employement_type=%s,education=%s,work_shift= %s,address=%s,doj=%s,salary=%s,usertype=%s,password=%s WHERE empid=%s',(name,email,gender,dob,contact,employement_type,education,work_shift,address,doj,salary,usertype,password,empid,))
        connection.commit()
        treeview_data()
        messagebox.showinfo('Success','Data is updated successfully')

def delete_employee(empid,):
     
    selected=employee_treeview.selection()
    if not selected:
            messagebox.showerror('Error','No row is selected')
    else:
        result=messagebox.askyesno('Confirm','Do you really want to  delete this record')
        if result:
         cursor,connection=connect_database()
        if not cursor or not connection:
                 return
      
        cursor.execute('Use Dashboard_system')
        cursor.execute('DELETE FROM employee_data Where empid=%s',(empid,))
        connection.commit()
        treeview_data()
        messagebox.showinfo('Success','Record is  deleted')
            

    
def search_employee(search_option, value):
    # Check if the search option is selected or value is provided
    if search_option == 'Search By':
        messagebox.showerror('Error', 'No option is selected')
        return
    elif value == '':
        messagebox.showerror('Error', 'Enter the value to search')
        return
    
    # List of valid column names to prevent SQL injection or errors
    valid_columns = ['empid', 'Name', 'email', 'gender', 'dob', 'contact', 'employement_type', 'education', 'work_shift', 'address', 'doj', 'salary', 'usertype']

    # Check if the search_option corresponds to a valid column
    if search_option not in valid_columns:
        messagebox.showerror('Error', 'Invalid search option selected')
        return

    cursor, connection = connect_database()
    if not cursor or not connection:
        return
    
    try:
        cursor.execute('USE Dashboard_system')

        # Use parameterized query to safely insert values
        query = f'SELECT * FROM employee_data WHERE {search_option} LIKE %s'
        cursor.execute(query, (f'%{value}%',))  # Passing value as a parameter

        records = cursor.fetchall()
        employee_treeview.delete(*employee_treeview.get_children())
        for record in records:
            employee_treeview.insert('', END, values=record)

    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    
    finally:
        cursor.close()
        connection.close()


def show_all(search_entry,search_combox):
    treeview_data()
    search_entry.delete(0,END)
    search_combox.set('Search By')





def employee_form(window):
  global back_image,employee_treeview
  employee_frame = Frame(window,width=1070,height=567,bg='white')
  employee_frame.place(x=200,y=100)
  heading_label = Label(employee_frame,text='Manage Employee Details',font=('times new roman',16,'bold'),bg = '#0f4d7d',fg='white')
  heading_label.place(x=0,y=0,relwidth=1)


  top_frame = Frame(employee_frame,bg='white')
  top_frame.place(x=0,y=40,relwidth=1,height=235)

  back_image = PhotoImage(file='images/back.png')
  back_button = Button(top_frame,image=back_image,bd=0,cursor='hand2',bg='white',command=lambda:employee_frame.place_forget())
  back_button.place(x=10,y=0)

  search_frame = Frame(top_frame,bg='white')
  search_frame.pack()
  search_combobox = ttk.Combobox(search_frame,values=('EmpId','Email','Name','Employement Type','Education','Work Shift'),font=('times new roman',12),state='readonly',justify=CENTER)
  search_combobox.set('Search By')
  search_combobox.grid(row=0,column=0,padx=20)

  search_entry = Entry(search_frame,font=('times new roman',12),bg='lightyellow')
  search_entry.grid(row=0,column=1,padx=20)

  search_button = Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:search_employee(search_combobox.get(),search_entry.get()))
  search_button.grid(row=0,column=2,padx=20)
    
  show_button = Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:show_all(search_entry,search_combobox))
  show_button.grid(row=0,column=3)


  horizonatal_scrollbar = Scrollbar(top_frame,orient=HORIZONTAL)
  vertical_scrollbar = Scrollbar(top_frame,orient=VERTICAL)

  employee_treeview = ttk.Treeview(top_frame,columns=('empid','name','email','gender','dob','contact','employement_type','education','work_shift','address','doj','salary','usertype'),show='headings',yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizonatal_scrollbar.set)
  horizonatal_scrollbar.pack(side=BOTTOM,fill=X)
  vertical_scrollbar.pack(side=RIGHT,fill=Y,pady=(10,0))
  horizonatal_scrollbar.config(command=employee_treeview.xview)
  vertical_scrollbar.config(command=employee_treeview.yview)

  employee_treeview.pack(pady=(10,0))

  employee_treeview.heading('empid',text='EmpId')
  employee_treeview.heading('name',text='Name')
  employee_treeview.heading('email',text='Email')
  employee_treeview.heading('gender',text='Gender')
  employee_treeview.heading('dob',text='Date of Birth')
  employee_treeview.heading('contact',text='Contact')
  employee_treeview.heading('employement_type',text='Employement Type')
  employee_treeview.heading('education',text='Education')
  employee_treeview.heading('work_shift',text='Work Shift')
  employee_treeview.heading('address',text='Address')
  employee_treeview.heading('doj',text='Date Of Joining')
  employee_treeview.heading('salary',text='Salary')
  employee_treeview.heading('usertype',text='Usertype')

  employee_treeview.column('empid',width=60)
  employee_treeview.column('name',width=140)
  employee_treeview.column('email',width=180)
  employee_treeview.column('gender',width=80)
  employee_treeview.column('contact',width=100)
  employee_treeview.column('dob',width=100)
  employee_treeview.column('employement_type',width=120)
  employee_treeview.column('education',width=120)
  employee_treeview.column('work_shift',width=100)
  employee_treeview.column('address',width=200)
  employee_treeview.column('doj',width=100)
  employee_treeview.column('salary',width=140)
  employee_treeview.column('usertype',width=120)

  treeview_data()
  employee_treeview.bind('<ButtonRelease-1>',lambda event:select_data(event,empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employeement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,user_type_combobox,password_entry))

  detail_frame = Frame(employee_frame,bg='white')
  detail_frame.place(x=20,y=280,)

  empid_label = Label(detail_frame,text='EmpId',font=('times new roman',12),bg="white")
  empid_label.grid(row=0,column=0,padx=20,pady=10,sticky ="w")
  empid_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
  empid_entry.grid(row=0,column=1,padx=20,pady=10)



  name_label = Label(detail_frame,text='Name',font=('times new roman',12),bg="white")
  name_label.grid(row=0,column=2,padx=20,pady=10,sticky ="w")
  name_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
  name_entry.grid(row=0,column=3,padx=20,pady=10)


  email_label = Label(detail_frame,text='Email',font=('times new roman',12),bg="white")
  email_label.grid(row=0,column=4,padx=20,pady=10,sticky ="w")
  email_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
  email_entry.grid(row=0,column=5,padx=20,pady=10)
      
  gender_label = Label(detail_frame,text='Gender',font=('times new roman',12),bg="white")   
  gender_label.grid(row=1,column=0,padx=20,pady=10 ,sticky ="w")

  gender_combobox = ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
  gender_combobox.set('Select Gender')
  gender_combobox.grid(row=1,column=1)



  Dob_label = Label(detail_frame,text='Date Of Birth',font=('times new roman',12),bg="white")   
  Dob_label.grid(row=1,column=2,padx=20,pady=10 ,sticky ="w")

  dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state = 'readonly',date_pattern = 'dd/mm/yyyy')
  dob_date_entry.grid(row=1,column=3)
  
  contact_label = Label(detail_frame,text='Contact',font=('times new roman',12),bg="white")   
  contact_label.grid(row=1,column=4,padx=20,pady=10,sticky ="w" )
   

  contact_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
  contact_entry.grid(row=1,column=5,padx=20,pady=10)


  employeement_type_label = Label(detail_frame,text='Employement Type',font=('times new roman',12),bg="white")   
  employeement_type_label.grid(row=2,column=0,padx=20,pady=10 ,sticky ="w")

  employeement_type_combobox = ttk.Combobox(detail_frame,values=('Full Time','Part Time','Contract'),font=('times new roman',12),width=18,state='readonly')
  employeement_type_combobox.set('Select Type')
  employeement_type_combobox.grid(row=2,column=1)


  education_label = Label(detail_frame,text='Education',font=('times new roman',12),bg="white")   
  education_label.grid(row=2,column=2,padx=20,pady=10 ,sticky ="w")
  education_option = ["B.Tech","B.Tech","M.Tech","M.Com","B.Sc","BBA","BA","LLB","M.Arch"]
  education_combobox = ttk.Combobox(detail_frame,values=education_option,font=('times new roman',12),width=18,state='readonly')
  education_combobox.set('Select Education')
  education_combobox.grid(row=2,column=3)


  work_shift_label = Label(detail_frame,text='Work Shift',font=('times new roman',12),bg="white")   
  work_shift_label.grid(row=2,column=4,padx=20,pady=10 ,sticky ="w")

  work_shift_combobox = ttk.Combobox(detail_frame,values=('Morning','Night','Evening'),font=('times new roman',12),width=18,state='readonly')
  work_shift_combobox.set('Select Work Shift')
  work_shift_combobox.grid(row=2,column=5 )

  address_label = Label(detail_frame,text='Address',font=('times new roman',12),bg="white")   
  address_label.grid(row=3,column=0,padx=20,pady=10 ,sticky ="w")
  address_text = Text(detail_frame,width=20,height=3,font=('times new roman',12),bg="light yellow")
  address_text.grid(row=3,column=1,rowspan=2)

  Doj_label = Label(detail_frame,text='Date Of Joining',font=('times new roman',12),bg="white")   
  Doj_label.grid(row=3,column=2,padx=20,pady=10 ,sticky ="w")

  doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state = 'readonly',date_pattern = 'dd/mm/yyyy')
  doj_date_entry.grid(row=3,column=3)

  user_type_label = Label(detail_frame,text='User Type',font=('times new roman',12),bg="white")   
  user_type_label.grid(row=4,column=2,padx=20,pady=10 ,sticky ="w")

  user_type_combobox = ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
  user_type_combobox.set('Select User Type')
  user_type_combobox.grid(row=4,column=3)


  salary_label = Label(detail_frame,text='Salary',font=('times new roman',12),bg="white")   
  salary_label.grid(row=3,column=4,padx=20,pady=10,sticky ="w" )
   

  salary_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
  salary_entry.grid(row=3,column=5,padx=20,pady=10)



  password_label = Label(detail_frame,text='Password',font=('times new roman',12),bg="white")   
  password_label.grid(row=4,column=4,padx=20,pady=10,sticky ="w" )
   

  password_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
  password_entry.grid(row=4,column=5,padx=20,pady=10)

  button_frame = Frame(employee_frame,bg='white')
  button_frame.place(x=200,y=520)

  add_button = Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda :add_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_date_entry.get_date(),contact_entry.get(),employeement_type_combobox.get(),education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),doj_date_entry.get_date(),salary_entry.get(),user_type_combobox.get(),password_entry.get()))
  
  add_button.grid(row=0,column=0,padx=20)
  
  update_button = Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg ='#0f4d7d' ,command=lambda:update_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_date_entry.get_date(),contact_entry.get(),employeement_type_combobox.get(),education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),doj_date_entry.get_date(),salary_entry.get(),user_type_combobox.get(),password_entry.get()))
 
  update_button.grid(row=0,column=1,padx=20)
  
  delete_button = Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg ='#0f4d7d',command= lambda:delete_employee(empid_entry.get(),
  ))
  delete_button.grid(row=0,column=2,padx=20)

  
  clear_button = Button(button_frame,text='Clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employeement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,user_type_combobox,password_entry,True))
  clear_button.grid(row=0,column=3,padx=20)
create_database_table()
