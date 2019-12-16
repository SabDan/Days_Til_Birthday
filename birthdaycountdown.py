# sketch of the program are the skeletons of the functions

import datetime

def print_header():
    print('-------------------------------------------------')
    print('             Birthday Countdown App')
    print('-------------------------------------------------')
    print()

def get_user_birthday_info():
    print('When is your birthday? ')
    year = int(input('Year, [YYYY]: '))
    month = int(input('Month, [MM]: '))
    day = int(input('Day, [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday

def days_between_date(original_date, target_date): #target year is 2019
    #month and day are the same as the original birthdate
    #this_year is 2019
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    birthdate = this_year - target_date
    return birthdate.days

def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days!'.format(days))
    else:
        print('Happy birthday to you!!!')


def main():
    print_header()
    bday = get_user_birthday_info()
    today = datetime.date.today()
    number_of_days = days_between_date(bday, today)
    print_birthday_info(number_of_days)

main()
