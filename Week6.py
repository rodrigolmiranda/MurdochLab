"""
from tkinter import *
scrn=Tk()
scrn.geometry("500x500")
def run():
    n=int(in1_storage.get())+int(in2_storage.get())
    print(n)
scrn.title("Calculator")
ok_btn=Button(text="Add", command=run)
ok_btn.place(x=100,y=100)
in1_storage=StringVar()
in1=Entry(textvariable=in1_storage)
in1.pack()
in2_storage=StringVar()
in2=Entry(textvariable=in2_storage)
in2.pack()
print("End")
scrn.mainloop()
"""
"""
def isPrime(n):
    flag=True
    for i in range(2,n-1):
        if n%i==0:
            flag=False
            break
    return flag
n=int(input("Enter a number: "))
print(isPrime(n))
"""

"""
#import random
from random import randint, seed
seed(234)
for i in range(10):
    print(randint(0,5))

#print(random.random())
"""

#%%

def gcd(a, b):
    if (b == 0):
        return a
    else:
        print(a, b, a % b)
        return gcd(b, a % b)
a = 33
b = 3
#print("The gcd of 60 and 48 is : ", end="")
print(gcd(a, b))
#print(gcd(5, 9))


# %%
