import math


##formulas for each geometric figure

def calc_rectangle(w_side, l_side):
    rect_area = l_side * w_side
    return rect_area


def calc_circle(radius):
    circle_area = math.pi * radius ** 2
    return circle_area


def calc_triangle(base, height):
    triangle_area = (base * height) / 2
    return triangle_area


def calc_trapezoid(short_base, long_base, height):
    trapezoid_area = ((short_base + long_base) / 2) * height
    return trapezoid_area


##function determining which formula to calculate

def area_calc_logic(user_calc):
    if user_calc == "1":
        l_side = float(input("Give the length: "))
        w_side = float(input("Give the width: "))
        print(calc_rectangle(w_side, l_side))
        area_calc_logic(input("What area would you like to calculate? "))
    elif user_calc == "2":
        radius = float(input("Give the radius: "))
        print(calc_circle(radius))
        area_calc_logic(input("What area would you like to calculate? "))
    elif user_calc == "3":
        base = float(input("Give the length of base: "))
        height = float(input("Give the height: "))
        print(calc_triangle(base, height))
        area_calc_logic(input("What area would you like to calculate? "))

    elif user_calc == "4":
        short_base = float(input("Give the length of the short base: "))
        long_base = float(input("Give the length of the long base: "))
        height = float(input("Give the height: "))
        print(calc_trapezoid(short_base, long_base, height))
        area_calc_logic(input("What area would you like to calculate? "))
    else:
        area_calc_logic(input("Error, Re-enter input: "))
        area_calc_logic(input("What area would you like to calculate? "))


print("This program will calculate the areas of some geometric shapes for you")
print("Choose from 1.rectangles,2. circles,3.triangles 4.trapezoid, 5.quit")
print("Enter the number of the shape")

area_calc_logic(input("What area would you like to calculate? "))