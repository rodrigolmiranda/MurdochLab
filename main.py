
#print all the common letters in two strings
""""
s1 = "MU u rock"
s2 = "i rule MU"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter:"+char1)
                break
"""

"""
s="12345"
L = s[len(s)-1] + s[1:len(s)-1] + s[0]
#  +

print(L)
"""

"""
s="123456789"
L=len(s)
i=2
j=4
t=s[i]
s=s[0:i]#+s[j]+s[i+1:j]+t+s[j+1:L]
print(s)
"""

"""
s="aBcDe"#input("Enter a string:")
L=len(s)
for loop_index in range(int(L/2)):
    i=loop_index
    j=L-1-i
    t=s[i]
    s=s[0:i]+s[j]+s[i+1:j]+t+s[j+1:L]
print(s)
"""

"""
cube = 29
f=False
accuracy=3
for guess in range(abs(cube)+1):
    if abs(guess**3 - cube)<accuracy:
        f=True
        break
if(f):
    print(guess)
else:
    print("not found")
"""

"""
cube = 270
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)


n_unit = int(input("How many units? "))
for i in range(n_unit):
    n_st = int(input("how many students for this unit?"))
    total = 0.0
    for j in range(n_st):
        t=float(input("marks: "))
        total = total + t;
    print("average: ", total/n_st)





numbers = [[1, 2, 3], [2, 2, 2], [3, 1, 2]]

def (number):
	return number < 3

an_iterator = filter(less_than_three, numbers[1])


filtered_numbers = list(an_iterator)

print(filtered_numbers)

"""

for i in range(2, 5, 1):
    print(i)