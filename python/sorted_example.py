def print_students(students):
    print()
    for student in students:
        print(student)


def main():
    FIRST_NAME_INDEX = 0
    LAST_NAME_INDEX = 1
    READING_LEVEL_INDEX = 2
    students = [
    ["Robert", "Smith", 6.7],
    ["Annie", "Smith", 6.2],
    ["Robert", "Lopez", 7.1],
    ["Sean", "Li", 5.6],
    ["Sofia", "Lopez", 5.3],
    ["Lily", "Harris", 6.7],
    ["Alex", "Harris", 5.8],
    ["Billy", "Bob", 6.3],
    ["Jeannie", "Roberts", 5.9],
    ["Bubba", "Bob", 7.9],
    ["Lilly", "Smith", 4.9],
    ["Jeannie", "Loper", 6.4],
    ["Gilligan", "Island", 4.1]]
    print_students(students)
    sorted_students = sorted(students)
    print_students(sorted_students)

    sorted_students_by_last_name = sorted(students, key = lambda student : student[LAST_NAME_INDEX])
    print_students(sorted_students_by_last_name)
    sorted_students_by_last_name = sorted(students, key = lambda student : student[READING_LEVEL_INDEX])
    print_students(sorted_students_by_last_name)
    sorted_students_by_last_name = sorted(students, key = lambda student : student[READING_LEVEL_INDEX], reverse= True)
    print_students(sorted_students_by_last_name)

main()
