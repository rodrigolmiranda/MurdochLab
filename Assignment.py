# %%
import datetime
from tkinter import *
import numpy as np
import random

# %% Function which creates a list of prime numbers


def dic_primes(qtdnumbers):
    # using set to create a list hashed because is faster
    # and I can use difference_update to clear non-prime-numbers
    list_numbers = set(range(2, qtdnumbers, 1))
    ret_primes = {}
    while list_numbers:
        prime = list_numbers.pop()
        ret_primes[prime] = len(str(prime))
        list_numbers.difference_update(  # function that clear from list_numbers de non-prime-numbers
            set(range(prime*2, qtdnumbers+1, prime)))

    return ret_primes
# %% Function which returns if two numbers is coprime (greatest common divisor)


def gcd(a: int, b: int):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

# Function which returns a random of big coprime numbers


def coprimes(list_primes: list):
    while True:
        p = random.choice(prime_list)
        list_primes2 = list(filter(lambda x: x >= int(p*0.9), list_primes))
        q = random.choice(list_primes2)
        if gcd(p, q) == 1:
            return(p, q)
            break

# %% ModularInverse


def ModularInverse(a: int, m: int, n: int):
    a = a % m
    for i in range(n, int(n*1.2)):
        if ((a * i) % m == 1):
            return i
    raise Exception("Modular inverse doesn't exist")

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# modinv(7, 20)


# %%
# generate exponente(e)


def Exponente(yn, min_e, max_e):
    for i in range(max_e):
        e = random.randint(min_e, max_e)
        if gcd(yn, e) == 1:
            return e


# %%
def cript(message: int, public_key: int, mod: int):
    result = 1
    for i in range(public_key):
        result = (result % mod)*(message % mod)
    print("result", message, public_key, mod, result)
    return result % N


def decript(message: int, private_key: int, mod: int):
    result = 1
    for i in range(private_key):
        result = (result % mod)*(message % mod)
    print("result", message, private_key, mod, result)
    return result % N
# %%


# creates a list of prime numbers using the function above
dicprime = dic_primes(100000)
# print(dicprime)
dig = list(dicprime.values())[-1]

prime_list = list({k: v for k, v in dicprime.items() if v >= dig}.keys())
prime_listshort = list({k: v for k, v in dicprime.items() if v <= 3}.keys())

# generate two coprime numbers using the fuction above
# print(prime_list)
listcoprime = coprimes(prime_list)
print("listcoprime", listcoprime)
p = listcoprime[0]
print("p", p)
q = listcoprime[1]
print("q", q)
n = p*q
print("n", n)
yn = (p-1)*(q-1)
print("yn", yn)
# e = Exponente(yn,prime_list[-1]/2,prime_list[-1]) #random.randint(int(prime_list[-1]/2),prime_list[-1]) #3
# e = Exponente(yn, int(prime_listshort[-1]/2), prime_listshort[-1])
e = 3
print("e", e)
# d = ModularInverse(e, yn, n)
d = modinv(e, yn)
print("d", d)
print(p, q, n, yn, e, d)

message = 31
public_key = e
private_key = d
mod = n
message_cript = cript(message, public_key, mod)
# message_cript = (message**public_key) % mod
print("Message", message)
print("Encrypted message", message_cript)
message_decrypt = cript(message_cript, private_key, mod)
print("Decrypted message", message_decrypt)

# message_decrypt = (message_cript**private_key) % mod
message_decrypt = (message_cript%mod%mod%mod%mod%mod%mod%mod%mod)**(private_key%mod%mod%mod%mod%mod%mod%mod%mod)
"""
# GUI

scrn = Tk()
scrn.geometry("500x500")


def run():
    n = int(in1_storage.get())+int(in2_storage.get())
    print(n)


scrn.title("RSA Encrypt/Decrypt")
ok_btn = Button(text="Add", command=run)
ok_btn.place(x=100, y=100)
in1_storage = StringVar()
in1 = Entry(textvariable=in1_storage)
in1.pack()
in2_storage = StringVar()
in2 = Entry(textvariable=in2_storage)
in2.pack()
print("End")
scrn.mainloop()
"""

# %%
prime_list = list_primes(100000)

# %%
# ModularInverse(12715560, 3)
# Iterative Algorithm (xgcd)




# %%
# prime_listshort = list({k: v for k, v in dicprime.items() if v <= 3}.keys())
# prime_listshort[-1]
# message_cript = 759
# private_key = 917307267
# mod = 1375960900
# (((a%c)%c)**((b%c)%c))
# (message_cript%mod%mod%mod%mod%mod%mod%mod%mod)#**

# (private_key%mod%mod%mod%mod%mod%mod%mod%mod%mod%mod%mod%mod%mod%mod%mod)
