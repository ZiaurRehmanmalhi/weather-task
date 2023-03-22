from datetime import datetime
from utils.reader import read_file


read_csv_file = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv")

for csv_response in read_csv_file:
    date_list = csv_response.split(",")[1]
    event_list = csv_response.split(",")[-2]

    if event_list == "Thunderstorm":
        date_string = str(date_list)    # Date converting to string.
        convert_date = datetime.strptime(date_string, "%Y-%m-%d")    # This code should be print date & time.
        weekday_names = convert_date.strftime("%A")    # Change date into week_days.

        print(weekday_names)
