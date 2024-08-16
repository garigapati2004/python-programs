def is_armstrong(number):  # defining a function to check if a number is an armstrong number or not
    original_value = number  # store the original number for comparing
    sum = 0  # initialize a variable to store the sum of each digit raised to the power of the number of digits

    while number > 0:
        digit = number % 10 # extracting the last digit of a given number
        sum += (digit ** length)  # add the digit raised to the power of the number of digits in the given number to the sum
        number //= 10 # remove the last digit from the number

    return sum == original_value # check if the sum of the digits raised to the power of the number of digits is equal to the original number


number = int(input("Enter a number: ")) # get a number from the user
length = len(str(number))  # caluclate the number of digits in the number

# check if the number is an armstrong number and print the result
if is_armstrong(number):
    print(f"{number} is an armstrong number.")

else:
    print(f"{number} is not an armstrong number.")
