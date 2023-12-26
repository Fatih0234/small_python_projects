import random 
import sys
import os
from datetime import date


from datetime import timedelta, datetime, date


def birthday_generator(num):
    """Returns a list of number random date objects for birthdays."""

    birthdays = []
    for i in range(num):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear =date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def get_match(iteration, number_people):
    same_birthdays = 0
    for i in range(iteration):
        birthdays = birthday_generator(number_people)
        if i % 10000 == 0:
            print('{} simulations run...'.format(i))
        if len(birthdays) != len(set(birthdays)):
            same_birthdays += 1

    print(f'Out of {iteration} simulations of {number_people}people, there was a matching birthday in the same group {same_birthdays} times. and the ratio is {same_birthdays/iteration}')
    
if __name__ == '__main__':
    iteration = 100000
    number_people = 23
    get_match(iteration, number_people)
    """
        0 simulations run...
        10000 simulations run...
        20000 simulations run...
        30000 simulations run...
        40000 simulations run...
        50000 simulations run...
        60000 simulations run...
        70000 simulations run...
        80000 simulations run...
        90000 simulations run...
        Out of 100000 simulations of 23people, there was a matching birthday in the same group 50698 times. and the ratio is 0.50698
    """