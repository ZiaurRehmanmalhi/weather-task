from utils.reader import read_file


read_csv_file = read_file("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f1.csv")

for csv_response in read_csv_file:
    date_list = csv_response.split(",")[0]
    max_temp_list = csv_response.split(",")[1]
    min_temp_list = csv_response.split(",")[3]
    average = (int(max_temp_list) - int(min_temp_list)) / 2     # This line get average calculation.

    print(f"date {date_list} maximum-temp {max_temp_list} minimum-temp {min_temp_list} and average between {average}")
