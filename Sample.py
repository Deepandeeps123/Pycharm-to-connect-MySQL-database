import streamlit as st

import mysql.connector
mydb=mysql.connector.connect(

     host="Localhost",
     user="root",
     password="python",
     database='project'
)

# if mydb.is_connected():
#      print('Yes')
# else:
#      print('No')


st.header('WelCome to abc Bank')

menu=['ADD THE CUSTOMER','WITHDRAW MONEY']
# st.selectbox('OPTION',menu)    #we use to store one variable

option=st.selectbox('OPTION',menu)

if option=='ADD THE CUSTOMER':
     name=st.text_input('NAME')
     phno=st.number_input('PHNO',min_value=1)
     password=st.text_input('PASSWORD')
     balance=st.number_input('BALANCE',min_value=1000)
     button=st.button('CREATE')
     # button=st.button('SUBMIT')
elif option=='WITHDRAW MONEY':

     name = st.text_input('NAME')
     phno = st.number_input('PHNO', min_value=1)
     password = st.text_input('PASSWORD')
     balance = st.number_input('BALANCE', min_value=1000)
     button = st.button('CREATE')

def add_customer(name,phno,password,balance):
     a=mydb.cursor()
     query='insert into customer(cname,phno,password,balance) values(%s,%s,%s,%s)'
     a.execute(query,(name,phno,password,balance))
     mydb.commit()
     st.success('CUSTOMER ADD SUCESSFULLY')
if button:
    add_customer(name,phno,password,balance)

     # st.success('CUSTOMER ADD SUCESSFULLY')
     # st.warning('CUSTOMER ADD SUCESSFULLY')











