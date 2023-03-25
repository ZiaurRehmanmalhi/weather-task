from utils.reader import get_file_contents
from utils.variables import MapperIndexF1

file_path = "../../weather-task/files/f1.csv"
file_contents = get_file_contents(file_path)

for contents in file_contents:
    date = contents.split(",")[MapperIndexF1.date]
    max_temperature = contents.split(",")[MapperIndexF1.max_temperature]
    min_temperature = contents.split(",")[MapperIndexF1.min_temperature]
    difference = int(max_temperature) - int(min_temperature)  # This line get calculation and convert to integer.

    print(f"date {date}"
          f" max_temperature {max_temperature}"
          f" min-temperature {min_temperature}"
          f" and difference between {difference}")
