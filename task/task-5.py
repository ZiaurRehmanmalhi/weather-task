from utils.reader import read_file
file_read_csv = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv")

for all_columns in file_read_csv:
    date = all_columns.split(",")[1]
    event = all_columns.split(",")[-2]

    if event in ["Rain", "Snow", "Rain-Snow"]:
        print(f"{date}  in  {event}")
