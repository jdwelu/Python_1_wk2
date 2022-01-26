print("***********************************************")
print("WELCOME TO THE METRO COLLEGE PAYROLL CALCULATOR")
print("***********************************************")
print("-------------author: JD WELU-------------------")
print()
print("You will use this program to accumulate the pay of all college")
print("employees. To continue or quit the program simply enter (yes/no)")
print("The final payroll balance will be displayed before you.")
print("'CTRL + c' will exit the program in the middle.") 
# Introduction for the program.

pay = 0 # Establishes program start pay.
condition = "yes" # Declares condition for the 'while' loop.

while condition == "yes":
    
    print()
    rpay = float(input("Enter an employee's pay rate (at least $9.25): "))
    hours = float(input("Please enter the amount of hours worked (zero or a positive number): "))
    print()
    # The two variable inputs needed for the program to run.
    
    if rpay < 9.25 or hours < 0 or hours > 80: # Error handling to get proper values.
        print()
        print("*************************************************************************")
        print("An invalid value was received for pay or hours. Please re-enter the data.")
        print("*************************************************************************")
        print()
        continue # Sends the user back to beginning of the loop if incorrect data is entered.
    if hours <= 40: # Regular pay statement.
        tpay = hours * rpay
        print("The total pay: $", format(tpay, ".2f"), sep="")
        pay = pay + tpay
        print()
        print("The total payroll is now: $", format(pay, ".2f"), sep="")
        print()
        print()
        condition = input("Enter 'yes' if you wish to continue: ")
        print()
    if hours > 40: # Regular pay with overtime statement.
        tpay = ((40 * rpay) + (((hours - 40) * rpay) * 1.5)) # Overtime math.
        print("The total pay: $", format(tpay, ".2f"), sep="")
        pay = pay + tpay
        print()
        print("The total payroll is now: $", format(pay, ".2f"), sep="")
        print()
        print()
        condition = input("Enter 'yes' if you wish to continue: ")
        print()

else:
    print()
    print("******************************")
    print("The total payroll is: $", format(pay, ".2f"), sep="")
    print("******************************")
    # Final payroll ending declaration.


##Notes:
##    1.) Before the program starts I check for incorrect values. I limited the
##    max hours to 80 hours and established minimum wage.
##    2.) I had plans to use an if, elif, else model, but plain if statements
##    served the needed functions.
##    3.) I tried to use asterix to make the program a bit easier to see.
