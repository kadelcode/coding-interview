def replace_spaces(input_string: str) -> str:
    """
    This function replaces spaces in a string with '%20'.
    
    Args:
        input_string: The input string

    Returns:
        The string with spaces replaced by '%20'.
    """
    
    # create an empty list
    result = []

    # loop through each character of the string
    for char in input_string:
        if char == ' ':
            result.append('%20')
        else:
            result.append(char)

    return ''.join(result)

# Test case
input_string = "Hello World! How are you?"
output_string = replace_spaces(input_string)
print(output_string)
