from utils.reader import read_file
value = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv")

for response in value:
    date = response.split(",")[1]
    event = response.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"{date}  in  {event}")
