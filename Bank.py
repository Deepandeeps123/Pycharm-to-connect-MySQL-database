'''
My sql and pycharm

'''

import streamlit as st
import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='python',
    database='online'
)

st.header('WELCOME TO ABC BANK')
name=st.text_input('NAME')
password=st.text_input('PASSWORD')
email=st.text_input('EMAIL')
phno=st.number_input('PHNO',min_value=0)
balance=st.number_input('BALANCE',min_value=1000)
button=st.button('CREATE')


def add_customer(name,password,email,phno,balance):
    a=mydb.cursor()
    query='insert into customer(cname,password,email,phno,balance) values(%s,%s,%s,%s,%s)'
    a.execute(query,(name,password,email,phno,balance))
    mydb.commit()
    st.success('Account Created')



if button:
    add_customer(name,password,email,phno,balance)