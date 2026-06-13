def display_menu():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset")
    print("6. Exit")

def get_numerical_input():
    try:
        num = float(input("Enter the number: "))
        return num
    except ValueError as e:
        print(f"Error: Invalid input. Please enter a valid numerical value. Details: {e}")
        return None

def execute_operation(choice, current, new_num):
    try:
        if choice == '1':
            return current + new_num
        elif choice == '2':
            return current - new_num
        elif choice == '3':
            return current * new_num
        elif choice == '4':
            if new_num == 0:
                print("Error: Division by zero is not allowed.")
                return current  # Returns the original value unchanged if division by zero occurs
            else:
                return current / new_num
        return current
    except ValueError as e:
        print(f"Error: Invalid input. Please enter a valid numerical value. Details {e}")         

def calculator():
    current_value = 0.0
    print("Welcome")
    
    while True:
        print("\nCurrent result: {}".format(current_value))
        display_menu()
        choice = input("Enter choice (1-6): ")
        if choice == '6':
            print("Bye")
            break
            
        if choice == '5':
            current_value = 0.0
            print("Result reset to 0.")
            continue
            
        if choice not in ['1', '2', '3', '4']:
            print("Error: Invalid option. Please select a number between 1 and 6.")
            continue

        num = get_numerical_input()  
        if num is None:
            continue 
     #  Execute the calculation and update the current value
        current_value = execute_operation(choice, current_value, num)
            
if __name__ == "__main__":
    calculator()