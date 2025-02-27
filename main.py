prompt = "Type add, show, edit, complete or exit: "
items = []
while True:
    user_input = input(prompt)
    user_input = user_input.strip()
    user_input = user_input.lower()
    if user_input == "add":
        add_item = input("Add an item: ") + '\n'
        items.append(add_item.capitalize())
        file = open("to-do.txt", "w")
        file.writelines(items)
        print("Item added")
    elif user_input == "show":
        for i, item in enumerate(items):
            show_output = f"{i+1}) {item}"
            print(show_output)
    elif user_input == "exit":
        break
    elif user_input == "complete":
        for i, item in enumerate(items):
            show_output = f"{i+1}) {item}"
            print(show_output)
        cmp_item = input("Select the number of the item to complete: ")
        cmp_item = int(cmp_item)
        items.pop(cmp_item-1)
    elif user_input == "edit":
        edit_str = "Choose the number of the item to edit: "
        for i, item in enumerate(items):
            show_output = f"{i+1}) {item}"
            print(show_output)
        edit_num = input(edit_str)
        edit_num = int(edit_num)
        if edit_num < 1 or edit_num > len(items)+1:
            print("Invalid Index")
        else:
            edit_item = input("Edit the item: ")
            items[edit_num-1] = edit_item
    else:
        print("Invalid commands")



