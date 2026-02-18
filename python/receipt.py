import csv

def read_products(file_name):
    with open(file_name, "rt") as file:
        line = csv.reader(file)
        next(line)
        dictionary = {}
        for key, name, price in line:
            dictionary[key] = (name, float(price))
    return dictionary

def read_request(file_name, products_dict):
    
    with open(file_name, "rt") as file:
        line = csv.reader(file)
        next(line)
        for row in line:
            product_number = row[0]
            quantity = int(row[1])
            product = products_dict[product_number]
            product_name = product[0]
            product_price = product[1]
            print(product_name, quantity, product_price)

def main():
    print("Inkom Emporium")
    print()
    products_dict = read_products("products.csv")
    read_request("request.csv", products_dict)


if __name__ == "__main__":
    main()