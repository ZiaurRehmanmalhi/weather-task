from utils.reader import get_file_contents
from utils.variables import MapperIndexF2


file_path = "../../weather-task/files/f2.csv"
file_contents = get_file_contents(file_path)

for contents in file_contents:
    date = contents.split(",")[MapperIndexF2.date]
    event_list = contents.split(",")[MapperIndexF2.events]

    if event_list in ["Rain", "Snow", "Rain-Snow"]:     # This is a main logic of this code
        print(f"{date}  in  {event_list}")
