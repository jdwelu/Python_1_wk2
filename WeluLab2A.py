print("Welcome to a simple calculating program!")   #TITLE
print()

choice = str(input("Enter a  (1) to add,  (2) to subtract,  (3) to multiply, or  (4) to divide: "))   #SELECTIONS
print()   

if choice == "1":   #ADDITION CONDITION
    fvalue = float(input("Please enter the first value: "))
    svalue = float(input("Please enter the second value: "))
    one = fvalue + svalue
    print()
    print("Addition Result = ", one)
elif choice == "2":   #SUBTRACTION CONDITION
    fvalue = float(input("Please enter the first value: "))
    svalue = float(input("Please enter the second value: "))
    two = fvalue - svalue
    print()
    print("Subtraction Result = ", two)
elif choice == "3":  #MULTIPLICATION CONDITION
    fvalue = float(input("Please enter the first value: "))
    svalue = float(input("Please enter the second value: "))
    three = fvalue * svalue
    print()
    print("Multiplication Result = ", three)
elif choice == "4":   #DIVISION CONDITION
    fvalue = float(input("Please enter the first value: "))
    svalue = float(input("Please enter the second value: "))
    four = fvalue / svalue
    print()
    print("Division Result = ", four)
else:   #ERROR HANDLING
    print("Invalid Operation Entry, Exiting Program")

print()

#DID NOT DO FORMATTING SO THE USER CAN GET THE MOST EXACT ANSWER POSSIBLE
#OTHERWISE print("<Operation> Result = ", format(<variable>, ".2f"))
