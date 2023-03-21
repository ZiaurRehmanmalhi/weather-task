def read_file(path):
    file_values = []

    with open(path) as file_read:
        file_contant = file_read.read()
        for row in file_contant.split("\n")[1:-1]:
            file_values.append(row)

    return file_values
