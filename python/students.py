import csv

def read_dictionary(file_name):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    with open(file_name, "rt") as file:
        line = csv.reader(file)
        next(line)
        dictionary = {}
        for key, value in line:
            dictionary[key] = value
    return dictionary

def main():
    STUDENT = 0
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    student_file = "students.csv"
    student_dict = read_dictionary(student_file)
    if i_number in student_dict:
        student = student_dict[i_number]
        print(student)
    else:
        print("No such student")
if __name__ =="__main__":
    main()