def read_file(path_1, path_2):
    file_values1 = []
    file_values2 = []
    with open(path_1) as file_read_1:
        file_contant = file_read_1.read()
        for row in file_contant.split("\n")[1:-1]:
            file_values1.append(row)
    with open("/home/zia/ISDP/Hammad sab/Python/wether_Mar/weather task 2 in csv file/files/f2.csv") as file_read:
        file_contant = file_read.read()
        for row in file_contant.split("\n")[1:-1]:
            file_values2.append(row)
    return file_values1, file_values2




