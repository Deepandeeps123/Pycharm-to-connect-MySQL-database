import streamlit as st
import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='python',
    database='project'
)


def add_customer(name,password,phno,balance):
    a=mydb.cursor()
    query='insert into customer (cname,password,phno,balance) values (%s,%s,%s,%s)'
    a.execute(query,(name,password,phno,balance))
    mydb.commit()
    st.success('ACCOUNT CREATED')


st.header('WELCOME TO ABC BANK')
menu=['ADD THE CUSTOMER','WITHDRAW MONEY']
option=st.selectbox('option',menu)
if option=='ADD THE CUSTOMER':
    name=st.text_input('NAME')
    password=st.text_input('PASSWORD')
    phno=st.number_input('PHNO',min_value=0)
    balance=st.number_input('BALANCE',min_value=1000)
    button=st.button('CREATE')
    if button:
        add_customer(name,password,phno, balance)
# elif option=='WITHDRAW MONEY':
#     cid=st.number_input('CID',min_value=0,format='%d')
#     password=st.number_input('PASSWORD',min_value=0)
#     amount=st.number_input('AMOUNT',min_value=0,format='%d')
#     # button = st.button('AMOUNT WITHDRAW')
#     if st.button('withdraw'):
#         b=mydb.cursor()
#         query='select cid,password,balance from customer where cid=%s'
#         b.execute(query,(cid,))
#         c=b.fetchall()
#         if cid==c[0][0] and password==c[0][1]:
#             if amount <= c[0][2]:
#                 d=mydb.cursor()
#                 # query='update customer set balance ='
#                 d.execute(f'update customer set balance = balance-{amount} where cid={cid}')
#                 mydb.commit()
#                 st.success('WITHDRAW')
#             else:
#                 st.warning('INSUFFIENCT BALANCE')

elif option=='WITHDRAW MONEY':
    cid=st.number_input('CID',min_value=0,format='%d')
    password=st.text_input('password')
    amount=st.number_input('AMOUNT',min_value=0,format='%d')
    if st.button('withdraw'):
        a=mydb.cursor()
        query='select cid,password,balance from customer where cid=%s'
        a.execute(query,(cid,))
        b=a.fetchall()
        if password==b[0][1] and cid==b[0][0]:
            if amount <=b[0][2]:
                s=mydb.cursor()
                s.execute(f'update customer set balance =balance -{amount} where cid={cid}')
                mydb.commit()
                st.success('withdraw sucesfull...')
            else:
                st.error('INSUFFICIENT BALANCE')