"""
Project II:  An implementation of the so-called "Russian Peasant" or "Ancient
             Egyptian" method for multiplication.

File Name:   multiplier.py
Name:        ?
Course:      CPTR 141
Code Review: Adam Taylor
"""
# add an array to print table and sum of the numbers
# define varible
stop_pro = False
repeat_infi = 1
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']
while stop_pro == False:  # while loop to repeat program if user wishes
    error = True
    frist_digit_col = []
    second_digit_col = []
    add_num = []
    while error == True:
        # User input numbers for muiltplation
        frist_digit = input("\nEnter the frist digit: ")
        second_digit = input("Enter the second digit: ")
        # checks if frist charter of inputs are numbers
        if not(frist_digit[0] in number) or not(second_digit[0] in number):
            print(
                "\nPlease enter a number with no leters or speical charaters beside (-). ")
        else:
            error = False

    # converts inputs to int and resets varibles
    frist_digit = int(frist_digit)
    second_digit = int(second_digit)
    negative1 = False
    negative2 = False
    final_value = 0

    if frist_digit < 0:  # Checks if inputs are negative
        frist_digit *= -1
        negative1 = True
    if second_digit < 0:
        second_digit *= -1
        negative2 = True

    while second_digit >= 1:  # algroithem for muiltplcation
        if second_digit % 2 == 1:  # check to see if the second digit is odd then add to final valu if true
            final_value = (frist_digit + final_value)
            add_num.append(frist_digit)
        frist_digit_col.append(frist_digit)
        second_digit_col.append(second_digit)
        second_digit //= 2
        frist_digit *= 2

    if negative1 or negative2 == True:  # Reverts results to negtive if numbers were negative
        final_value *= -1
    if negative1 and negative2 == True:  # Revses prior action if both are postive
        final_value *= -1
    # print out result of algrothim
    print()
    for i in range(0, len(frist_digit_col)):
        print("{:<5}|| {}".format(frist_digit_col[i], second_digit_col[i]))
    print()

    if negative1 and negative2 == True:
        for j in range(0, len(add_num)):
            if j == len((add_num))-1:
                print("{} = ".format(add_num[j]), end="")
                break
            print("{} ".format(add_num[j]), end="+ ")

    elif negative1 or negative2 == True:
        for j in range(0, len(add_num)):
            if j == len((add_num))-1:
                print("{} = -".format(add_num[j]), end="")
                break
            print("{} ".format(add_num[j]), end="- ")

    else:
        for j in range(0, len(add_num)):
            if j == len((add_num))-1:
                print("{} = ".format(add_num[j]), end="")
                break
            print("{} ".format(add_num[j]), end="+ ")
    print(sum(add_num))
    print()
    print(final_value, "is the product of the two numbers.\n")

    while repeat_infi == 1:  # Promts use if they want to reapet calulations.
        response = input(("Do you wish to repeat the calucation [y/n]?"))
        if response[0].lower() == 'n':  # will break and stop if first letter is n or reapter if y
            stop_pro = True
            break
        elif response[0].lower() == 'y':
            print("Repeating...")
            break
        else:
            print()
            print("Try again. Please Enter a y or n. \n")
