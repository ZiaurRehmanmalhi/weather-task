from utils.reader import get_file_contents
from utils.variables import MapperIndexF1


file_path = "../../weather-task/files/f1.csv"
file_contents = get_file_contents(file_path)

for contents in file_contents:
    date_list = contents.split(",")[MapperIndexF1.date]
    max_temperature = contents.split(",")[MapperIndexF1.max_temperature]
    min_temperature = contents.split(",")[MapperIndexF1.min_temperature]
    average = (int(max_temperature) - int(min_temperature)) / 2     # This line get average and calculation.

    print(f"date {date_list} "
          f"maximum-temp {max_temperature} "
          f"minimum-temp {min_temperature} "
          f"and average between {average}")
