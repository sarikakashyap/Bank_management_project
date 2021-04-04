import tkinter as tk
from tkinter import PhotoImage
from PIL import Image ,ImageTk
import os
from tkinter import messagebox as msg


def home():

    # 1 HOME PAGE
    root_home1=tk.Tk()
    def remove():
        root_home1.destroy()
    root_home1.config(bg="#D3D3CB")
    root_home1.state("zoom")
    heading_frame = tk.Frame(width=200, height=200, background="#FFA500")
    heading_label=tk.Label(heading_frame,text="Bank Management Project")
    heading_label.config(bg="#FFA500",fg="black",font ="arial 40 bold")
    heading_label.pack(padx=20,pady=50)
    heading_frame.pack(fill="both")
    pic=Image.open("oval_button3.png")
    resize=pic.resize((300,70),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)
    register_button=tk.Button(root_home1, image=but,text="REGISTER ACCOUNT",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove(),create()])
    register_button.place(x=350,y=300)
    show_button=tk.Button(root_home1, image=but,text="SHOW ACCOUNT",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove(),show()])
    show_button.place(x=850,y=300)
    deposit_button=tk.Button(root_home1, image=but,text="DEPOSIT AMOUNT",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove(),deposit()])
    deposit_button.place(x=350,y=400)
    withdraw_button=tk.Button(root_home1, image=but,text="WITHDRAW AMOUNT",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove(),withdraw()])
    withdraw_button.place(x=850,y=400)
    money_button=tk.Button(root_home1, image=but,text="MONEY TRANSFER",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove(),money_transfer()])
    money_button.place(x=350,y=500)
    delacc_button=tk.Button(root_home1, image=but,text="DELETE ACCOUNT",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove(),delete_account()])
    delacc_button.place(x=850,y=500)
    cancel_button=tk.Button(root_home1, image=but,text="CANCEL",font="Arial 15 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",relief="flat",command=lambda:[remove()])
    cancel_button.place(x=350,y=600)

    root_home1.mainloop()


def create():

    # 2 CREATE ACCOUNT PAGE
    root_create=tk.Tk()
    root_create.state("zoom")
    root_create.config(bg="#D3D3CB")
    Create_frame=tk.Frame(height=200,width=200,bg="#FFA500")


    create_heading=tk.Label(Create_frame,text="CREATE ACCOUNT")
    create_heading.config(font="Arial 40 bold",bg="#FFA500",fg="black")
    create_heading.pack(padx=20,pady=50)
    Create_frame.pack(fill="both")

    name=tk.Label(root_create,text="User Name",font="arial 16",bg="#D3D3CB")
    name.place(x=500,y=250)
    age=tk.Label(root_create,text="Age",font="arial 16",bg="#D3D3CB")
    age.place(x=500,y=300)
    account=tk.Label(root_create,text="Account No",font="arial 16",bg="#D3D3CB")
    account.place(x=500,y=350)

    #Radio Button
    i = tk.StringVar()
    current=tk.Radiobutton(root_create,text="Current Account",value="Current Account",variable=i,font="arial 16",bg="#D3D3CB")
    current.place(x=500,y=400)
    saving=tk.Radiobutton(root_create,text="Saving Account",value="Saving Account",variable=i,font="arial 16",bg="#D3D3CB")
    saving.place(x=700,y=400)

    amount=tk.Label(root_create,text="Enter amount to start account",font="arial 16",bg="#D3D3CB")
    amount.place(x=500,y=450)
    #entry for name
    name_entry=tk.Entry(root_create,font="arial 15")
    name_entry.place(x=700,y=250)
    #enter age
    age_entry=tk.Entry(root_create,font="arial 15")
    age_entry.place(x=700,y=300)
    #enter account no.
    acc_entry=tk.Entry(root_create,font="arial 15")
    acc_entry.place(x=700,y=350)
    #enter amount
    amount_entry=tk.Entry(root_create,font="arial 15" , width=12)
    amount_entry.place(x=800,y=450)
    
    def create_function():
        #getting entry from field
        name_get=name_entry.get()
        age_get=age_entry.get()
        acc_get=acc_entry.get()
        amount_get=amount_entry.get()
        typeacc_get=i.get()
        #validation checking
        try:
                int(age_get)
        except:
                 msg.showerror("","Age should be a no" )
                 
        try:
                int(amount_get)
        except:
                 msg.showerror("","amount should be a no" )  
                  
        try:
                int(acc_get)
        except:
                 msg.showerror("","account should be a no" )
                  
                                    
        
        try:
            int(acc_get) and int(age_get) and int(amount_get)
            #creating file with account no 
            file_name=acc_get+".txt"
            path="D:/data_bankManagement/"
            #list all the file
            file_list=os.listdir(path)

            a=name_get.isalpha()

            if file_name in file_list:
                msg.showwarning("","Already Exist account")
            elif a is True or " " in name_get :                
                file_Create=acc_get+".txt"
                file_open=open(path+file_Create,"a")#open file
                #adiing content into file
                file_open.write("Name:{}\nAge:{}\n{}\nType of Account: {}".format(name_get,age_get,amount_get,typeacc_get))
                msg.showinfo("","account Created" )
            else:
                msg.showerror("","Name cannot be a number" )
        except:
            pass
        
    pic=Image.open("oval_button3.png")
    resize=pic.resize((200,40),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)

    create_button=tk.Button(root_create,image=but,text="CREATE",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda:[create_function()])
    create_button.place(x=500,y=550)

    back_button=tk.Button(root_create,image=but,text="BACK",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[root_create.destroy(),home()])
    back_button.place(x=750,y=550)

    root_create.mainloop()
  
def delete_account():
    # 3 DELETE ACCOUNT PAGE
    root_delete=tk.Tk()
    root_delete.state("zoom")
    root_delete.config(bg="#D3D3CB")
    del_frame=tk.Frame(root_delete,height=200,width=200,bg="#FFA500")
    del_heading=tk.Label(del_frame,text="DELETE ACCOUNT",font="arial 30 bold",bg="#FFA500")
    del_heading.pack(padx=20,pady=50)
    del_frame.pack(fill="both")
    acc_label=tk.Label(root_delete,text="Enter Account no.",font="arial 15",bg="#D3D3CB")
    acc_label.place(x=500,y=250)
    acc_entry=tk.Entry(root_delete,font="arial 16")
    acc_entry.place(x=700,y=250)
    
    def delete_function():

        path="D:/data_bankManagement/"
        get_acc_entry=acc_entry.get()
        file_name=get_acc_entry+".txt"
        file_list=os.listdir(path)
        if file_name in file_list:
            os.remove(path+file_name)
        else:
            msg.showerror("Error","Account not exist") 
    pic=Image.open("oval_button3.png")
    resize=pic.resize((200,40),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)
    del_button=tk.Button(root_delete,image=but,text="DELETE",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda:[delete_function()])
    del_button.place(x=500,y=325)
    back_button=tk.Button(root_delete,image=but,text="BACK",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[root_delete.destroy(),home()])
    back_button.place(x=700,y=325)
    root_delete.mainloop()
def show():

    # 4 SHOW ACCOUNT PAGE
    root_show=tk.Tk()
    root_show.state("zoom")
    root_show.config(bg="#D3D3CB")
    show_frame=tk.Frame(root_show,height=200,width=200,bg="#FFA500")
    show_heading=tk.Label(show_frame,text="SHOW ACCOUNT",font="arial 30 bold",bg="#FFA500")
    show_heading.pack(padx=20,pady=50)
    show_frame.pack(fill="both")
    acc_label=tk.Label(root_show,text="Enter Account no.",font="arial 15",bg="#D3D3CB")
    acc_label.place(x=500,y=250)
    acc_entry=tk.Entry(root_show,font="arial 16")
    acc_entry.place(x=700,y=250)
    def show_function():
        path="D:/data_bankManagement/"
        acc_get=acc_entry.get()
        file_name=acc_get+".txt"
        file_list=os.listdir(path)

        if file_name in file_list:
            #print("yes")
            file_open=open(path+file_name,"r")
            file_read=file_open.readlines()
            name=file_read[0]
            age=file_read[1]
            amount=file_read[2]
            type_acc=file_read[3]
            
            frame=tk.Frame(root_show,height=300,width=200)
            
            show_name=tk.Label(frame,text=name+"\n"+age+"\n Amount:"+amount+"\n"+type_acc,font="arial 15 bold")
            show_name.pack()
            frame.pack(fill="both",side="bottom",pady=30)

        elif acc_get=="":
            msg.showinfo("","Account no is not entered" )
        else:
            msg.showerror("Error","Invaid Account")    
   
    pic=Image.open("oval_button3.png")
    resize=pic.resize((200,40),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)
    del_button=tk.Button(root_show,image=but,text="SHOW",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda:[show_function()])
    del_button.place(x=500,y=325)
    back_button=tk.Button(root_show,image=but,text="BACK",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[root_show.destroy(),home()])
    back_button.place(x=700,y=325)


    root_show.mainloop()
def money_transfer():
        
    # 5 MONEY TRANSFER PAGE
    root_money=tk.Tk()
    root_money.state("zoom")
    root_money.config(bg="#D3D3CB")
    money_frame=tk.Frame(root_money,height=200,width=200,bg="#FFA500")
    money_heading=tk.Label(money_frame,text="MONEY TRANSFER",font="arial 30 bold",bg="#FFA500")
    money_heading.pack(padx=20,pady=50)
    money_frame.pack(fill="both")

    accsender_label=tk.Label(root_money,text="Enter Sender Account no.",font="arial 15",bg="#D3D3CB")
    accsender_label.place(x=400,y=250)
    acc_receiver_label=tk.Label(root_money,text="Enter Receiver Account no.",font="arial 15",bg="#D3D3CB")
    acc_receiver_label.place(x=400,y=300)
    acc_amount_label=tk.Label(root_money,text="Enter Amount.",font="arial 15",bg="#D3D3CB")
    acc_amount_label.place(x=400,y=350)

    accsender_entry=tk.Entry(root_money,font="arial 16")
    accsender_entry.place(x=700,y=250)
    acc_receiver_entry=tk.Entry(root_money,font="arial 16")
    acc_receiver_entry.place(x=700,y=300)
    acc_amount_entry=tk.Entry(root_money,font="arial 16")
    acc_amount_entry.place(x=700,y=350)

    def money_function():
        sender_get=accsender_entry.get()
        receiver_get=acc_receiver_entry.get()
        amount_get=acc_amount_entry.get()
        path="D:/data_bankManagement/"
        file_name1=sender_get+".txt"
        file_name2=receiver_get+".txt"
        file_list=os.listdir(path)

        if file_name1 in file_list and file_name2 in file_list and file_name1 != file_name2 and amount_get!="0" and amount_get!="" :

            file=open(path+file_name1,"r")
            file_read= file.readlines()
            amount=file_read[2]
            file_rec=open(path+file_name2,"r")
            file_read1= file_rec.readlines()
            amount_rec=file_read1[2]
            if int(amount_get)<int(amount):
                diff=int(amount)-int(amount_get)
                sum=int(amount_rec)+int(amount_get)

                f=open(path+file_name1,"rt")
                recf=open(path+file_name2,"rt")
                record_sender=f.read()
                record_receiver=recf.read()

                record_sender=record_sender.replace(amount,str(diff)+"\n")
                record_receiver=record_receiver.replace(amount_rec,str(sum)+"\n")
                f.close()
                f=open(path+file_name1,"wt")
                f.write(record_sender+"\n")
                f.close()

                f1=open(path+file_name2,"wt")
                f1.write(record_receiver+"\n")

                f1.close()
                msg.showinfo("","Transfer Successfully")
            else:
                msg.showwarning("","Balance not sufficient")
        elif file_name1 not in file_list :
            msg.showerror("","sender account not exist")    
        elif file_name2 not in file_list :
            msg.showerror("","Receiver account not exist")
        elif file_name2 == file_name1 :
            msg.showerror("","Both Account No can not be same")
        elif amount_get=="0" or amount_get=="":
            msg.showerror("","Amount Can't be zero or Blank")             
        else:
            msg.showerror("","both are invalid account") 

    pic=Image.open("oval_button3.png")
    resize=pic.resize((200,40),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)

    tran_button=tk.Button(root_money,image=but,text="TRANSFER",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda:[money_function()])
    tran_button.place(x=400,y=425)
    back_button=tk.Button(root_money,image=but,text="BACK",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[root_money.destroy(),home()])
    back_button.place(x=700,y=425)

    root_money.mainloop()

def deposit():
        
    # 6 DEPOSIT PAGE
    root_deposit=tk.Tk()
    root_deposit.state("zoom")
    root_deposit.config(bg="#D3D3CB")
    deposit_frame=tk.Frame(root_deposit,height=200,width=200,bg="#FFA500")
    deposit_heading=tk.Label(deposit_frame,text="AMOUNT DEPOSIT",font="arial 30 bold",bg="#FFA500")
    deposit_heading.pack(padx=20,pady=50)
    deposit_frame.pack(fill="both")

    acc_label=tk.Label(root_deposit,text="Enter Account no.",font="arial 15",bg="#D3D3CB")
    acc_label.place(x=450,y=300)

    acc_amount_label=tk.Label(root_deposit,text="Enter Amount.",font="arial 15",bg="#D3D3CB")
    acc_amount_label.place(x=450,y=350)

    acc_entry=tk.Entry(root_deposit,font="arial 16")
    acc_entry.place(x=750,y=300)
    acc_amount_entry=tk.Entry(root_deposit,font="arial 16")
    acc_amount_entry.place(x=750,y=350)

    def deposit_function():
        acc_get=acc_entry.get()
        acc_amount=acc_amount_entry.get()
        path="D:/data_bankManagement/"
        file_name=acc_get+".txt"
        file_list=os.listdir(path)

        if file_name in file_list:
            print("yes")
            file_open=open(path+file_name,"r")
            file_read=file_open.readlines()
            amount=file_read[2]
            if acc_amount != "0":
                sum=int(amount)+int(acc_amount)
                sum2=str(sum)
            f = open(path+file_name, "rt")
            data = f.read()
            data = data.replace(amount, sum2+"\n")
            f.close()
            f = open(path+file_name, "wt")
            f.write(data +"\n")
            f.close()

            frame=tk.Frame(root_deposit,height=300,width=200)
            
            show_details=tk.Label(frame,text=" Balance Amount:"+amount,font="arial 15 bold")
            show_details.pack()
            show_details1=tk.Label(frame,text=" After deposit Balance:"+sum2,font="arial 15 bold")
            show_details1.pack()
            frame.pack(fill="both",side="bottom",pady=40)
        elif acc_get=="" and acc_amount=="" :
            msg.showinfo("","field can't be empty" )    
        elif acc_get=="" :
            msg.showinfo("","Account no is not entered" )
        elif acc_amount=="" or acc_amount=="0"  :
            msg.showinfo("","Amount is not entered" )
            
        else:
            msg.showerror("Error","Invaid Account") 

    pic=Image.open("oval_button3.png")
    resize=pic.resize((200,40),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)

    deposit_button=tk.Button(root_deposit,image=but,text="DEPOSIT",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[deposit_function()] )
    deposit_button.place(x=450,y=425)
    back_button=tk.Button(root_deposit,image=but,text="BACK",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[root_deposit.destroy(),home()])
    back_button.place(x=750,y=425)

    root_deposit.mainloop()


def withdraw():

    # 7 WITHDRAW PAGE
    root_withdraw=tk.Tk()
    root_withdraw.state("zoom")
    root_withdraw.config(bg="#D3D3CB")
    withdraw_frame=tk.Frame(root_withdraw,height=200,width=200,bg="#FFA500")
    withdraw_heading=tk.Label(withdraw_frame,text="WITHDRAW AMOUNT",font="arial 30 bold",bg="#FFA500")
    withdraw_heading.pack(padx=20,pady=50)
    withdraw_frame.pack(fill="both")

    acc_label=tk.Label(root_withdraw,text="Enter Account no.",font="arial 15",bg="#D3D3CB")
    acc_label.place(x=450,y=300)

    acc_amount_label=tk.Label(root_withdraw,text="Enter Amount.",font="arial 15",bg="#D3D3CB")
    acc_amount_label.place(x=450,y=350)

    acc_entry=tk.Entry(root_withdraw,font="arial 16")
    acc_entry.place(x=750,y=300)
    acc_amount_entry=tk.Entry(root_withdraw,font="arial 16")
    acc_amount_entry.place(x=750,y=350)

    def withdraw_function():
        acc_get=acc_entry.get()
        acc_amount=acc_amount_entry.get()
        path="D:/data_bankManagement/"
        file_name=acc_get+".txt"
        file_list=os.listdir(path)
        
        if file_name in file_list:
            
            file_open=open(path+file_name,"r")
            file_read=file_open.readlines()
            amount=file_read[2]
            
            bal_amount=int(amount)
            if acc_amount=="" or acc_amount=="0":
                msg.showinfo("","Amount is not entered" )
            elif acc_amount != "0" and int(acc_amount)<bal_amount:
                diff=int(amount)-int(acc_amount)
                diff2=str(diff)
                f = open(path+file_name, "rt")
                data = f.read()
                data = data.replace(amount, diff2+"\n")
                f.close()
                f = open(path+file_name, "wt")
                f.write(data +"\n")
                f.close()

                frame=tk.Frame(root_withdraw,height=300,width=200)
            
                show_details=tk.Label(frame,text=" Balance Amount:"+amount,font="arial 15 bold")
                show_details.pack()
                show_details1=tk.Label(frame,text=" After withdraw Balance:"+diff2,font="arial 15 bold")
                show_details1.pack()
                frame.pack(fill="both",side="bottom",pady=40)
            elif int(acc_amount)>bal_amount:
                msg.showinfo("","Insufficient Balance:" )        
            elif acc_get=="" and acc_amount=="":
                msg.showinfo("","field can't be empty" )    
            elif acc_get=="" :
                msg.showinfo("","Account no is not entered" )
            
        

        else:
            msg.showerror("Error","Invaid Account") 

    def check():
        acc_get=acc_entry.get()
        
        path="D:/data_bankManagement/"
        file_name=acc_get+".txt"
        file_list=os.listdir(path)

        if file_name in file_list:
            print("yes")
            file_open=open(path+file_name,"r")
            file_read=file_open.readlines()
            amount=file_read[2]
            frame=tk.Frame(root_withdraw,height=300,width=200)
            
            show_details=tk.Label(frame,text=" Balance Amount:"+amount,font="arial 15 bold")
            show_details.pack()
            
            frame.pack(fill="both",side="bottom",pady=40)


    pic=Image.open("oval_button3.png")
    resize=pic.resize((200,40),Image.ANTIALIAS)
    but=ImageTk.PhotoImage(resize)

    withdraw_button=tk.Button(root_withdraw,image=but,text="WITHDRAW",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda:[withdraw_function()])
    withdraw_button.place(x=500,y=425)
    check_button=tk.Button(root_withdraw,image=but,text="CHECK BALANCE",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda:[check()])
    check_button.place(x=750,y=425)
    back_button=tk.Button(root_withdraw,image=but,text="BACK",font="Arial 12 bold",compound=tk.CENTER,borderwidth=0,bg="#D3D3CB",command=lambda :[root_withdraw.destroy(),home()])
    back_button.place(x=550,y=500)

    root_withdraw.mainloop()



    
    
home()                             
