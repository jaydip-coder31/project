from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql
from employeee import employee_form
from supplier  import supplier_form
from category import category_form
from product import product_form
# Functionality part

  

#GUI part
window = Tk()
window.title("Dashboard")
window.geometry("1270x668+0+0")
window.resizable(0,0)
window.config(bg="white")

bg_image = PhotoImage(file="images/inventory.png")
titleLabel = Label(window,image=bg_image,compound=LEFT,text="  Inventory Management system",font=('times new roman',40,'bold'),bg="#010c48",fg='white',anchor='w',padx=20)
titleLabel.place(x=0,y=0,relwidth=1)
logoutbutton = Button(window,text='Logout',font=('times new roman',20,'bold'))
logoutbutton.place(x=1100,y=10)
subtitleLabel = Label(window,text='Welcome Admin\t\t Date:08-07-2024\t\t Time:12:36:17 pm',font=('times new roman',15),bg="#4d636d",fg="white")
subtitleLabel.place(x=0,y=70,relwidth=1)

leftFrame = Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)
logo_image = PhotoImage(file="images/logo.png")
imageLabel = Label(leftFrame,image =logo_image)
imageLabel.pack()
menuLabel = Label(leftFrame,text="Menu",font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)

employee_img = PhotoImage(file="images/employee.png")
employee_button = Button(leftFrame,image=employee_img,compound=LEFT,text=' Employee',font=('times new roman',20,'bold'),anchor="w",padx=10,command=lambda:employee_form(window))
employee_button.pack(fill=X)

supplier_img = PhotoImage(file="images/supplier.png")
supplier_button = Button(leftFrame,image=supplier_img,compound=LEFT,text=' Supplier',font=('times new roman',20,'bold'),anchor="w",padx=10,command=lambda:supplier_form(window))
supplier_button.pack(fill=X)

category_img = PhotoImage(file="images/category.png")
category_button = Button(leftFrame,image=category_img,compound=LEFT,text=' Category',font=('times new roman',20,'bold'),anchor="w",padx=10,command=lambda:category_form(window))
category_button.pack(fill=X)

product_img = PhotoImage(file="images/product.png")
product_button = Button(leftFrame,image=product_img,compound=LEFT,text=' Product',font=('times new roman',20,'bold'),anchor="w",padx=10,command=lambda:product_form(window))
product_button.pack(fill=X)


sales_img = PhotoImage(file="images/sales.png")
sales_button = Button(leftFrame,image=sales_img,compound=LEFT,text='   Sales',font=('times new roman',20,'bold'),anchor="w",padx=10)
sales_button.pack(fill=X)

exit_img = PhotoImage(file="images/exit.png")
exit_button = Button(leftFrame,image=exit_img,compound=LEFT,text='  Exit',font=('times new roman',20,'bold'),anchor="w",padx=10)
exit_button.pack(fill=X)



emp_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
total_emp_icon = PhotoImage(file='images/total_emp.png')
total_emp_icon_Label = Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_Label.pack(pady=10)

total_emp_Label = Label(emp_frame,text="Total Employees",bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
total_emp_Label.pack()

total_emp_count_Label = Label(emp_frame,text="0",bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
total_emp_count_Label.pack()


supplier_frame = Frame(window,bg='#8E44AD',bd=3,relief=RIDGE)
supplier_frame.place(x=800,y=125,height=170,width=280)
total_supplier_icon = PhotoImage(file='images/total_sup.png')
total_supplier_icon_Label = Label(supplier_frame,image=total_supplier_icon,bg='#8E44AD')
total_supplier_icon_Label.pack(pady=10)

total_sup_Label = Label(supplier_frame,text="Total Supplier",bg='#8E44AD',fg='white',font=('times new roman',20,'bold'))
total_sup_Label.pack()

total_sup_count_Label = Label(supplier_frame,text="0",bg='#8E44AD',fg='white',font=('times new roman',20,'bold'))
total_sup_count_Label.pack()



cat_frame = Frame(window,bg='#27AE60',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
total_cat_icon = PhotoImage(file='images/total_cat.png')
total_cat_icon_Label = Label(cat_frame,image=total_cat_icon,bg='#27AE60')
total_cat_icon_Label.pack(pady=10)

total_cat_Label = Label(cat_frame,text="Total Category",bg='#27AE60',fg='white',font=('times new roman',20,'bold'))
total_cat_Label.pack()

total_cat_count_Label = Label(cat_frame,text="0",bg='#27AE60',fg='white',font=('times new roman',20,'bold'))
total_cat_count_Label.pack()


prod_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)
total_prod_icon = PhotoImage(file='images/total_cat.png')
total_prod_icon_Label = Label(prod_frame,image=total_prod_icon,bg='#2C3E50')
total_prod_icon_Label.pack(pady=10)

total_prod_Label = Label(prod_frame,text="Total Product",bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
total_prod_Label.pack()

total_prod_count_Label = Label(prod_frame,text="0",bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
total_prod_count_Label.pack()



sales_frame = Frame(window,bg='#E74C3C',bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,height=170,width=280)
total_sales_icon = PhotoImage(file='images/total_cat.png')
total_sales_icon_Label = Label(sales_frame,image=total_sales_icon,bg='#E74C3C')
total_sales_icon_Label.pack(pady=10)

total_sales_Label = Label(sales_frame,text="Total Sales",bg='#E74C3C',fg='white',font=('times new roman',20,'bold'))
total_sales_Label.pack()

total_sales_count_Label = Label(sales_frame,text="0",bg='#E74C3C',fg='white',font=('times new roman',20,'bold'))
total_sales_count_Label.pack()


window.mainloop()