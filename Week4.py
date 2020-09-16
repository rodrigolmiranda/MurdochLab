"""
def my_max(a,b,c,d,e):
    return(max(a,b,c,d,e))
def my_min(a,b,c,d,e):
    return(min(a,b,c,d,e))

def f_max_min_GPA(a,b,c,d,e):
    x = my_max(a, b, c, d, e)
    n = my_min(a, b, c, d, e)
    return[x,n]
print(f_max_min_GPA(1,3,5,4,2))

print(f_max_min_GPA(1,3,5,4,2)[0])
"""

up = "ABCDEFGHIJKLMNOPQRSTYWXZ"
dw = "abcdefghijklmnopqrstywxz"
text = "aBcDeFg"
retUP = ""
retDW = ""
for i in text:
    if (up.find(i) >= 0):
        retUP = retUP + i
    if (dw.find(i) >= 0):
        retDW = retDW + i

print(retUP)
print(retDW)
