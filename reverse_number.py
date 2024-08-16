def reverse_number(number):
    # Store the sign of the number
    sign = -1 if number < 0 else 1
    
    # Convert the number to positive
    number = abs(number)
    
    # Initialize the reversed number
    reversed_number = 0
    
    # Loop to reverse the digits
    while number > 0:
        digit = number % 10  # Get the last digit
        reversed_number = reversed_number * 10 + digit  # Build the reversed number
        number //= 10  # Remove the last digit
    
    # Restore the sign
    return sign * reversed_number

# Example usage
number = int(input("Enter a number: "))
print(f"The reverse of {number} is {reverse_number(number)}.")
