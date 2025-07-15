#birthYear = int(input('Enter your birthdate: '))
#age = 2025 - birthYear
#print("your age is: " + str(age))

from datetime import date
import time

def calculate_age(birth_date_str):
    """
    Calculates age in years based on a birth date string.

    Args:
        birth_date_str (str): The birth date in 'YYYY-MM-DD' format.

    Returns:
        int: The calculated age in years.
    """
    try:
        birth_year, birth_month, birth_day = map(int, birth_date_str.split('-'))
        born = date(birth_year, birth_month, birth_day)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

    today = date.today()
    age = today.year - born.year
    if (today.month, today.day) < (born.month, born.day):
        age -= 1
    return age

if __name__ == "__main__":
    print("Age Calculator")
    birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")

    start_time = time.time()  # Record start time

    age_result = calculate_age(birth_date_input)

    end_time = time.time()    # Record end time
    running_time = end_time - start_time

    if age_result is not None:
        print(f"You are {age_result} years old.")
        print(f"Calculation running time: {running_time:.6f} seconds.")