from utils.reader import read_file_2
list_data = read_file_2()

for data in list_data:
    date = data.split(",")[1]
    event = data.split(",")[-2]

    if event == "Rain" or event == "Snow" or event == "Rain-Snow":
        print(f"{date}  ko  {event}")
        