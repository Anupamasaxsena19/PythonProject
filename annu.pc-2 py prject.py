from tkinter import*
import tkinter.messagebox as messagebox
from PIL import ImageTk,Image
import mysql.connector as mysql

def insert():
    id=A_id.get()
    name=A_name.get()
    phone=A_phone.get()
    account=A_account.get()
    amount=A_amount.get()
    cash_mode=var.get()
    if(id=='' or name=='' or phone=='' or cash_mode=='' or account=='' or amount==''):
        messagebox.showinfo("insert status"," all fields are required")
    else:
        con=mysql.connect(host='localhost',user='root',password='', database="bank corporation")
        cursor=con.cursor()
        cursor.execute("insert into forms values('"+id +"','"+ name +"','"+ phone +"','"+ account +"','"+amount +"','"+str(cash_mode) +"')")
        cursor.execute("commit");

        A_id.delete(0,'end')
        A_name.delete(0,'end')
        A_phone.delete(0,'end')
        A_account.delete(0,'end')
        A_amount.delete(0,'end')
        var.set(0)
        show()
        messagebox.showinfo("insert status","inserted succussfully");
        con.close();

def delete():
    if(A_id.get()==""):
        messagebox.showinfo("delete status","ID is compulsory for delete");
    else:
        con=mysql.connect(host='localhost',user='root',password='', database="bank corporation")
        cursor=con.cursor()
        cursor.execute("delete from forms where id='"+A_id.get() +"'")
        cursor.execute("commit");

        A_id.delete(0,'end')
        A_name.delete(0,'end')
        A_phone.delete(0,'end')
        A_account.delete(0,'end')
        A_amount.delete(0,'end')
        var.set("")
        show()
        messagebox.showinfo("delete status","deleted succussfully");
        con.close();

def update():
    id=A_id.get()
    name=A_name.get()
    phone=A_phone.get()
    account=A_account.get()
    amount=A_amount.get()
    cash_mode=var.get()
    if(id=='' or name=='' or phone=='' or cash_mode=='' or account==''):
        messagebox.showinfo("update status"," all fields are required")
    else:
        con=mysql.connect(host='localhost',user='root',password='', database="bank corporation")
        cursor=con.cursor()
        cursor.execute("update forms set name='"+ name +"',phone='"+ phone +"'where id='"+ id +"'")
        cursor.execute("commit");

        A_id.delete(0,'end')
        A_name.delete(0,'end')
        A_phone.delete(0,'end')
        A_account.delete(0,'end')
        A_amount.delete(0,'end')
        var.set("")
        show()
        messagebox.showinfo("update status","updated successfully");
        con.close();

def get():
    if(A_id.get()==""):
        messagebox.showinfo("fetch status"," ID is compulsory for delete")
    else:
        con=mysql.connect(host='localhost',user='root',password='', database="bank corporation")
        cursor=con.cursor()
        cursor.execute("select * from forms where id='"+ A_id.get() +"'")
        rows= cursor.fetchall();

        for row in rows:
            A_name.insert(0,row[1])
            A_phone.insert(0,row[2])
            A_account.insert(0,row[3])
            A_amount.insert(0,row[4])
            var.set(row[5])

        con.close();

def clear():
        A_id.delete(0,'end')
        A_name.delete(0,'end')
        A_phone.delete(0,'end')
        A_account.delete(0,'end')
        A_amount.delete(0,'end')
        var.set(0)
        show()
        messagebox.showinfo("clear status","clear successfully");

def deposit_money():
    amount = str(entry_deposit.get())
    current_balance = float(balance_label["text"])
    new_balance = current_balance + amount_balance_label.config(text=f"{new_balance:.2f}")
        
def withdraw_money():
    amount = str(entry_withdraw.get())
    current_balance = float(balance_label["text"])
    if current_balance >= amount:new_balance = current_balance -amount_balance_label.config(text=f"{new_balance:.2f}")
    else: error_label.config(text="Insufficient balance")
    
def show():
    con= mysql.connect (host='localhost',user='root',password='', database="bank corporation")
    cursor=con.cursor()
    cursor.execute("select * from forms")
    rows= cursor.fetchall()
    list.delete(0,list.size())

    for row in rows:
        insertdata=str(row[0])+'  '+row[1]
        list.insert(list.size()+1,insertdata)
    con.close()

root=Tk()
root.geometry('800x300')
root.title('Bank Management System')

#Add Image
bg_image=Image.open("C:\\Users\\ANIMATION4\\Pictures\\gold.jpeg")
bg_photo=ImageTk.PhotoImage(bg_image)
bg_label=Label(root,image=bg_photo)
bg_label.place(relwidth=1,relheight=1)

#Add Label
id=Label(root,text='Enter Aadhar', font=('bold',10))
id.place(x=20,y=30)

name=Label(root,text='Enter Name', font=('bold',10))
name.place(x=20,y=60)

phone=Label(root,text='Enter Phone', font=('bold',10))
phone.place(x=20,y=90)

account=Label(root,text='Enter account', font=('bold',10))
account.place(x=20,y=120)

total_balance= Label(root, text='Enter Balance: $0' ,font=('bold',10))
total_balance.place(x=20,y=150)

amount= Label(root, text='Enter amount: $0' ,font=('bold',10))
amount.place(x=20,y=180)

#Adding Entries
A_id=Entry()
A_id.place(x=160,y=30)
A_name=Entry()
A_name.place(x=160,y=60)
A_phone=Entry()
A_phone.place(x=160,y=90)
A_account=Entry()
A_account.place(x=160,y=120)
A_balance=Entry()
A_balance.place(x=160,y=150)
A_amount=Entry()
A_amount.place(x=160,y=180)

#Adding RadioButton
var=IntVar()
R1=Radiobutton(root,text='Enter cashdeposit', variable=var,value=1).place(x=20,y=220)
R2=Radiobutton(root,text='Enter cashwithdraw', variable=var,value=2).place(x=180,y=220)

#Adding Buttons
insert=Button(root,text='insert', bg='orange', command=insert)
insert.place(x=20,y=250)
delete=Button(root,text='delete', bg='white', command=delete)
delete.place(x=70,y=250)
update=Button(root,text='update', bg='sky blue', command=update)
update.place(x=120,y=250)
get=Button(root,text='get', bg='yellow', command=get)
get.place(x=180,y=250)
clear=Button(root,text='clear', bg='green', command=clear)
clear.place(x=220,y=250)

list=Listbox(root)
list.place(x=400,y=30)
show()
root.mainloop()
