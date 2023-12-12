
def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            division_sum += i

    return division_sum == num

# Input a number to check if it's a perfect number
num = int(input("Enter a number to check if it's a perfect number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")