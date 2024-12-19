from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employeee import connect_database


def treeview_data(treeview):

  cursor,connection = connect_database()
  if not cursor or not connection:
           return
  cursor.execute('Use Dashboard_system')
  cursor.execute('select * from product_data')
  records = cursor.fetchall()
  treeview.delete(* treeview.get_children())
  for record in records:
       treeview.insert('',END,values=record)
    


def fetch_supplier_category(category_combobox,supplier_combobox):
  category_option = []
  supplier_option = [] 
  cursor,connection=connect_database()
  if not cursor or not connection:
    return
  cursor.execute('USE Dashboard_system')
  cursor.execute('SELECT name from category_data ')
  names=cursor.fetchall()
  if len(names)>0:
    category_combobox.set('Select')
  for name in names:
    category_option.append(name[0])
  category_combobox.config(values=category_option )

  cursor.execute('SELECT name from suppplier_data ')
  names=cursor.fetchall()
  if len(names)>0:
    supplier_combobox.set('Select ')

  for name in names:
    supplier_option.append(name[0])
  supplier_combobox.config(values=supplier_option)
  



def add_product(category,supplier,name,price,quantity,status,treeview):
  if category=='Select':
    messagebox.showerror('Error','Please add categories')
  elif supplier=='Select':
    messagebox.showerror('Error','Please  add supplier')

  elif category=='Select' or supplier=='Select' or name==''or price==''or quantity==''or status=='Select Status':
    messagebox.showerror('Error','All fields are required')

  else :
    cursor,connection=connect_database()
  if not cursor or not connection:
    return
  cursor.execute('USE Dashboard_system')
  cursor.execute('CREATE TABLE IF NOT EXISTS product_data(id INT AUTO_INCREMENT PRIMARY KEY ,category VARCHAR(100),supplier VARCHAR(100),name VARCHAR(100),price DECIMAL(10,2),quantity INT ,status VARCHAR(50))')
  cursor.execute('INSERT INTO product_data(category,supplier,name,price,quantity,status) VALUES(%s,%s,%s,%s,%s,%s)',(category,supplier,name,price,quantity,status))
  connection.commit()
  messagebox.showinfo('Succes','Data is added Succesfully ')
  treeview_data(treeview)








def product_form(window):
  global back_image
  product_frame=Frame(window,width=1070,height=567,bg='white')
  product_frame.place(x=200,y=100)
  
  

  
  back_image = PhotoImage(file='images/back.png')
  back_button = Button(product_frame,image=back_image,bd=0,cursor='hand2',bg='white',command=lambda:product_frame.place_forget())
  back_button.place(x=10,y=0)

  left_frame = Frame(product_frame,bg='white',bd=2,relief=RIDGE)
  left_frame.place(x=20,y=40)
  heading_label = Label(left_frame,text='Manage Product Details',font=('times new roman',16,'bold'),bg = '#0f4d7d',fg='white')
  heading_label.grid(row=0,columnspan=2,sticky='we')

  category_label = Label(left_frame,text="Category",font=('times new roman ',14,'bold'),bg='white')
  category_label.grid(row=1,column=0,padx=20,sticky='w')
  category_combobox = ttk.Combobox(left_frame,font=('times new roman ',14,'bold'),width=18,state='readonly')
  category_combobox.grid(row=1,column=1,pady=40)
  category_combobox.set('Empty')

  supplier_label = Label(left_frame,text="Supplier",font=('times new roman ',14,'bold'),bg='white')
  supplier_label.grid(row=2,column=0,padx=20,sticky='w')
  supplier_combobox = ttk.Combobox(left_frame,font=('times new roman ',14,'bold'),width=18,state='readonly')
  supplier_combobox.grid(row=2,column=1)
  supplier_combobox.set('Empty')


  name_label = Label(left_frame,text="Name",font=('times new roman ',14,'bold'),bg='white')
  name_label.grid(row=3,column=0,padx=20,sticky='w')
  name_entry=Entry(left_frame,font=('times new roman ',14,'bold'),bg='lightyellow')
  name_entry.grid(row=3,column=1,pady=40)

  price_label = Label(left_frame,text="Price",font=('times new roman ',14,'bold'),bg='white')
  price_label.grid(row=4,column=0,padx=20,sticky='w')
  price_entry=Entry(left_frame,font=('times new roman ',14,'bold'),bg='lightyellow')
  price_entry.grid(row=4,column=1)


  quantity_label = Label(left_frame,text="Quantity",font=('times new roman ',14,'bold'),bg='white')
  quantity_label.grid(row=5,column=0,padx=20,sticky='w')

  quantity_entry=Entry(left_frame,font=('times new roman ',14,'bold'),bg='lightyellow')
  quantity_entry.grid(row=5,column=1,pady=40)

  status_label = Label(left_frame,text="Status",font=('times new roman ',14,'bold'),bg='white')
  status_label.grid(row=6,column=0,padx=20,sticky='w')
  status_combobox = ttk.Combobox(left_frame,values=('Active','Inactive'),font=('times new roman ',14,'bold'),width=18,state='readonly')
  status_combobox.grid(row=6,column=1)
  status_combobox.set('Select Status')

  button_frame = Frame(left_frame,bg='white')
  button_frame.grid(row=7,columnspan=2,pady=(30,10))

  add_button = Button(button_frame,text='Add',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',command=lambda:add_product(category_combobox.get(),supplier_combobox.get(),name_entry.get(),price_entry.get(),quantity_entry.get(),status_combobox.get(),treeview))
  add_button.grid(row=0,column=0,padx=10,)


  update_button = Button(button_frame,text='Update',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',)
  update_button.grid(row=0,column=1,padx=10)


  delete_button = Button(button_frame,text='Delete',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',)
  delete_button.grid(row=0,column=2,padx=10)

  clear_button = Button(button_frame,text='Clear',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',)
  clear_button.grid(row=0,column=3,padx=10)

  search_frame = LabelFrame(product_frame,text='Search Product',font=('times new roman',14,'bold'),bg='white')
  search_frame.place(x=480,y=30)

  search_combobox = ttk.Combobox(search_frame,values=('Category','Supplier','Name','Status'),state='readonly',width=16,)
  search_combobox.grid(row=0,column=0,padx=10)
  search_combobox.set('Search By')


  search_entry=Entry(search_frame,font=('times new roman ',14,'bold'),bg='lightyellow',width=16)
  search_entry.grid(row=0,column=1)

  search_button = Button(search_frame,text='Search',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',)
  search_button.grid(row=0,column=2,padx=(10,0),pady=10)


  showall_button = Button(search_frame,text='Show All',font=('times new roman',14),width=8,cursor='hand2',fg='white',bg ='#0f4d7d',)
  showall_button.grid(row=0,column=3,padx=10)


  treeview_frame = Frame(product_frame,bg='white')
  treeview_frame.place(x=480,y=125,width=570,height=430)


  scrolly = Scrollbar(treeview_frame,orient=VERTICAL)
  scrollx =Scrollbar(treeview_frame,orient=HORIZONTAL)

  treeview = ttk.Treeview(treeview_frame,column=('id','category','supplier','name','price','quantity','status'),show='headings',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
  scrolly.pack(side=RIGHT,fill=Y)
  scrollx.pack(side=BOTTOM,fill=X)

  scrollx.config(command=treeview.xview)
  scrolly.config(command=treeview.yview)


  treeview.pack(fill=BOTH,expand=1)
  
  treeview.heading('id',text='Id')
  treeview.heading('category',text='Category')
  treeview.heading('supplier',text='Supplier')
  treeview.heading('name',text='Product Name')
  treeview.heading('price',text='Price')
  treeview.heading('quantity',text='Quanity')
  treeview.heading('status',text='Status')

  fetch_supplier_category(category_combobox,supplier_combobox)
  treeview_data(treeview)

   




  