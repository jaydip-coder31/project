from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employeee import connect_database



def delete_category(treeview):
    index = treeview.selection()
   
    
    if not index:
        messagebox.showerror('Error', 'No row is selected')
        return
    content=treeview.item(index)
    row=content['values']

    if not row:
        messagebox.showerror('Error', 'Selected row has no data')
        return
    
    id = row[0] 
    try:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return 
        cursor.execute('USE Dashboard_system')
        cursor.execute('DELETE FROM category_data WHERE Id=%s',id)
        connection.commit()
        treeview_data(treeview)
        messagebox.showinfo('info','Record is deleted')
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        connection.close()
    

def clear(Id_entry,category_name_entry,Description_text):
    Id_entry.delete(0,END)
    category_name_entry.delete(0,END)
    Description_text.delete(1.0,END)
    

def treeview_data(treeview):
   cursor,connection = connect_database()
   if not cursor or not connection:
           return
   cursor.execute('Use Dashboard_system')
   cursor.execute('select * from category_data')
   records = cursor.fetchall()
   treeview.delete(* treeview.get_children())
   for record in records:
       treeview.insert('',END,values=record)




def add_category(id, name, description,treeview):
    if id == '' or name == '' or description == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        
        try:   
            cursor.execute('USE Dashboard_system')
            cursor.execute('CREATE TABLE IF NOT EXISTS category_data (Id INT PRIMARY KEY, name VARCHAR(100), description TEXT)')
            cursor.execute('SELECT * FROM category_data WHERE Id = %s', (id,))
            if cursor.fetchone():
                messagebox.showerror('Error', 'Id already exists')
                return
            
            cursor.execute('INSERT INTO category_data (Id, name, description) VALUES (%s, %s, %s)', (id, name, description))
            
            # Commit the transaction
            connection.commit()
            
            # Show success message
            messagebox.showinfo('Info', 'Data is inserted')
            
            # Update treeview with new data
            treeview_data(treeview)
        
        except Exception as e:
            # Handle any errors
            messagebox.showerror('Error', f'Error due to {e}')
            return
        
        finally:
            # Close the cursor and connection to the database
            cursor.close()
            connection.close()


def category_form(window):
   global back_image ,logo
   category_frame=Frame(window,width=1070,height=567,bg='white')
   category_frame.place(x=200,y=100)
   heading_label = Label(category_frame,text='Manage Category Details',font=('times new roman',16,'bold'),bg = '#0f4d7d',fg='white')
   heading_label.place(x=0,y=0,relwidth=1)

   back_image = PhotoImage(file='images/back.png')
   back_button = Button(category_frame,image=back_image,bd=0,cursor='hand2',bg='white',command=lambda:category_frame.place_forget())
   back_button.place(x=10,y=35)


   logo=PhotoImage(file='images/product_category.png')
   label=Label(category_frame,image=logo,bg='white')
   label.place(x=30,y=100)

   detail_frame = Frame(category_frame,bg='white')
   detail_frame.place(x=500,y=60)

   Id_label = Label(detail_frame,text="Id",font=('times new roman ',14,'bold'),bg='white')
   Id_label.grid(row=0,column=0,padx=20,sticky='w')
   Id_entry=Entry(detail_frame,font=('times new roman ',14,'bold'),bg='lightyellow')
   Id_entry.grid(row=0,column=1)
   

   category_name_label = Label(detail_frame,text="Category Name",font=('times new roman ',14,'bold'),bg='white')
   category_name_label.grid(row=1,column=0,padx=20,sticky='w')
   category_name_entry=Entry(detail_frame,font=('times new roman ',14,'bold'),bg='lightyellow')
   category_name_entry.grid(row=1,column=1,pady=20)

   description_label = Label(detail_frame,text="Description",font=('times new roman ',14,'bold'),bg='white')
   description_label.grid(row=2,column=0,padx=20,sticky='nw')
   Description_text = Text(detail_frame,width=25,height=6,bd=2)
   Description_text.grid(row=2,column=1)

   Button_frame = Frame(category_frame,bg='white')
   Button_frame.place(x=580,y=280)


   add_button = Button(Button_frame,text='Add',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:add_category(Id_entry.get(),category_name_entry.get(),Description_text.get(1.0,END).strip(),treeview))
   add_button.grid(row=0,column=0,padx=20)


   delete_button = Button(Button_frame,text='Delete',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:delete_category(treeview) )
   delete_button.grid(row=0,column=1 ,padx=20)

   clear_button = Button(Button_frame,text='Clear',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:clear(Id_entry,category_name_entry,Description_text) )
   clear_button.grid(row=0,column=2 ,padx=20)


   treeview_frame = Frame(category_frame,bg='white')
   treeview_frame.place(x=530,y=340,height=200,width=500)


   scrolly = Scrollbar(treeview_frame,orient=VERTICAL)
   scrollx =Scrollbar(treeview_frame,orient=HORIZONTAL)
   treeview = ttk.Treeview(treeview_frame,column=('Id','Category Name','Description'),show='headings',yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
   scrolly.pack(side=RIGHT,fill=Y)
   scrollx.pack(side=BOTTOM,fill=X)

   scrollx.config(command=treeview.xview)
   scrolly.config(command=treeview.yview)


   treeview.pack(fill=BOTH,expand=1)
   
   treeview.heading('Id',text='Id')
   treeview.heading('Category Name',text='Category Name')
   treeview.heading('Description',text='Description')

   treeview.column('Id',width=80)
   treeview.column('Category Name',width=160)
   treeview.column('Description',width=300)    


   treeview_data(treeview)    
   
   
   





   


