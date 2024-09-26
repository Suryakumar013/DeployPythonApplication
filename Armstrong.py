def is_armstrong(number):
    # Convert the number to string to easily iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of the digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == number

# Input from the user
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
