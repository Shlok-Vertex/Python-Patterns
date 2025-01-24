def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if(b==0):
        return "Error...! Try Again..."
    else:
        return a/b

def calculator():
    print("Please select Operator :")
    print("1. Add :")
    print("2. Subtract:")
    print("3. Multiply :")
    print("4. Division :")

    choice = input("Enter Operator (1/2/3/4) :")

    if choice not in ('1','2','3','4'):
        print("Invalid input...!, Please enter a valid choice...")
        return
    
    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {diff(num1,num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {mult(num1,num2)}")
    elif choice == '4':
       print(f"{num1} / {num2} = {div(num1,num2)}")
    else:
        print("Error...!")

if __name__ == "__main__":
    calculator()   