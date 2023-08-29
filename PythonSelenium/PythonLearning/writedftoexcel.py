import pandas as pd
from faker import Faker
from faker.providers import DynamicProvider
"""df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
df1.to_excel("output.xlsx")"""
"""testd=[["Anusha",33],["aksh",4],["ragh",38],["amani",34],['mani',45]]
testdn=[["AnushaN",33],["akshN",4],["raghN",38],["amaniN",34],['maniN',45]]
df=pd.DataFrame(testd, columns=['Name','Age'])
df2=pd.DataFrame(testdn)
print(df)

readexcel = pd.read_excel("namenage.xlsx")
rowcount=readexcel.shape[0] """ # reads no of rows

# write to single sheet
#df.to_excel('namenage.xlsx',index=False,sheet_name='appendtoexcel')

# append to existing sheet
"""with pd.ExcelWriter("namenage.xlsx", mode='a',if_sheet_exists='overlay',engine="openpyxl") as writer:
    df.to_excel(writer,sheet_name='newsheet')
    df2.to_excel(writer,sheet_name='newsheet',startrow=rowcount,header=None)"""
    # header=none will append the data to existing data without the column name

# write to multiple sheet
"""with pd.ExcelWriter("namenage.xlsx") as write:
    df.to_excel(write, sheet_name='newsheet')
    df.to_excel(write,sheet_name='addnewaheet')"""

#generate the fake data
fake= Faker()
names=[]
for i in range(1,5):
    names.append(fake.name())

email1=[]
for i in range(1,5):
    email1.append(fake.email())

medical_professions_provider = DynamicProvider(
     provider_name="medical_profession",
     elements=["dr.", "doctor", "nurse", "surgeon", "clerk"])
fake.add_provider(medical_professions_provider)
medical_profession=[]
for i in range (1,5):
    medical_profession.append(fake.medical_profession())

df = pd.DataFrame(zip(names,email1,medical_profession),columns=['Name','Email','medical_profession'])
print(df)
