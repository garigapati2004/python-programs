def sum_of_digits(number):
    number = abs(number)   # It is used to convert negative number into positive number
    sum = 0

    while number > 0:
        digit = number % 10   # It gives the last digit of a number which is given by the user
        sum += digit  # It adds the last digit of a number to the sum
        number //= 10  # Now it removes the last digit of a number given by the user

        # It continues the loop until the number is greater than zero
    return sum

number = int(input("Enter a number: "))
print(f"The sum of the digits in {number} is {sum_of_digits(number)}")
