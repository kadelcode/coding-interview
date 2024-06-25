def isSubstring(s1, s2):
    """
    This function checks if s2 is a
    substring of s1.

    Args:
        s1: The first string
        s2: Second string

    Returns:
        s2 in s1

    """
    return s2 in s1

def isRotation(s1, s2):
    """
    This function checks if s2 is  a
    rotation of s1

    Args:
        s1: First string
        s2: Second string

    Returns:
        isSubstring function of the concatenated s1, and s2

    """
    if len(s1) != len(s2):
        return False

    concatenated_s1 = s1 + s1
    
    return isSubstring(concatenated_s1, s2)

# Example usage
s1 = "waterbottle"
s2 = "erbottlewat"
print(isRotation(s1, s2)) # Output: True
