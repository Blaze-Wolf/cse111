import math
class circle:
    
    __radius = 0

    def __init__(self):
        __radius = 0
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        if radius <= 0:
            print("Invalid radius")
            self.__radius = 1.0
            return
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_diameter(self):
        return 2 * self.__radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius

def print_circle_information(my_circle):
    print(f'Area: {my_circle.get_area()}, diameter: {my_circle.get_diameter()}, circumference: {my_circle.get_circumference()}, radius: {my_circle.get_radius()}')

def main():
    my_circle = circle()
    my_circle.set_radius(-10)
    print(my_circle.get_radius())
    my_circle.radius = -20
    print(my_circle.get_radius())
    my_circle.__radius = 230
    print(my_circle.get_radius())
    print_circle_information(my_circle)

main()