import FreeSimpleGUI as sg

label = sg.Text("Type in an item")
input_box = sg.InputText(tooltip="Enter item")

layout = [label, input_box]
window = sg.Window("To-do App", layout=[layout])
window.read()
window.close()

