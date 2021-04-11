# I am writing my training code
'''
bulk comments can be put within tripple quotes
'''
print('Hello Kabeer')
print('Welcome to a wonderful, healthy and happy life')
A=10
B="Jugnu"
print(A,B)
"""
Tuples come within ()
Lists come within []
Dictionaries {'Age':41, 'Name':Jugnu}
Set {A,1,2,B}
"""
X=10
Y=15
if(X<Y):
    print('X is less than Y')
elif('X>Y'):
    print('X is greater than Y')
else:
    print('X is equal to Y')

count=0
while (count<5):
    print('Jugnu')
    count=count+1
    break
print('Done')


print('do some research')
print('this is a check3')

count=1
N=int(input("number:"))
faccheck=1
for count in range (1,N+1):
    faccheck= faccheck*count
print (faccheck)

# Reading, Writing and Working on Files

import os
newfile=open("jugnutesting.txt", "w+")

for i in range (1,10):
    newfile.write("\n welcome to peace")

for i in range (1,10):
    print(newfile.read())

newfile.seek(0)
print(newfile.tell())

# Let's draw a few charts

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show()

import pandas as pd
df = pd.read_excel ('C:\My_Data\python_learn\Check2.xlsx', sheet_name='Sheet1')
print (df)

df2 = pd.read_excel ('C:\My_Data\python_learn\Agent_Perf.xlsx', sheet_name='Sheet1')
df3 = pd.read_excel ('C:\My_Data\python_learn\Agent_Perf.xlsx', sheet_name='Sheet2')

print (df2)
df2.head()
print(df2.shape)
print(df2.describe)

print(df3)

gk= df2.groupby(['Name', 'Date'])
gk.count()

gk2=pd.merge(df2,df3, on='Name')
print(gk2)
gk2.sort_values(by=['Calls'])

























