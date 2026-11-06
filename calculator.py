
def add(a, b):
    
    with open("history.txt","a") as f:
        f.write(f"{a} + {b} = {a + b}\n")
    return a + b


def subtract(a, b):
    with open("history.txt","a") as f:
        f.write(f"{a} - {b} = {a - b}\n")
    return a - b


def multiply(a, b):
    with open("history.txt","a") as f:
        f.write(f"{a} * {b} = {a * b}\n")  
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    else:
        with open("history.txt","a") as f:
            f.write(f"{a} / {b} = {a / b}\n")
        return a / b
def power(a,b):
    with open("history.txt","a") as f:
        f.write(f"{a} ^ {b} = {a**b}\n")
    return a**b

def square_root(a):
    if a < 0:
        return "Square root of negative number is not defined."
    else:
        with open("history.txt","a") as f:
            f.write(f"Square root of {a} = {a**0.5}\n")
        return a**0.5

def process():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. View History")
    print("8. Clear History")
    print("9. Search History")
    print("10. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")
    return choice

if __name__=="__main__":

    print("Welcome to Smart Calculator!")

    while True:

        choice = process()

        if choice in ('1', '2', '3', '4', '5'):
            while True:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values.")

            

            if choice == '1':
                print("Result:", add(a, b))

            elif choice == '2':
                print("Result:", subtract(a, b))

            elif choice == '3':
                print("Result:", multiply(a, b))

            elif choice == '4':
                print("Result:", divide(a, b))

            elif choice == '5':
                print("Result:", power(a, b))


        elif choice == '6':

            while True:
                try:
                    a = float(input("Enter a number: "))
                    print("Result:", square_root(a))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            
            
        elif choice =="7":
            try:
                with open("history.txt","r") as f:
                
                    history = f.read()
                    if history:    
                        print("\nCalculation History:")
                        print(history)
                    else:
                        print("\nNo calculations performed yet.")
            except FileNotFoundError:
                print("\nNo calculations performed yet.")

        elif choice == '8':
            with open("history.txt","w") as f:
                pass
            print("\nCalculation history cleared.")


        elif choice == '9':
            print("What operation do you want to search for? (e.g., +, -, *, /, ^, sqrt): ")
            search_term=input("Enter the operation to search for:")
            flag=False
            if search_term=='sqrt':
                search_term='Square root'
            try:
                with open("history.txt","r") as f:
                    history = f.readlines()
                    for line in history:
                        if search_term in line:
                            print(line)
                            flag=True
                    if not flag:
                        print(f"\nNo calculations found for '{search_term}'.")
                    
            except FileNotFoundError:
                print("\nNo calculations performed yet.")
            
        elif choice == '10':
            print("Thank you for using Smart Calculator!")
            break

        else:
            print("Invalid choice")

        yn = input("\nDo you want to perform another calculation? (y/n): ")

        if yn.lower() != "y":
            print("Thank you for using Smart Calculator!")
            break
