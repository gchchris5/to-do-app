import FreeSimpleGUI as sg

label = sg.Text("Type in an item")
input_box = sg.InputText(tooltip="Enter item")
add_button = sg.Button("Add")

layout = [[label], [input_box, add_button]]
window = sg.Window("To-do App", layout=layout)
window.read()
window.close()

