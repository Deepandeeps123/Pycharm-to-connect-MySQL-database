'''




import streamlit as st
import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='python',
    database='project'
)


def add_customer(name,phno,password,balance):
    a=mydb.cursor()
    query='insert into customer (cname,phno,password,balance) values(%s,%s,%s,%s)'
    a.execute(query,(name,password,phno,balance))
    mydb.commit()
    st.success('CREATED.......')


st.header('WELCOME TO ABC BANK')
menu=['ADD THE CUSTOMER','WITHDRAW MONEY']
option=st.selectbox('option',menu)

if option =='ADD THE CUSTOMER':
    name=st.text_input('NAME')
    password=st.number_input('PASSWORD',min_value=0)
    phno=st.number_input('PHNO',min_value=0)
    balance=st.number_input('BALANCE',min_value=1000)
    button=st.button('CREATE')
    if button:
        add_customer(name,phno,password,balance)

elif option =='WITHDRAW MONEY':
    cid=st.number_input('CID',min_value=0,format='%d')
    password=st.text_input('PASSWORD')
    amount=st.number_input('AMOUNT',min_value=0,format='%d')
    if st.button('withdraw'):
        a=mydb.cursor()
        query='select cid,password,balance from customer where cid=%s'
        a.execute(query,(cid,))
        b=a.fetchall()
        if password==b[0][1] and cid == b[0][0]:
            if amount <=b[0][2]:
                s=mydb.cursor()
                s.execute(f'update customer set balance = balance -{amount} where cid = {cid}')
                mydb.commit()
                st.success('Withdraw')
            else:
                st.error('Insuffienct balance')
'''
import streamlit as st
import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='python',
    database='project'
)


def add_customer(name,phno,password,balance):
    a=mydb.cursor()
    query='insert into customer (cname,phno,password,balance) values (%s,%s,%s,%s)'
    a.execute(query,(name,phno,password,balance))
    mydb.commit()
    st.success('CREATED.......')

st.header('WELCOME TO ABC BANK')
menu=['ADD THE CUSTOMER','WITHDRAW MONEY','DEPOSIT','BALANCE']
option=st.selectbox('option',menu)
if option=='ADD THE CUSTOMER':
    name=st.text_input('NAME')
    password=st.text_input('PASSWORD')
    phno=st.number_input('PHNO',min_value=0)
    balance=st.number_input('BALANCE',min_value=1000)
    button=st.button('CREATE')
    if button:
        add_customer(name, phno, password, balance)
elif option =='WITHDRAW MONEY':
    cid=st.number_input('CID',min_value=0,format='%d')
    password=st.text_input('PASSWORD')
    amount=st.number_input('AMOUNT',min_value=0,format='%d')
    if st.button('withdraw'):
        a=mydb.cursor()
        query='select cid,password,balance from customer where cid=%s'
        a.execute(query,(cid,))
        b=a.fetchall()
        if cid==b[0][0] and password==b[0][1]:
            if amount <= b[0][2]:
                s=mydb.cursor()
                s.execute(f'update customer set balance = balance - {amount} where cid = {cid}')
                mydb.commit()
                st.success('WITHDRAW......')
            else:
                st.warning('INSUFICENT BALANCE')
elif option=='DEPOSIT':
    cid=st.number_input('CID',min_value=0,format='%d')
    password=st.text_input('PASSWORD')
    amount=st.number_input('AMOUNT',min_value=0,format='%d')
    if st.button('DEPOSIT'):
        a=mydb.cursor()
        query='select cid,password,balance from customer where cid =%s'
        a.execute(query,(cid,))
        b=a.fetchall()
        if cid==b[0][0] and password==b[0][1]:
            s=mydb.cursor()
            s.execute(f'update customer set balance = balance + {amount} where cid ={cid}')
            mydb.commit()
            st.success('DEPOSIT')
        else:
            st.warning('Invalid')
elif option=='BALANCE':
    cid=st.number_input('CID',min_value=0)
    password=st.text_input('PASSWORD')
#     if st.button('Sumbit'):
#         a=mydb.cursor()
#         a.execute('select cid,password,balance from customer where cid=%s' ,(cid,))
#
#         b=a.fetchall()
#         if cid==b[0][1] and password==b[0][1]:
#             st.write(f'Your Balance is :{b[0][2]}')
#         else:
#             st.write('Invalid')



if st.button('SUBMIT'):
    a = mydb.cursor()
    a.execute('select cid,password, balance from customer where cid=%s', (cid,))
    b = a.fetchall()
    if password == b[0][1] and cid == b[0][0]:
        st.write(f'your balnce is :- {b[0][2]}')
    else:
        st.error('invalid credentials...')