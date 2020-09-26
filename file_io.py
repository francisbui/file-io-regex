"""
 * Francis Bui
 * SDEV 300
 * Professor Chris Howard
 * Lab 5 - Data Analysis Application (with File I-O and Exceptions)
 * Sept 18, 2020
 * The purpose of this program is to import various csv files with try and except
 * function. After the file has been imported, it will be converted into an array
 * with Pandas. Matplotlib will then create a histogram based on the user's menu
 * selection. A report will also be displayed on the console with the respective
 * columns count, mean, standard deviation, min, and max.
"""

import sys
import statistics as stat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main_menu():
    """
    Main Menu function
    Executes first and after every function excepts when the user exits
    :return:
    """
    print('Select the file you want to analyze: \n')
    print('\t1. Population Data')
    print('\t2. Housing Data')
    print('\t3. Exit the Program')

    user_input = input()
    if user_input == '1':
        pop_data()
    elif user_input == '2':
        house_data()
    elif user_input == '3':
        exit_program()
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        main_menu()


def pop_data():

    print('\nYou have entered Population Data')
    print('Select the column you want to analyze: \n')
    print('\ta. Pop Apr 1')
    print('\tb. Pop Jul 1')
    print('\tc. Change Pop')
    print('\td. Exit Column')

    try:
        pop_change_import = pd.read_csv('PopChange.csv', skiprows=0)

        user_input = input()
        if user_input == 'a':
            print('You selected Pop Apr 1')
            column = pop_change_import['Pop Apr 1']
            data_analysis(column)
            pop_data()
        elif user_input == 'b':
            print('You selected Pop Jul 1')
            column = pop_change_import['Pop Jul 1']
            data_analysis(column)
            pop_data()
        elif user_input == 'c':
            print('You selected Change Pop')
            column = pop_change_import['Change Pop']
            data_analysis(column)
            pop_data()
        elif user_input == 'd':
            main_menu()
        else:
            print('Please enter a valid letter that corresponds to the menu item\n')
            pop_data()

    except FileNotFoundError:
        print('File could not be found\n')


def house_data():
    print('\nYou have entered Housing Data')
    print('Select the column you want to analyze: \n')
    print('\ta. Age')
    print('\tb. Bedrooms')
    print('\tc. Built')
    print('\td. Rooms')
    print('\te. Utility')
    print('\tf. Exit Column')

    try:
        housing_import = pd.read_csv('Housing.csv', skiprows=0)

        user_input = input()
        if user_input == 'a':
            print('You selected Age')
            column = housing_import['AGE']
            data_analysis(column)
            house_data()
        elif user_input == 'b':
            print('You selected Bedrooms')
            column = housing_import['BEDRMS']
            data_analysis(column)
            house_data()
        elif user_input == 'c':
            print('You selected Built')
            column = housing_import['BUILT']
            data_analysis(column)
            house_data()
        elif user_input == 'd':
            print('You selected Rooms')
            column = housing_import['ROOMS']
            data_analysis(column)
            house_data()
        elif user_input == 'e':
            print('You selected Utility')
            column = housing_import['UTILITY']
            data_analysis(column)
            house_data()
        elif user_input == 'f':
            main_menu()
        else:
            print('Please enter a valid letter that corresponds to the menu item\n')
            house_data()

    except FileNotFoundError:
        print('File could not be found\n')


def exit_program():
    """
    Exit Function
    Thank the user and exits the system
    :return:
    """
    print('')
    print('{:*^80}'.format(''))
    print('{:^80}'.format(' Thank you for using the Python Data Analysis Application '))
    print('{:^80}'.format(' We hope you try it again very soon '))
    print('{:*^80}'.format(''))
    print('')
    sys.exit()


def data_analysis(column):
    array_column = np.array(column)

    print('The statistics for this column are: ')
    print('Count = ' + str(column.count()))
    print('Mean = ' + str(column.mean()))
    print('Standard Deviation = ' + str(stat.stdev(column)))
    print('Min = ' + str(column.min()))
    print('Max = ' + str(column.max()))
    print('The Histogram of this column is now displayed')

    plt.hist(array_column, density=False, bins=100)
    # plt.xlabel('Distribution')
    # plt.ylabel('Number Of')
    plt.grid(True)
    plt.draw()
    plt.pause(60)
    plt.close()


# Application begins here
print('')
print('{:*^80}'.format(''))
print('{:^80}'.format(' Welcome to the '))
print('{:^80}'.format(' Python Data Analysis Application '))
print('{:*^80}'.format(''))
print('')

main_menu()
