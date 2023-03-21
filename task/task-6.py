from datetime import datetime
from utils.reader import read_file
value = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv")

for response in value:
    date = response.split(",")[1]
    event = response.split(",")[-2]

    if event == "Thunderstorm":
        date_str = str(date)
        convert = datetime.strptime(date_str, "%Y-%m-%d")
        weekday_names = convert.strftime("%A")
        print(weekday_names)
