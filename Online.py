import streamlit as st
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='python',
    database='online'
)


st.header('WELCOME TO OUR WEBSITE')
name=st.text_input('NAME')
password=st.text_input('PASSWORD')
email=st.text_input('EMAIL')
phno=st.number_input('PHNO',min_value=0)
button=st.button('CREATE')



def add_customer(name,password,email,phno):
    a=mydb.cursor()
    query='insert into customer(cname,password,email,phno) values(%s,%s,%s,%s)'
    a.execute(query,(name,password,email,phno))
    mydb.commit()
    st.success('Account Created')

if button:
    st.write(name,password,email,phno)
    st.success('ACCOUNT CREATED')