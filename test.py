import PySimpleGUI as sg

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

try:
    while True:             # Event Loop
        event, values = window.read()
        window.bad()
        print(event, values)
        if event in (None, 'Exit'):
            break
        if event == 'Go':
            window['-OUT-'].update(values['-IN-'])
    window.close()
except Exception as e:
    sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)