def get_user_age():
    '''Obtain a correct age from the user and return it'''
    done = False
    while not done:
        try:
            age = int(input('Please input your age: '))
            if( 0 <= age <= 125):
                done = True
            else:
                # print('Please input a valid age (0-125)')
                raise ValueError ('Invalid integer')
        except ValueError as ve:
            print(f'Invalid input, please input a valid age (0-125): {ve}')
        except KeyboardInterrupt as keyboard_interrupt:
            print(f'Nice try but you must input your age.')
        except EOFError as eof_error:
            print(f'That also does not work. Please input your age.')
        finally:
            print('In my finally block.')
    return age

def main():
    age = get_user_age()
    print(f"Your age is: {age}")
main()