from datetime import datetime

def days_between_dates(date1, date2):
    # Convert the input strings to datetime objects
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')
    
    # Calculate the difference between the dates and return the number of days
    return abs((date2_obj - date1_obj).days)

# Input dates
date1 = input("Input Date1 (YYYY-MM-DD): ")
date2 = input("Input Date2 (YYYY-MM-DD): ")

# Print the result
print("Number of days between the dates:", days_between_dates(date1, date2))
