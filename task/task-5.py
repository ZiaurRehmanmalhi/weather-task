from utils.reader import get_file_contents
from utils.variables import MapperIndex


file_path = "/home/zia/ISDP/Hammad sab/Python/weather_Mar/weather-task/files/f2.csv"
file_contents = get_file_contents(file_path)

for contents in file_contents:
    date = contents.split(",")[MapperIndex.date1]
    event_list = contents.split(",")[MapperIndex.events]

    if event_list in ["Rain", "Snow", "Rain-Snow"]:     # This is a main logic of this code
        print(f"{date}  in  {event_list}")
