def get_file_contents(file_path):
    file_contents = []

    with open(file_path) as file_read:
        file_content = file_read.read()
        for column_value in file_content.split("\n")[1:-1]:
            file_contents.append(column_value)

    return file_contents
