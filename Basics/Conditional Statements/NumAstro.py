# Program for numerology

def sum_digits_to_single(number):
    """
    Sums the digits of a number repeatedly until a single-digit result is obtained.

    Args:
        number (int): The input integer.

    Returns:
        int: The single-digit sum.
    """
    while number >= 10:
        digit_sum = 0
        # Convert the number to a string to iterate through its digits
        for digit_char in str(number):
            digit_sum += int(digit_char)
        number = digit_sum
    return number

birthDay = int(input("Enter the day number (0 to 31) of the Birth:"))
numeroLogy = sum_digits_to_single(birthDay)

match numeroLogy:
    case 1:
        print("Leadership, independence, ambition, and a pioneering spirit.")
    case 2:
        print("Diplomacy, cooperation, harmony, and sensitivity.")
    case 3:
        print("Creativity, communication, optimism, and social skills.")
    case 4:
        print("Practicality, stability, organization, and hard work.")
    case 5:
        print("Freedom, adventure, change, and adaptability.")
    case 6:
        print("Nurturing, responsibility, compassion, and balance.")
    case 7:
        print("Spirituality, introspection, analysis, and wisdom.")
    case 8:
        print("Ambition, authority, success, and material achievements.")
    case 9:
        print("Humanitarianism, compassion, idealism, and completion.")
    case _:
        print("First get born and get a life and then come.")