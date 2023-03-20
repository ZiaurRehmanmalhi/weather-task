from utils.reader import read_file_2
list_data = read_file_2()

for data in list_data:
    date = data.split(",")[1]
    event = data.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"{date}  in  {event}")
