from utils.reader import read_file

list_data = read_file()
for data in list_data:
    date = data.split(",")[0]
    max_temp = data.split(",")[1]
    min_temp = data.split(",")[3]
    avrage = (int(max_temp) - int(min_temp))/2


    print(f"date {date} maximum-temp {max_temp} minimum-temp {min_temp} and avrage between {avrage}")
