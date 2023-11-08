#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_b = 0
    for y in range(len(roman_string)):
        if y > 0 and roman_a[roman_string[y]] > roman_a[roman_string[y - 1]]:
            roman_b += roman_a[roman_string[y]] - 2 * \
                        roman_a[roman_string[y - 1]]
        else:
            roman_b += roman_a[roman_string[y]]
    return roman_b
