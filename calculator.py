"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculate_numbers():

    while True:

        input_string=input("<")
        token = input_string.split(' ')

        if token[0] == "q":
            result = None
            break

        else: 
            num1=int(token[1])
            num2=int(token[2])
            
            
            if token[0] == "add" or "+":
                result= add(lst)
            elif token[0] == "-":
                result= subract(num1,num2)
            elif token[0] == "*":
                result= multiply(num1,num2)
            elif token[0] == "/":
                result= divide(num1,num2)
            elif token[0] == "square":
                result= square(num1)
            elif token[0] == "cube":
                result= subract(num1)
            elif token[0] == "pow" :
                result= subract(num1,num2)
            elif token[0] == "mod" :
                result= subract(num1,num2)
            print(result)
    
    return result
  

calculate_numbers()

# Your code goes here
