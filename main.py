prompt = "Type add, show, edit, complete or exit: "
while True:
    user_input = input(prompt)
    user_input = user_input.strip()
    user_input = user_input.lower()
    # Add an item to the to do list
    if user_input == "add":
        add_item = input("Add an item: ") + '\n'
        file = open("to-do.txt", "r")
        items = file.readlines()
        file.close()
        items.append(add_item.capitalize())
        file = open("to-do.txt", "w")
        file.writelines(items)
        file.close()
        print("Item added")
    # Show items in the to do list
    elif user_input == "show":
        file = open("to-do.txt", "r")
        items = file.readlines()
        file.close()
        # new_items = [item.strip("\n") for item in items]
        for i, item in enumerate(items):
            item = item.strip("\n")
            print(f"{i+1}: {item}")
    # Exit the application
    elif user_input == "exit":
        print("Exiting!")
        break
    # Mark an item as complete, removes from to do list
    elif user_input == "complete":
        file = open("to-do.txt", "r")
        items = file.readlines()
        file.close()
        for i, item in enumerate(items):
            item = item.strip('\n')
            show_output = f"{i+1}) {item}"
            print(show_output)
        cmp_item = input("Select the number of the item to complete: ")
        cmp_item = int(cmp_item)
        items.pop(cmp_item-1)
        file = open("to-do.txt", "w")
        file.writelines(items)
        file.close()
    # Edit an existing item in the to do list
    elif user_input == "edit":
        file = open("to-do.txt", "r")
        items = file.readlines()
        file.close()
        edit_str = "Choose the number of the item to edit: "
        for i, item in enumerate(items):
            item = item.strip('\n')
            show_output = f"{i+1}) {item}"
            print(show_output)
        edit_num = input(edit_str)
        edit_num = int(edit_num)
        if edit_num < 1 or edit_num > len(items):
            print("Invalid Index")
        else:
            edit_item = input("Edit the item: ")
            items[edit_num-1] = edit_item + '\n'
        file = open("to-do.txt", "w")
        file.writelines(items)
        file.close()
    else:
        print("Invalid commands")