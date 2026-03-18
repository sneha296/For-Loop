#what is a function?
#A function is a block of code that run only when it is called

#why are function?
#1.Avoid removing code
#2.make program,clean and organised 
#3.

# syntax :
# def function_name():
# ex :
""""
def greet():
    print("Hello students")
greet()

# function with parameters
# used to pass values
def greet(name = "student"):
     print(f"Hello {name}")
greet()
greet("Shreyarth")
greet("AICW")

# function with return value
# used when we want to send result back
def add(a , b):
    return a + b
result = add(2 , 3)
print(result)
"""
#1 : create a function to calculate and return result

    
#2 : create a function to check if number is even or odd
num=int(input("Enter a number:"))
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

print(check_even_odd(num))
#3 : create a function to find the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number:"))
result = factorial(num)
print(result)

#4.create a function of maximum among 3 numbers  
def find_max(a, b, c):
    return max(a, b, c) 

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a=float(input("Enter a number: "))
b=float(input("Enter a number: "))
c=float(input("Enter a number: "))
result=find_max(a,b,c)
print(f"The greater number is:{result}")   

#5.create a function to check if a string is palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()

    return s == s[::-1]

input_str = input("Enter a string: ")
result = is_palindrome(input_str)
if result:
    print(f"(input_str) is a palindrome.")
else:
    print(f"(input_str) is not a palindrome.")
    
#6.create a function to calculate area of circle  

def calculate_area(radius):
    return 3.14 * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"Area of the circle is:, {area}")