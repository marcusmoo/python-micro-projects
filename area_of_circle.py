import math


# returns area of circle with a given radius

def area_of_circle(radius):
    return math.pi * radius**2
    

# asks the user for a radius and returns what the area is to 2 decimal places

def main():
    radius_str = input("What is the radius of the circle: ")
    
    radius = float(radius_str)

    area = area_of_circle(radius)

    area_str = str(round(area, 2))

    print("The area of a circle with a radius of " + radius_str + " is " + area_str)

if __name__ == "__main__":
    main()

while True:
    pass