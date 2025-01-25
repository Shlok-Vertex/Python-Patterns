import calendar

while True:
    year = int(input("Enter the year : "))
    month = int(input("Enter the month : "))

    print(calendar.month_name[month],year)
    print(calendar.month(year,month))

    ans = input("Do you want to continue (y/n) : ")
    ans = ans.lower()
    if ans != 'y':
        break

