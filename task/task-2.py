from utils.reader import read_file


file_read_csv = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f1.csv")

for data in file_read_csv:
    date = data.split(",")[0]
    max_temp = data.split(",")[1]
    min_temp = data.split(",")[3]
    average = (int(max_temp) - int(min_temp))/2

    print(f"date {date} maximum-temp {max_temp} minimum-temp {min_temp} and average between {average}")
