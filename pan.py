import pandas as pd
name=['dinga','dingoi','manga','mangi','sanga']
sql=[1,2,3,4,6]
python=[4,5,3,2,1]
django=[2,4,3,1,5]
web_tech=[5,3,2,4,2]
df=pd.DataFrame({'name':name,'sql':sql,'python':python,'django':django,'web_tech':web_tech})


print(df)

# print(df.head(5))
# tail