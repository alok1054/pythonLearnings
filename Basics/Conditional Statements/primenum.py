def is_prime_while_loop(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False

    # Start checking for divisors from 2
    i = 2
    # Loop while i*i is less than or equal to num
    # This optimizes the check by only going up to the square root
    while i * i <= num:
        # If num is divisible by i, it's not prime
        if num % i == 0:
            return False
        # Move to the next potential divisor
        i += 1

    # If no divisors were found, the number is prime
    return True

# Example usage:
number_to_check = int(input("Enter the integer number: "))
if is_prime_while_loop(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
