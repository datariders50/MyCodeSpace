from datetime import datetime, timedelta

def get_start_end_epoch_for_day(year, month, day):
    # Start of the day (00:00:00)
    start_of_day = datetime(year, month, day)
    # End of the day (23:59:59)
    end_of_day = start_of_day + timedelta(hours=23, minutes=59, seconds=59)
    
    # Convert to epoch timestamps
    start_epoch = int(start_of_day.timestamp())
    end_epoch = int(end_of_day.timestamp())
    
    return start_epoch, end_epoch

# Example usage for a specific day:
year, month, day = 2024, 10, 25
start_epoch, end_epoch = get_start_end_epoch_for_day(year, month, day)

print("Start of day:", start_epoch)
print("End of day:", end_epoch)



from datetime import datetime, timedelta

def get_all_dates(start_date, end_date):
    # Create a list to store dates
    date_list = []
    # Start from the start date
    current_date = start_date
    
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    
    return date_list

# Example usage
start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 10, 10)

dates = get_all_dates(start_date, end_date)
for date in dates:
    print(date.strftime("%Y-%m-%d"))
