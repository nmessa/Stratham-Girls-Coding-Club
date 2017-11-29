PI = 3.14159265358979   # global constant -- can be used by all functions

def circleArea(radius):
    return PI*radius*radius    # use value of global constant PI

def circleCircumference(radius):
    return 2*PI*radius         # use value of global constant PI

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = circleArea(radius)
    circumference = circleCircumference(radius)
    print('circle area with radius', radius, '=', round(area,2))
    print('circumference with radius', radius, '=', round(circumference,2))

main()
