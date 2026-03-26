def is_leap_year(year):
    """It gives if the given year is leap year or not"""
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True
    return leap
leap_year = is_leap_year(2000)
print(leap_year)