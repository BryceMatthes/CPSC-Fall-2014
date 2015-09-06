# Name: Bryce Matthes	
# Student ID: 10147880
# Mini 4

def multiply(num1,num2):
	return(num1*num2)

def start():
    print("This program will multiply two numbers")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))    

    product = multiply(num1,num2)

    print("%f * %f = %f" %(num1,num2,product))

start()