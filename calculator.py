# Simple Calculator

# 1. Functions for Operations

# 2. User Input

# 3. Print Result

# Function to add two numbers
def add(x,y):
    return x+y
# Function to substract two numbers
def sub(x,y):
    return x-y
# Function to multiply two numbers
def mul(x,y):
    return x*y
# Function to divide number
def div(x,y):
    return x/y
# Function for average of  two numbers
def avg(x,y):
    return (x+y)/2
# User Input
print("Operation To Perform :\n"\
      "1. Addition\n"\
      "2. Substraction\n"\
      "3. Multiplication\n"\
      "4. Division\n"\
      "5. avrerage\n")
select=int(input("Select the operstions 1 To 5 :"))

x=int(input("Enter the First nuber :"))
y=int(input("Enter the second number :"))
 
# Result
if select==1:
    print( x, "+", y, "=",add(x,y))
elif select==2:
    print( x, "-", y, "=",sub(x,y))
elif select==3:
    print(x ,"*", y,"=",mul(x,y))
elif select==4:
    print(x,"/", y," =",div(x,y))
elif select==5:
    print("(",x,"+",y,")","/","2","=",avg(x,y))
else:
    print("Invalid Number")