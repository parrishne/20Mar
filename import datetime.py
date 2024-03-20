import datetime

def count_business_days(start_date, end_date):
    count = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            count += 1
        current_date += datetime.timedelta(days=1)
    return count

#test the code
start_date = datetime.date(2018, 12, 1)
end_date = datetime.date(2018, 12, 31)
print(count_business_days(start_date, end_date))