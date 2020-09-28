# %%Q1. Write a program that accepts two integer inputs from the user and checks if
# one integer evenly divides another. In your solution, you are required to implement exception handling to check user inputs for validity and also to avoid
# ZeroDivisionError in the output

try:
    n = int(input("Type the numerator:"))
    d = int(input("Type the denominator:"))
    if d == 0:
        raise Exception('Division by zero',
                        'Type another value for divisor different of zero!')
    print("The division of the two values is: ", n / d)
except Exception:
    print("Divide by zero")
finally:
    print("End of program")

# %%
# Q2. You are in country where there are two conditions for fishing:
# (a) you can fish if you are 17 years old or less and your parent has a license.
# (b) If you are 18 years old or more you need to have your own license.
# Write a program that tells someone if they are legal to fish. First ask them how old they are, whether they have a license or not, and whether their parent has a license or not. Add exception handling to the program so that if the user answers something other than their age that the program prints “You did not enter your age correctly”.
try:
    a = input("Type your age:")
    if not a.isnumeric():
        raise Exception("Your age is not numerical")
    if int(a) < 18:
        license = input("Does your parent has a fishing license?[S/N]:")
        if license.upper() not in ['S', 'N']:
            raise Exception("The value typed is diferent of expected [S/N].")
        if license.upper() == 'S':
            print("you can fishing")
        else:
            print("you can not fishing")
    else:
        license = input("Do you have a fishing license?[S/N]:")
        if license.upper() not in ['S', 'N']:
            raise Exception("The value typed is diferent of expected [S/N].")
        if license.upper() == 'S':
            print("you can fishing")
        else:
            print("you can not fishing")

except Exception as e:
    print(str(e))
finally:
    print("End of program")

# %%
# Q3. Consider the following program (an example of continuous menu) D=['Sara', 3.40, '04235','IT'] def runMenu(): choice=1
# while not choice==0:
# print("Please enter your choices:") print("1- to print your Name")
# print("2- to print your GPA")
# print("3- to print your Contact")
# print("4- to print your major")
# print("0- to Exit")
# choice=int(input())
# print(D[choice-1])
# runMenu()
# Questions: a. List all the errors might happen due to some unexpected inputs b. Fix them using exception handling concept
D = ['Sara', 3.40, '04235', 'IT']


def runMenu():
    try:
        choice = 1
        while not choice == 0:
            print("Please enter your choices:")
            print("1- to print your Name")
            print("2- to print your GPA")
            print("3- to print your Contact")
            print("4- to print your major")
            print("0- to Exit")
            choice = int(input())

            if choice == 0:
                break
            elif(choice in [1, 2, 3, 4]):
                print(D[choice-1])
            else:
                print("Alert: Value typed is not on menu, type again.")

    except ValueError as e:
        print("Error: Value typed is not numerical!")
    except Exception as e:
        print(str(e))
    finally:
        print("End of Program")


runMenu()
