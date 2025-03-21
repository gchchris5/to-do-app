import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in an item")
input_box = sg.InputText(tooltip="Enter item", key="item")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

layout = [[label],
          [input_box, add_button],
          [exit_button]]
window = sg.Window(title="To-do App",
                   layout=layout,
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    if event == "Add":
        items = functions.get_items()
        new_item = values["item"] + "\n"
        items.append(new_item)
        functions.write_items(items_in=items)
    elif event == "Exit" or sg.WIN_CLOSED:
        break

window.close()

