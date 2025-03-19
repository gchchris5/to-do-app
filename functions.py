import time
filepath = "to-do.txt"


def get_items(filepath_in=filepath):
    with open(filepath_in, "r") as read_file:
        return_items = read_file.readlines()
    return return_items


def write_items(items_in, filepath_in=filepath):
    with open(filepath_in, "w") as write_file:
        write_file.writelines(items_in)


def welcome_message():
    now_date = time.strftime("%A, %B %d, %Y")
    now_time = time.strftime("%I:%M:%S %p")
    print(f"Welcome, the date is {now_date}. The time is {now_time}")


if __name__ == "__main__":
    welcome_message()

