from datetime import datetime
from utils.reader import get_file_contents
from utils.variables import MapperIndex


file_path = "/home/zia/ISDP/Hammad sab/Python/weather_Mar/weather-task/files/f2.csv"
read_csv_file = get_file_contents(file_path)

for contents in read_csv_file:
    date = contents.split(",")[MapperIndex.date1]
    event_list = contents.split(",")[MapperIndex.events]

    if event_list == "Thunderstorm":
        date_string = str(date)    # Date converting to string.
        convert_date = datetime.strptime(date_string, "%Y-%m-%d")    # This code should be print date & time.
        weekday_names = convert_date.strftime("%A")    # Change date into week_days.

        print(weekday_names)
