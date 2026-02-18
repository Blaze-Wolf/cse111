import math
def calculate_can_volume(radius, height):
    return math.pi * radius * radius * height

def calculate_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def calculate_storage_efficiency(radius, height):
    return calculate_can_volume(radius, height) / calculate_surface_area(radius, height)

def main():
    with open("cans.txt") as file:
        header = file.readline()

        for line in file:
            line_clean = line.strip()
            parts = line_clean.split(", ")
            radius = float(parts[1])
            height = float(parts[2])
            print(calculate_storage_efficiency(radius, height))



main()