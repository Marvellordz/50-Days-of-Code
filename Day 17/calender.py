import calendar


def getCalendar():
    year = int(input('Enter the year: '))
    month = int(
        input('Enter the month in number (E.g 1 for Jan, 12 for Dec.): '))
    print(calendar.month(year, month))


getCalendar()
