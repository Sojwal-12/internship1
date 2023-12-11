#calci

def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
def modules(num1,num2):
    return num1 % num2


def arithmetic():
 
 print("*****Oprations*****")
 print("1. Add")
 print("2. Subtract")
 print("3. Multiply")
 print("4. Divide") 
 print("5. Modules")  

 select = int(input("Select Arithmetic Operation From 1, 2, 3, 4, 5:"))
 
 num1 = float(input("Enter First Number ="))
 num2 = float(input("Enter Second Number ="))
 
 if (select == 1):
    print(num1, "+", num2, "=", add(num1, num2))
    
 elif (select == 2):
    print(num1, "-", num2, "=", subtract(num1, num2))

 elif (select == 3):
    print(num1, "*", num2, "=", multiply(num1,num2))

 elif (select == 4):
    print(num1, "/", num2, "=", divide(num1,num2))

 elif (select == 5):
    print(num1, "%", num2, modules(num1,num2))

 else:
    print("Invalid Operation")

 next_op=input("You want to perform next operation ? (yes/no): ")
 if next_op == "no":
    print("See you Later !!")
    exit()
 elif next_op == "yes":
    arithmetic()
 else:
    print("Invalid Choice")

arithmetic()