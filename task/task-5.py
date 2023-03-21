from utils.reader import read_file
path = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv")

for data in path:
    date = data.split(",")[1]
    event = data.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"{date}  in  {event}")
