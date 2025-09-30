def calculator():
    print("Welcome to the Calculator App")
          
    while True:
    
        print("\n select an operation from below(1/2/3/4/5)")
        print('1.Addition (+)')
        print('2.Subtraction (-)')
        print('3.multiplication (*)')
        print('4.division (/)')
        print('5.power (^)')
        print('6.Exit')

        choice = input("Enter Your Choice from (1/2/3/4/5/6):")

        if choice == "6":
            print("Thank u for using the calculator app")
            break
            
        if choice in ['1','2','3','4','5']:
            try:
                num1 = float(input('Enter the First Number: '))
                num2 = float(input('Enter the Second Number: '))


                if choice == '1':
                    result = num1 + num2
                    print(f"The result of addition is: {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"The result of subraction is: {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"the result of multiplication is: {result} ")
                elif choice == '4':
                    if num2 !=0:
                        result = num1/num2
                        print(f"The result of division is: {result}")
                    else:
                        print('Error: cannot divide by Zero')
                elif choice == '5':
                    result = num1 ** num2 
                    print(f"the result of power is: {result}")

            except ValueError:
                print("Error: please enter a valid numeric values")
        
        else:
            print('Invalid choice! please select a valid operation')

calculator()    