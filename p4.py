x1y1 = input("")
x2y2= input("")
x1 = float(x1y1.split(" ")[0])
y1 = float(x1y1.split(" ")[1])
x2 = float(x2y2.split(" ")[0])
y2 = float(x2y2.split(" ")[1])

"""
x1 = float(input(""))
y1 = float(input(""))
x2 = float(input(""))
y2 = float(input(""))

x1 = 1.0
y1 = 7.0
x2 = 5.0
y2 = 9.0

x1 = -2.5
y1 = 0.4
x2 = 12.1
y2 = 7.3

"""
result = round((((x2-x1) **2) + ((y2-y1) **2)) ** 0.5, 4)
print(result)
