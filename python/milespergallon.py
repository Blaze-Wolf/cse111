
# Python

# This file will calculate the miles per gallon of a trip


def calculate_miles_per_gallon(starting_mile, ending_mile, gallons_used):
    assert starting_mile > 0
    assert ending_mile > 0
    assert gallons_used > 0
    assert ending_mile > starting_mile
    '''Calculate and return the miles per gallon (mph)
    start_milage - the starting milage on the car before the strip
    end_milage - the ending milage ont he car after the trip
    gallons - the number of gallons of gas used on the trip.
    mpg = end - start / gallons'''
    miles_traveled = ending_mile - starting_mile
    mpg = miles_traveled / gallons_used
   # assert mpg >= 9
    return mpg

def obtain_user_input():
    '''Obtain the starting mile, ending mile, and gallons used from the user and return them.'''
    starting_mile = int(input('Input car mileage before trip started: '))
    ending_mile = int(input('Input car ending mileage after the trip: '))
    gallons_used = int(input('Input the number of gallons of gas used on the trip: '))
    return starting_mile, ending_mile, gallons_used


def main():
    '''Ask the user for the needed items and call calculate_miles_per_gallong
    to get the miles per gallon (mpg)'''

    starting_mile, ending_mile, gallons_used = obtain_user_input()

    miles_per_gallon = calculate_miles_per_gallon(starting_mile, ending_mile, gallons_used)
    print(f'The miles per gallon for this trip was: {miles_per_gallon:.2f}')


if __name__ == '__main__':
    main()
