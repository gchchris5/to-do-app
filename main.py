prompt = "Type add, show, edit, complete or exit: "
inv_cmd = "Invalid Command."
while True:
    user_input = input(prompt)
    user_input = user_input.strip()
    user_input = user_input.lower()

    # Add an item to the to do list
    if user_input.startswith("add"):
        add_item = user_input[4:] + "\n"
        with open("to-do.txt", "r") as file:
            items = file.readlines()
        items.append(add_item.capitalize())
        with open("to-do.txt", "w") as file:
            file.writelines(items)
        print("Item added")

    # Show items in the to do list
    elif "show" in user_input:
        with open("to-do.txt", "r") as file:
            items = file.readlines()
        # new_items = [item.strip("\n") for item in items]
        for i, item in enumerate(items):
            item = item.strip("\n")
            print(f"{i+1}: {item}")

    # Mark an item as complete, removes from to do list
    elif user_input.startswith("complete"):
        try:
            with open("to-do.txt", "r") as file:
                items = file.readlines()
            cmp_item = int(user_input[9:]) - 1
            todo_completed = items[cmp_item].strip("\n")
            items.pop(cmp_item)
            with open("to-do.txt", "w") as file:
                file.writelines(items)
            print(f"Item {todo_completed} removed from list.")
        except ValueError:
            print(inv_cmd)
            continue

    # Edit an existing item in the to do list
    elif user_input.startswith("edit"):
        try:
            with open("to-do.txt", "r") as file:
                items = file.readlines()
            edit_num = int(user_input[5:])
            edit_num = int(edit_num)
            if edit_num < 1 or edit_num > len(items):
                print("Invalid Index")
            else:
                edit_item = input("Edit the item: ")
                items[edit_num-1] = edit_item + '\n'
            with open("to-do.txt", "w") as file:
                file.writelines(items)
            print("Item edited")
        except ValueError:
            print(inv_cmd)
            continue

    # Exit the application
    elif user_input == "exit":
        print("Exiting!")
        break

    else:
        print(inv_cmd)