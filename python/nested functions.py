def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def process_data(process_function, data):
    processed_data = []
    for item in data:
        temp = process_function(item)
        process_data.append(temp)

    return process_data

def main():
    print(celsius_to_fahrenheit(100))

main()
