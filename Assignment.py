# %%
from tkinter import *
import numpy
import random

# %% Function which creates a list of prime numbers


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i & 1)+4)//3::2*k] = False
    return numpy.r_[2, 3, ((3*numpy.nonzero(sieve)[0][1:]+1) | 1)]


# %% creates a list of prime numbers using the function above
prime_list = primesfrom2to(1000000)

# %% Function which returns if two numbers is coprime


def gcd(a, b):
    if (b == 0):
        return a
    else:
        # print(a, b, a % b)
        return gcd(b, a % b)

# %% Function which returns a random of big coprime numbers


def coprimes(list_primes):
    prime_listcut = [x for x in list_primes if x >= int(list_primes[-1]//10)]
    # random.choice(prime_list2)

    while True:
        p = random.choice(prime_listcut)
        q = random.choice(prime_listcut)
        if gcd(p, q) == 1:
            return(p, q)
            break


# %% generate two coprime numbers using the fuction above

pq = coprimes(prime_list)
p = pq[0]
q = pq[1]
n = p*q

# %%
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

# %%
text = 'RODRIGO MIRANDA'
i = int.from_bytes(text.encode('utf-8'), byteorder='big')
i = 31
e = 3
d = 7
print("i", i)
c = (i**e) % 33
print("c", c)
d = (c**d) % 33
print("d", d)
# %%
# gcd(3, 7)

# d = (3**-1)%33
# d
# gcd(12, 20)
x = 1
y = 7
N = 20
for i in range(y):
    result = (result % N)*(x % N)
print("Second way:", result % N)

# %%


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


modinv(7, 20)

# %%
