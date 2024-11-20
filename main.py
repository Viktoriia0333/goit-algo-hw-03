# first task
from datetime import datetime
import random


def get_days_from_today(date):
    current_date = datetime.now()
    try:
        converted_date = datetime.strptime(date, '%Y.%m.%d')
        days_from_today = current_date - converted_date
        return days_from_today.days
    except ValueError:
        return 'Please, enter a date in the right format'


# date = input('Enter date (format: \'РРРР.ММ.ДД\'): ')
# print(get_days_from_today(date))


# second task
def get_numbers_ticket(min, max, quantity):
    my_set = set()
    if min < 1 or max > 1000:
        return []
    elif quantity > (max-min+1):
        return f'There are no no {quantity} numbers in this range.'
    else:
        while len(my_set) < quantity:
            i = random.randint(min, max)
            my_set.add(i)
    return list(my_set)


print(get_numbers_ticket(1, 12, 20))
