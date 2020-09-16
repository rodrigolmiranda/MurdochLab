#%% Question 1 - Recursion on Strings. Write a recursive function to reverse the input / strings. E.g., if the input is ‘world’, the required output is ‘dlrow’.
ret = ""
def revString(t):
    if len(t)==1:
        return t
    else:
        return ret+t[-1]+revString(t[0:-1])

revString("Rodrigo")

#%% Question 2 - Write a recursive function to compute the sum of the first n integers.
def sumtorial(n):
    if n == 1:
        return 1
    else:
        return n+sumtorial(n-1)

sumtorial(25)

#%% Question 3 - 
"""
The implementation of Fibonacci is provided in one of the slide of lecture
notes. Your task in this question is to improve it and implement a recursive
function with memorisation. You can define a dictionary as a global variable that
will serve as map ping from values of n to their fib(n) result. The memorised fib
function will record any value returned by the function in its dictionary
"""
f = {}
C=0
def fib(x, xori):
    global C
    C=C+1
    if x == 0 or x == 1:
        f[x] = x
    else:
        f[x] = f[x-1] + f[x-2]
    if x == xori:
        return f[xori]
    else:
        return fib(x+1, xori)

print("Fibonacci: ", fib(0, 100))
print("Quantity of iterations: ", C)
print("Dictionary of Fibonacci: ", f)


#%%
C=0
def fib(x):
    global C
    C=C+1
    if x==0:
        return 0
    if x ==1:
        return 1
    else:
        # if 
        return fib(x-1) + fib(x-2)

print(fib(10))
print(C)

# %%

dic = {'HD': '80-100', 'D': '70-79'}

dic.keys()
dic.values()
dic['D']

#%%

table = {'Ana': (1001, 3.9), 'Michael': (1002, 3.54), 'Dina': (1003, 2.5)}
table.keys()
#table.values()
table['Dina'] = [1003, 2.5, 'Female']
del(table['Dina'])
table

#%%
def fac(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

sumtorial(3)
#%%
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(3, 'A', 'C', 'B')


#%%
d={}
id = int(1)
while id > 0:
    id = int(input("Enter ID (negative to exist):"))
    if id <0 : 
        break
    if id in d:
        print("Existing!!")
    else:
        cgpa = float(input("type the GPA:"))
        d[id] = cgpa
    print(d)

