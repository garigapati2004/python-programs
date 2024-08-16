# palindrome means checking the input given by the user is same as when we reverse the input given by the user

def is_palindrome(s):  # defining a function to check if a sting s is a palindrome
    
    s = s.replace(" ", "").lower()  # s.replace() removes all the spaces from the string and .lower() converts the string to lower case.
    
    return s == s[::-1]  # s[::-1] creates a reversed version of the string and s == s[::-1] checks if the original string is same as the reversed string

# Get input from the user
user_input = input("Enter a string to check if it's a palindrome: ")   # prompts the user for the input

# Check if the input is a palindrome and print the result
if is_palindrome(user_input):
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
