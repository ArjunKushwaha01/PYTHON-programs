def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisors_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    
    return divisors_sum == number

# Input a number from the user
num = int(input("Enter a positive integer: "))

if is_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")



