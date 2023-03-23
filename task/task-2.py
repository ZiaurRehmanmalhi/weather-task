from utils.reader import get_file_contents
from utils.variables import MapperIndex


file_path = "/home/zia/ISDP/Hammad sab/Python/weather_Mar/weather-task/files/f1.csv"
file_contents = get_file_contents(file_path)

for contents in file_contents:
    date_list = contents.split(",")[MapperIndex.date]
    max_temperature = contents.split(",")[MapperIndex.max_temperature]
    min_temperature = contents.split(",")[MapperIndex.min_temperature]
    average = (int(max_temperature) - int(min_temperature)) / 2     # This line get average and calculation.

    print(f"date {date_list} "
          f"maximum-temp {max_temperature} "
          f"minimum-temp {min_temperature} "
          f"and average between {average}")
