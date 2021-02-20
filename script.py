print('Enter Five Numbers')
# The Five Numbers Must be an Integers
while True:
    try:
        user_numbers = [int(input("first number: ")), int(input("second number: ")), int(input("third number: ")),
                        int(input("fourth number: ")), int(input("fifth number: "))]
        break
    # Hint:Just In case the user Enters an Invalid Number Such as Float
    except ValueError:
        print("kindly Enter an Integer")
        continue
        # The users_Input is to be Displayed in Ascending Order
print(sorted(user_numbers))
