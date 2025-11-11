current_choice = "-"
computer_parts = [] #create an empty list


while current_choice != '0':
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
    else:
        print("Please add options from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4:2 mouse")
        print("5: mouse mat")
        print("0: to finish")

    current_choice = input()
