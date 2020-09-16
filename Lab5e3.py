x = int(input("Type a value for x: "))#43
y = int(input("Type a value for y: "))#23
N = int(input("Type a value for N: "))#764
r = int((2147483647**0.5)-1)
print(r)

permit = True
if abs(x) > r:
    permit = False
    print("x is outside of the range permitted: +-46339")
if abs(y) > r:
    permit = False
    print("y is outside of the range permitted: +-46339")
if abs(N) > r:
    permit = False
    print("N is outside of the range permitted: +-46339")


if permit == True:
    result = 1
    for i in range(y):
        result = (result*x)%N
    print("First way:", result)

    result=1
    for i in range(y):
        result = (result%N)*(x%N)
    print("Second way:", result%N)
