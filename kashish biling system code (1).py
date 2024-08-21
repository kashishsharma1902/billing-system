import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='KazuhaAnemo',database='biling_management')
if conn.is_connected():
      print('succesfully conected')
c1=conn.cursor()
c1.execute('create table customer_details(customer_name varchar(50) primary key,product_name varchar(60))')
print('table created')
c1.execute('create table order_placement(customr_name varchar(50),product_name varchar(50),demanding_quantity int(9))')
print('table created')
c1.execute('create table order_details(customer_name varchar(50),mobile_number int(10),adress varchar(999),date_to_deliver char(999))')
print('table created')
c1.execute('create table cancelation_of_order(customer_name varchar(50),order_number int(15),products_contained varchar(90),reason_for_cancelling varchar(90),confirm_cancelation varchar(20))')
print('table created')


from sys import exit
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='KazuhaAnemo',database='biling_management')
if conn.is_connected():
      print('succesfully conected')
c1=conn.cursor()
print('marketing system and sales system')
print("1.login")
print("2.exit")
choice=int(input("enter your choice"))
if choice==1:
      name=input("enter the user name:")
      passwd=input("enter the password:")
      while name=='kashish' and passwd=='chandu' :
            print('welcome')
            print('1. registry for customer ')
            print('2.registry for order placement')
            print('3.modify the order details')
            print('4.registry for cancelation of order')
            print('5.display the customer details')
            print('6.EXIT')
          
            choice=int(input('enter your choice'))
            if choice==1:
                  customer_name=input('enter the customer name:')
                  product_name=input('enter the product name:')
                  sql_insert="insert into customer_details values(""'"+customer_name+"'," "'"+product_name+"'"")"
                  c1.execute(sql_insert)
                  conn.commit()
                  print('SUCCESSFULLY REGISTERD')

      


            elif choice==2: 
                 customer_name=input('enter the customer name:')
                 product_name=input('enter the product name:')
                 demanding_quantity=input('enter tne quantity:')
                 sql_insert="insert into order_placement values(""'"+customer_name+"'," "'"+product_name+"'," "'"+demanding_quantity+"'"")"
                 c1.execute(sql_insert)
                 conn.commit()
                 print('successfully registerd')

            elif choice==3:
                 customer_name=input('enter the customer name:')
                 mobile_number=input('enter mobile number:')
                 adress=input('enter your adress:')
                 date_to_deliver=input('enter the date:')
                 sql_insert="insert into order_details values(""'"+customer_name+"'," "'"+mobile_number+"'," "'"+adress+"'," "'"+date_to_deliver+"'"")"
                 c1.execute(sql_insert)
                 conn.commit()
                 print('SUCCESSFULLY REGISTERD')
      
      
            elif choice==4:
                 customer_name=input('enter tthe customer name:')
                 order_number=input('enter tyhe order number:')
                 products_contained=input('enter the product contained in your order:')
                 reason_for_cancelation=input('enter the reason for cancelling the order:')
                 confirm_cancelation=input('say YES or NO:')
                 sql_insert="insert into cancelation_of_order values(""'"+customer_name+"'," "'"+order_number+"'," "'"+products_contained+"'," "'"+reason_for_cancelation+"',""'"+confirm_cancelation+"'"")"
                 c1.execute(sql_insert)
                 conn.commit()
                 print('SUCCESSFULLY REGISTERD')

            elif choice==5:
                sql_s="select*from customer_details"
                c1.execute(sql_s)
                a=c1.fetchall()
                for i in a:
                      print(i)
                      break
                  
            elif choice==6:
                print('visit again')
                print('')
                print('thank you')
                  

                  
                  
      else:
            print('sorry')
      
