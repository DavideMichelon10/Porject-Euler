months = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def sundays(year, days, sundays = 0):

    for index, month_days in enumerate(months):
        if index == 1 and is_leap(year):
            days += 29
        else: days += month_days
        if days % 7 == 0:
            sundays += 1
    
    return sundays

# every year starts one day later than the previous one
# Exept leap year which makes next year starts 2 days later
def get_days_later(year, counter ):
    if year == 1900: return 1
    # check year - 1 bc a 
    if is_leap(year - 1):
        counter += 2
    else:
        counter+=1
    return counter if counter < 7 else counter % 7

counter = 0
days_of_later_year_start = 0

for year in range(1900, 2001):

    days_of_later_year_start = get_days_later(year, days_of_later_year_start)
    sundays_counter = sundays(year, days_of_later_year_start) 

    if year != 1900:
        counter += sundays_counter

print(counter)