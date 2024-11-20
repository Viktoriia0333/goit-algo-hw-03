# first task
from datetime import datetime
import random
import re


def get_days_from_today(date):
    current_date = datetime.now()
    try:
        converted_date = datetime.strptime(date, '%Y-%m-%d')
        days_from_today = current_date - converted_date
        return days_from_today.days
    except ValueError:
        return 'Please, enter a date in the right format'


date = input('Enter date (format: \'РРРР-ММ-ДД\'): ')
print(get_days_from_today(date))


# second task
def get_numbers_ticket(min, max, quantity):
    my_set = set()
    if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int):
        if quantity > (max-min+1):
            return f'There are no {quantity} numbers in this range.'
        if min >= 1 and max <= 1000:
            while len(my_set) < quantity:
                i = random.randint(min, max)
                my_set.add(i)
    return list(my_set)


print(get_numbers_ticket(1, 12, 0.5))


# third task
def normalize_phone(phone_number):
    cleaned_string = re.sub(r'[^\d+]', '', phone_number)
    if cleaned_string.startswith('+'):
        if not cleaned_string.startswith('+38'):
            return f'Only ukrainian numbers supported'
    elif cleaned_string.startswith('380'):
        cleaned_string = '+' + cleaned_string
    else:
        cleaned_string = '+38'+cleaned_string
    return cleaned_string


print(normalize_phone('0968645223'))
