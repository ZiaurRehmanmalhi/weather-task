from datetime import datetime
from utils.reader import get_file_contents
from utils.variables import MapperIndexF2


file_path = "../../weather-task/files/f2.csv"
read_csv_file = get_file_contents(file_path)

for contents in read_csv_file:
    date = contents.split(",")[MapperIndexF2.date]
    event_list = contents.split(",")[MapperIndexF2.events]

    if event_list == "Thunderstorm":
        date_string = str(date)    # Date converting to string.
        convert_date = datetime.strptime(date_string, "%Y-%m-%d")    # This code should be print date & time.
        weekday_names = convert_date.strftime("%A")    # Change date into week_days.

        print(weekday_names)
