#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Restaurant management system
class RMS:
   def __init__(self,restaurant_name,menu):
       self.bill=0
       self.restaurant_name=restaurant_name
       self.menu=menu
       self.order=''
       self.amount=0
       self.ask_user=''
       self.ord_prices=[]
       self.ord_li=[]
   
   def welcome_user(self):
       #Welcome user
       return(f"Welcome to the {self.restaurant_name.title()}")
       print("*"*30)

   def display_menu(self):
       print("Menu: ")
       #suggest menu for customers
       for i in self.menu:
           print(i.title(),self.menu[i])
       print("*"*35)

   def user_order(self):
       #ask user to for his order
       self.order=input("Please Give me your order Sir/Mam?")
       #Receive order
       print(f"Okay your order is {self.order.title()}")

   def preparing_order(self):
       #Preparing order
       print(f"preparing your {self.order.title()}")
       import time
       time.sleep(3)
       self.bill=self.bill+self.menu[self.order.lower()]
       self.ord_li.append(self.order.lower())
       self.ord_prices.append(self.menu[self.order.lower()])

   def serve_order(self):
       #serve the order
       print("your order is ready!")
       print(f"Please enjoy your {self.order.title()}")

   def repeat_order(self):
       self.user_order()
       if self.order.lower() in self.menu:
           self.preparing_order()
           self.serve_order()
       else:
           print("Invalid Order")
           print("Please choose correct order from menu ")
           self.repeat_order()

   def display_bill(self):
       #display bill
       self.bill_dict=list(zip(self.ord_li,self.ord_prices))
       for i in self.bill_dict:
           print(i[0].title(),i[1])
           
       print("your bill amount is",self.bill)

   def verify_bill(self):
       #Take maount from user
       
       self.amount=int(input("Please Enter your amount here: "))

       #if the bill amount is more bill ---> give change to customer

       while self.bill >self.amount:
           self.bill=self.bill-self.amount
           print("Payment failed! please pay remaining amount of bill",self.bill)
           self.amount=int(input("Please pay your remaining amount here: "))
       if self.bill <self.amount:
           print("Take your change",self.amount-self.bill)
       else:
           pass

   def ty(self):
       print(f"Thank your for visiting {self.restaurant_name}!")
   
   def verify_repeat_order(self):
       self.ask_user=input("do you want anything else Sir/Mam?")
       self.valid_input=['yes','no']
       while self.ask_user.lower() not in self.valid_input:
           print("please write correct input yes or no")
           self.verify_repeat_order()
       
   def order_process(self):
       self.user_order()
       if  self.order.lower() in self.menu:
           self.preparing_order()
           self.serve_order()
           self.verify_repeat_order()
           
           while self.ask_user.lower()=="yes":
               self.repeat_order()
               self.verify_repeat_order()

           self.display_bill()
           self.verify_bill()
           self.ty()
       else:
           print("Invalid order")
           print("Please Enter order from menu: ")
           self.order_process()

if __name__=='__main__':
   user_input_file=open("user input.txt")
   user_input_li=user_input_file.readlines()
   rn=user_input_li[0].replace('/n','')
   food_items=user_input_li[1].replace('./','').split(',')
   food_prices=[]
   for i in user_input_li[2].split(','):
       food_prices.append(int(i))
   rm=dict(zip(food_items,food_prices))
   restaurant=RMS(restaurant_name=rn,menu=rm)
   #importing tkinter library
   import tkinter as tk
   window=tk.Tk()
   #title
   window.title("RMS")
   #geometry
   window.geometry("700x500")
   #LABEL
   tk.Label(window,text=restaurant.welcome_user(),font=("Helvetica",21,'bold'),bg="black",fg="red").pack(pady=30)
   #Button
   tk.Button(window,text='MENU',command=restaurant.display_menu,width=25,height=3,bg='black',fg='white').pack(pady=40)
   tk.Button(window,text="START ORDER",command=restaurant.order_process,width=25,height=3,fg="white",bg="black").pack(pady=40)
   #mainloop it is nessecary to wite
   window.mainloop()

                             



# In[ ]:




