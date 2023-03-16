def read_file():
    file_values = []
    with open("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f1.csv") as file_read:
        file_contant = file_read.read()

        for row in file_contant.split("\n")[1:-1]:
            file_values.append(row)
            # print(row)
        return file_values

