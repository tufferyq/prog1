"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""


def longest_substring_in_order(string):
    """
    This function gives out the longest substring where the letters are in
    strictly alphabetic order, without repeating identical letters.
    :param string: str,
    :return longest_substring: str,
    """
    if len(string) == 0:
        return ""  # Handle empty strings

    longest_substring = string[0]  # Start with the first letter by default
    substring = string[0]

    for letter in range(1, len(string)):
        # Check if the next letter is strictly greater than the current one
        if string[letter - 1] < string[letter]:
            substring += string[letter]
        else:
            substring = string[letter]  # Start a new substring

        if len(substring) > len(longest_substring):
            longest_substring = substring

    return longest_substring