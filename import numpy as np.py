import numpy as np

def business_days(start_date, end_date):
    return np.busday_count(start_date, end_date)

# Usage
start_date = '2022-01-01'
end_date = '2022-01-31'
# print output
print(business_days(start_date, end_date))