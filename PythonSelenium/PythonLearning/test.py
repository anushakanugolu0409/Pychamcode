import keyword

"""key= keyword.kwlist # kwlist returns all the keywords in python
print(key)

x = "test  Anusha"
print(x.islower())
print(x[::-1]) # return from last
y = "name, age, city"
print(y[0:y.index(',')]) # index :return the position of the char specified

print(" " .join(y.split(','))) # split the string with specified char
print(y.partition(','))
print(y.rsplit(',',maxsplit=3)) # split the string with matching sub and no of matching

print('www.example.com'.strip('comwwwqweyrt.')) # removes the char from the string
print("welcome to {cl} learning {through} ".format(cl="Python",through=y)) # we can use keywords in the {} and value can be assign with var or assign the string
print("welcome {} y value{}".format(x,y))"""

"""dic={1:23,2:32}
print(dic[1]) # key and values can be of any type as int , string , boolean, float
dic[3]=42 # add value to dic
print(dic)

list1=[1,2,3,4,5,6]
list2=[6,7,8,9,10]
s=list(zip(list1,list2)) # maps the items from list1 to items in list2
print(s)

for x,y in zip(list1,list2):
    print(x,y)"""

tup=(1,2,3,4,5)
print(next(iter(tup))) # iter will return the iterable obj and next print the elements in iter
lis=[1,2,3,4]
print(next(iter(lis)))

for x in lis:
    print(x)

import datetime
today= datetime.datetime.now()
print(today)
print(datetime.datetime.today())
print(datetime.datetime.today().date())
print(datetime.datetime.today().timestamp())
