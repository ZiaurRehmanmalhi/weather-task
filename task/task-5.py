from utils.reader import read_file


read_csv_file = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv")

for csv_response in read_csv_file:
    date_list = csv_response.split(",")[1]
    event_list = csv_response.split(",")[-2]

    if event_list in ["Rain", "Snow", "Rain-Snow"]:     # This is a main logic of this code
        print(f"{date_list}  in  {event_list}")
