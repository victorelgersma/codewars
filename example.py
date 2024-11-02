def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    pi = 3.14159
    return pi * (radius ** 2)

def mai():
    radius = 5
    area = calculate_area(radius)
    prin(f"The area of the circle with radius {radius} is {area}")

if __name__ == "__main__":
    main()

