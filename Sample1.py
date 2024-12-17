import streamlit as st
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='python',
    database='project'
)

st.header('WELCOME TO ABC BANK')
name=st.text_input('NAME')
password=st.text_input('PASSWORD')
phno=st.number_input('PHNO',min_value=0)
balance=st.number_input('BALANCE',min_value=1000)
button=st.button('CREATE')