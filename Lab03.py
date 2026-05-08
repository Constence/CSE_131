# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-



def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline



#gets the month from the user
def getMonth(): 
    try:
        month = int(input("Enter the month #: "))
        assert(1 <= month <= 12)
        return month

    except:
        print("Error: Invalid month")
        quit()

#getss the year from the user 
def getYear():
    try:
        year = int(input("Enter a year: "))
        assert(year >= 1753)
        return year

    except:
        print("Error: Invalid year")
        quit()

#the math to see if its a leap year (if there is no dec. when divided by 400 its a leap year)
def isLeapYear(year):
    if year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False
    
    elif year % 4 == 0: 
        return True 
    else: 
        return False


# if the leap year is true or false, return days of the year
def daysYear(year):
    if isLeapYear(year):
        return 366
    return 365

# make sure that feb. has the right num of days and months 4,6,9 and 11 do as well
def daysMonth(month, year):
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28

    if month in [4, 6, 9, 11]:
        return 30
    return 31


# the  math to see how many days have passed from 1/1/1753 and find the day of the week
def computeOffset(month, year):
    
    totalDays = 0
    for currentYear in range(1753, year):
        totalDays += daysYear(currentYear)

    for currentMonth in range(1, month):
        totalDays += daysMonth(currentMonth, year)

    offset = (totalDays + 1) % 7
    return offset


#display it all together
def display(month, year):
    numDays = daysMonth(month, year)
    dow = computeOffset(month, year)
    display_table(dow, numDays)


def main():
    month = getMonth()
    year = getYear()
    display(month, year)


main()