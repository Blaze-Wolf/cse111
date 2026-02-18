import csv
CITY_INDEX = 0

def read_file_data_into_list(file_name):
    with open(file_name, 'rt') as file_handle:
        next(file_handle)
        data_list = []
        for line in file_handle:
            data_list.append(line.strip().split(','))
        return data_list

def read_file_data_into_list_using_csv(file_name):
    with open(file_name, 'rt') as file_handle:
        reader = csv.reader(file_handle)
        next(reader)
        data_list = []
        for line in reader:
            data_list.append(line)
        return data_list
    
def read_file_data_into_dictionary_using_csv(file_name):
    with open(file_name, 'rt') as file_handle:
        reader = csv.reader(file_handle)
        next(reader)
        data_dictionary = {}
        for city_info in reader:
            data_dictionary[city_info[CITY_INDEX]] = city_info
        return data_dictionary


def main():
    file_name = 'favoritecities.csv'
    data_list = read_file_data_into_list(file_name)
    print(data_list)
    # for item in data_list:
      #  print(item[CITY_INDEX])
    
    data_list2 = read_file_data_into_list_using_csv(file_name)
    print(data_list2)
    city_dictionary = read_file_data_into_dictionary_using_csv(file_name)
    for key, city_info in city_dictionary.items():
        print(key, city_info)
main()