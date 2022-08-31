import datetime


def getAge():
    year = int(input('Enter your Year of birth: '))
    month = int(input('Enter your Month of birth (in Numeric representation): '))
    day = int(input('Enter your Day of birth: '))
    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, day)
    age = int((today-dob).days / 365.25)
    print('Your age is ', age, 'years old')


getAge()
