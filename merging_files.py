def reading_files_from_directory(path_folder):

    import os

    dir_list = os.listdir(path_folder)
    # path_file = f"Files\{dir_list[0]}"
    files_list = []
    for file_name in dir_list:
        with open(f"Files\{file_name}", encoding='utf-8') as f:
            file_text = f.readlines()
        files_list.append([file_name, len(file_text), file_text])
    return files_list


def sorted_list(data_files):

    def custom_key(elem):
        return elem[1]

    data_files.sort(key=custom_key)
    return data_files


def writing_file(data_files):
    with open("final_file.txt", 'w', encoding='utf-8') as f:
        for elements in data_files:
            for element in elements:
                if isinstance(element, int):
                    element = str(element)
                    f.write(checking_the_line_break(element))
                elif isinstance(element, list):
                    for subelement in element:
                        f.write(checking_the_line_break(subelement))
                else:
                    f.write(checking_the_line_break(element))


def checking_the_line_break(line_text):
    if not line_text[-1:] == '\n':
        line_text += '\n'
    return line_text


data_files = reading_files_from_directory("Files")
print(f"Список до сортировки")
print(data_files)

sorted_data_files = sorted_list(data_files)
print(f"Список после сортировки")
print(sorted_data_files)

writing_file(sorted_data_files)