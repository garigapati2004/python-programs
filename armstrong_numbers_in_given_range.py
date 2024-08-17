def is_armstrong(number, length):  # Define a function to check if a number is an armstrong number
    original_value = number  # Store the original number for comparing later
    sum = 0  # Initialize a variable to store the sum of each digit raised to the power of the number of digits
    

    while number > 0: # loop until there are no more digits left in the number
        digit = number % 10 # Extract the last digit of the number
        sum += (digit ** length) # Add the digit raised to the power of the number of digits
        number //= 10 # Remove the last digit from the number 

    return sum == original_value # Returns true if the sum equals to the original number (It is an armstrong number )

def find_armstrong_numbers(start, end): # Define a function to find the armstrong numbers in a given range
    armstrong_numbers = [] # Initialize an empty list to sore the armstrong numbers
    for num in range(start, end + 1): # Loop through each number from start to end (starting and ending numbers both are included )
        length = len(str(num)) # Caluclate the number of digits in the current number
        if is_armstrong(num, length): # Check if the current number is an armstrong number 
            armstrong_numbers.append(num) # Insert the number to the list if it is an armstrong number
    return armstrong_numbers # Return the list of armstrong number

# Taking input from the user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

# Find and print armstrong numbers in the specified range
armstrong_numbers = find_armstrong_numbers(start_num, end_num) # Call the function to find armstrong numbers
if armstrong_numbers: # Check if the list of armstrong numbers is not empty
    print(f"Armstrong numbers from {start_num} to {end_num}: {armstrong_numbers}") # Print the armstrong numbers
else: # If the list is empty
    print(f"There are no armstrong numbers from {start_num} to {end_num}.") # Inform the users that no Armstrong numbers were found
