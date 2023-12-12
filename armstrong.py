def is_armstrong_number(number):
    # Convert the number to a string to count its digits
    num_str = str(number)
    
    # Calculate the number of digits
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return digit_sum == number

# Input a number from the user
num = int(input("Enter a positive integer: "))

if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


