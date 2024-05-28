def reverse_c_style_string(c_string):
    # convert the C-style string into a list of characters
    char_list = list(c_string)

    # get the length of the string excluding the null character
    length = len(char_list) - 1

    # initialize two pointers, one at the start
    # one at the end (before the null characters)
    left, right = 0, length

    # swap characters until the two pointers meet in the middle
    while left < right:
        # swap the characters
        char_list[left], char_list[right] = char_list[right], char_list[left];

        # move the pointers
        left += 1
        right -= 1

    # convert the list of characters back to a string
    return ''.join(char_list)

# Test the function
c_string = "abcd\0"
reversed_c_string = reverse_c_style_string(c_string)
print(reversed_c_string) # output "dcba\0"
