import FreeSimpleGUI as sg
import functions
import time

sg.theme("LightGrey")
clock_label = sg.Text("", key="clock")
title_label = sg.Text("Manage Your To-do List")
input_box = sg.InputText(tooltip="Enter item", key="new_item")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=functions.get_items(), key="list_item",
                      enable_events=True, size=(45, 10))
layout = [[title_label],
          [clock_label],
          [input_box, add_button],
          [edit_button, complete_button],
          [list_box],
          [exit_button]]
window = sg.Window(title="To-do App",
                   layout=layout,
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A, %B %d, %Y %I:%M:%S %p"))
    if event == "Add":
        items = functions.get_items()
        if len(values["new_item"]) > 0:
            new_item = values["new_item"] + "\n"
            items.append(new_item.capitalize())
            functions.write_items(items_in=items)
            window["list_item"].update(values=items)
            window["new_item"].update(value="")
        else:
            message = "No item entered to add."
            sg.popup(message, font=("Helvetica", 20))
    elif event == "Edit":
        try:
            item_edit = values["list_item"][0]
            new_item = values["new_item"] + "\n"
            items = functions.get_items()
            index = items.index(item_edit)
            items[index] = new_item.capitalize()
            functions.write_items(items)
            window["list_item"].update(values=items)
            window["new_item"].update(value="")
        except IndexError as e:
            message = "An item must be selected to edit."
            sg.popup(message, font=("Helvetica", 20))
    elif event == "list_item":
        window["new_item"].update(value=values["list_item"][0].strip("\n"))
    elif event == "Complete":
        try:
            item_complete = values["list_item"][0]
            items = functions.get_items()
            index = items.index(item_complete)
            items.pop(index)
            functions.write_items(items_in=items)
            window["list_item"].update(values=items)
            window["new_item"].update(value="")
        except IndexError as e:
            message = "An item must be selected to complete."
            sg.popup(message, font=("Helvetica", 20))
    elif event == "Exit" or sg.WIN_CLOSED:
        break

window.close()

