def has_unique_characters(string):
    # Assuming ASCII characters
    if len(string) > 128:
        return False

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

# Test function
print(has_unique_characters('close')) # True
print(has_unique_characters('deep')) # False
