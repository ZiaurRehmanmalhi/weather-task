from utils.reader import read_file
path_1 = "/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f1.csv"
path_2 = "/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv"
file_1, file_2 = read_file(path_1, path_2)

for data in file_2:
    date = data.split(",")[1]
    event = data.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"{date}  in  {event}")
