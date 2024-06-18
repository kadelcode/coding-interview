# rotate_image.py

def rotate_image(image):
    """
    This function rotates an image represented by a matrix
    by 90 degrees clockwise in-place.

    Args:
        image: A 2D list representing the image to rotate.
    """
    n = len(image)

    # swap rows and columns
    for i in range(n):
        for j in range(i, n):
            image[i][j], image[j][i] = image[j][i], image[i][j]

    # reverse each row of the transposed image
    for row in image:
        row.reverse()

# Test case
image = [[1, 3, 5], [2, 4, 6], [5, 10, 15]]
rotate_image(image)
print(image)
