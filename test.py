# Faulty Calculator @ Sourabh Kamat
import os
while True:
    os.system("cls")
    print("Enter a number to select.\n", # Showing Options
          "1. Addition",
          "2. Subtraction",
          "3. Multiplication",
          "4. Division", sep='\n')

    Option = 0
    while True:
        Option = int(input(">>>"))
        if Option < 1 or Option > 4:
            print(Option, "is a invalid selection, Try Again...\n",
                  "option range is between 1 to 4 only.")
        else:
            break
        

    number1   = int(input("Enter First  Number : ")) # Getting First  Number
    number2   = int(input("Enter Second Number : ")) # Getting Second Number

    if Option == 1:  # Addition
        faultnum1 = (56) # Specify those first numbers which you want to do calculation wrong with.
        faultnum2 = (9)  # And Second numbers.
        
        if (number1 == faultnum1 and number2 == faultnum2) or (number1 == faultnum2 and number2 == faultnum1):
            total = 77 # Pre Defined Faulty Answer
            print(number1, '+', number2, '=', total)
        else:
            total = number1 + number2
            print(number1, '+', number2, '=', total)

    elif Option == 2:  # Subtraction
        faultnum1 = (34)  # Specify those first numbers which you want to do calculation wrong with. 
        faultnum2 = (12)  # And Second numbers.
        
        if (number1 == faultnum1 and number2 == faultnum2) or (number1 == faultnum2 and number2 == faultnum1):
            total = 46   # Pre Defined Faulty Answer
            print(number1, '-', number2, '=', total)
        else:
            total = number1 - number2
            print(number1, '-', number2, '=', total)
            
    elif Option == 3:  # Multiplication
        faultnum1 = (45)  # Specify those first numbers which you want to do calculation wrong with. 
        faultnum2 = (3)   # And Second numbers.
        
        if (number1 == faultnum1 and number2 == faultnum2) or (number1 == faultnum2 and number2 == faultnum1):
            total = 555 # Pre Defined Faulty Answer
            print(number1, '×', number2, '=', total)
        else:
            total = number1 * number2
            print(number1, '×', number2, '=', total)
            
    elif Option == 4:  # Division
        faultnum1 = (56)  # Specify those first numbers which you want to do calculation wrong with. 
        faultnum2 = (6)   # And Second numbers.
        
        if (number1 == faultnum1 and number2 == faultnum2) or (number1 == faultnum2 and number2 == faultnum1):
            total = 4 # Pre Defined Faulty Answer
            print(number1, '÷', number2, '=', total)
        else:
            total = number1 / number2
            print(number1, '÷', number2, '=', total)

    else:
        print("Something's went wrong.")
        
    x = input("\nPress Enter To Do Again...")
