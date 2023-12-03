import re

def find_first_and_last_digits (string):
    digits = re.findall(r'\d', string)
    if digits:
        return int(digits[0]), int(digits[-1])
    else:
        return None, None

calibration_values = 0

with open('input.txt', 'r') as file:
    for line in file:
        # Process the line and strip /n character
        processed_line = line.strip()
        first_digit, last_digit = find_first_and_last_digits(processed_line)

        if first_digit is not None and last_digit is not None:
            calibration_values += int(f"{first_digit}{last_digit}")

        elif first_digit is not None and last_digit is None:
            calibration_values += int(f"{first_digit}{first_digit}")

        elif first_digit is None and last_digit is not None:
            calibration_values += int(f"{last_digit}{last_digit}")

        else: 
            calibration_values += 0

print("Total sum of calibration values:", calibration_values)


 
