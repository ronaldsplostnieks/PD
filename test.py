import PySimpleGUI as sg

items = [
    "Automobile", "Chemical", "Engineering/Consulting", "FMCG",
    "Healthcare/Hospitality", "Infrastructue", "IT/Comm/DC", "Manufacturing",
    "Mines", "Energy/Oil & Gas", "Pharma", "Retail", "Cement",
]
length = len(items)
size = (max(map(len, items)), 1)

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 11))

column_layout = []
line = []
num = 4
for i, item in enumerate(items):
    line.append(sg.Button(item, size=size, metadata=False))
    if i%num == num-1 or i==length-1:
        column_layout.append(line)
        line = []

layout = [
    [sg.Text('Choose the Industry')],
    [sg.Column(column_layout)],
    [sg.Text(size=(50,1),key=('loaded'))],
    [sg.Text('Enter Observation/Recommendation: ', size =(26, 1)), sg.InputText()],
    [sg.Button("Predict Risk", bind_return_key=True)],
    [sg.Text(size=(30,1),key=('output'))],
    [sg.Text('If the above prediction is correct select \'yes\' else select the correct risk.')],
    [sg.Button("Yes"),sg.Button("Low"),sg.Button("Medium")],
    [sg.Text(size=(30,2),key=('trained'))],
    [sg.Button("Exit"),sg.Button("Clear Fields")]
]

window=sg.Window("Risk Predictor", layout, use_default_focus=False, finalize=True)
for key in window.key_dict:    # Remove dash box of all Buttons
    element = window[key]
    if isinstance(element, sg.Button):
        element.block_focus()

while True:

    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event in items:
        window[event].metadata = True
    elif event == "Predict Risk" and window["Mines"].metadata:
        print("Predict Risk for Mines")

window.close()