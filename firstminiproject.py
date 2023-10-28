
def add(a,b):
    ans = a + b
    print("Addition is: ",a + b)

def sub(a,b):
    ans = a - b
    print("Subtraction is: ",a - b)

def mul(a,b):
    ans = a * b
    print("Multiplication is: ",a * b)

def div(a,b):
    ans = a / b
    print("Division is: ",a / b)


while True:
    choice = int(input(" 1.Add\t 2.Sub \n 3.Mul\t 4.Div\n Enter your choice: "))
    if choice == 1:
        print("Addition is: ")
        fn = int(input("Enter a first number: "))
        sn = int(input("Enter a second number: "))
        add(fn,sn)


        
    elif choice == 2:
        print("Substraction is: ")
        fn = int(input("Enter a first number: "))
        sn = int(input("Enter a second number: "))
        sub(fn,sn)

        
        
    elif choice == 3:
        print("Muliplication is: ")
        fn = int(input("Enter a first number: "))
        sn = int(input("Enter a second number: "))
        mul(fn,sn)

        
        
    elif choice == 4:
        print("Division is: ")
        fn = int(input("Enter a first number: "))
        sn = int(input("Enter a second number: "))
        div(fn,sn)

        
        
    elif choice == 5:
        print("code for exit: ")
        break

    

    else:
        print("Hushar ahe ka re tu 1-4 madhe value taak!!!")


        
