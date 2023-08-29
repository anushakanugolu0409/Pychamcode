import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import csv

list1= ['asder%"',"@#$.,/;'!%^&*()-?:{}[]+|\gfhgh",'asd@',"__test"]
str= " ".join(list1)
# print(str)
list2=["test","test1","test2",'test3']
list3=["123, West Way","1234, Test","546, te","99, tes"]
list4=['12345','35435','4543','43543']


"""p=pd.Series(df)
print(p)
for x in p:
    print(x.replace("%","")) # string will be retured
    print(x.split("@#$")) # return the list
    print(x.strip("__")) # return the string """
p=pd.DataFrame(zip(list1,list2,list3,list4),columns=('Name','FN',"Address","population"))
# print(p)

"""
p['Name']=p['Name'].map(lambda x: re.sub(r'\W+', '', x)) # replace one or more matching string and replace with specified char in the iteration
print(p)

# p['Address','pincode']=p['Address'].apply(lambda x : x.split(","))
# print(p)


p[['Address','pincode']]=p['Address'].str.split(",", expand=True)
print(p) # split single column to multiple column

p['FullName']= p[['Name','FN']].apply(lambda x : ",".join(x),axis=1) # combine 2 columns to 1 column
print(p)
print(p.drop(columns=['Name','FN'])) # drop the columns

# Move the columns to first position
temp_cols=p.columns.tolist()
index=p.columns.get_loc("FullName")
new_cols=temp_cols[index:index+1] + temp_cols[0:index] + temp_cols[index+1:]
p=p[new_cols]
print(p)

# move to last position
temp_cols=p.columns.tolist()
print(temp_cols)
print(temp_cols[1:], temp_cols[0:1])
new_cols=temp_cols[1:] + temp_cols[0:1]
print(new_cols)
p=p[new_cols]
print(p)"""


# sal=pd.read_csv("C:\\madhan\\appsql\\Salaries.csv") # read the csv file

lis=['sfdjkj www.hdfc.com fdsfd https://pytest.com','sfdh https://docs.pyton.com']

df=pd.DataFrame(lis)
print(df)
"""def extract_url(text):
    pattern= re.compile(r'https://\S+|www\.\S+|\b[^ ]+\.com\b')
    print("pattern" ,pattern)
    url=pattern.findall(text)
    print("url:",url)
    return " ".join(url) # return in the form of list to convert to str
print(df[0].apply(extract_url))"""
print(df[0].apply(lambda x :" ".join(re.compile(r'https://\S+|www\.\S+|\b[^ ]+\.com\b').findall(x))))
print(df[0].apply(lambda x : re.compile(r'https://\S+|www\.\S+|\b[^ ]+\.com\b').search(x)))

#complie search for prticular pattern and findall extract data in the string
# serach used to search for the pattern in string

