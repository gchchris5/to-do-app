filepath = "to-do.txt"


def get_items(filepath_in=filepath):
    with open(filepath_in, "r") as read_file:
        return_items = read_file.readlines()
    return return_items


def write_items(items_in, filepath_in=filepath):
    with open(filepath_in, "w") as write_file:
        write_file.writelines(items_in)
