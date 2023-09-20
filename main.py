from shop import *
import PySimpleGUI as sg

sg.theme('GreenTan')
font = ("Arial", 12)

# All the stuff inside your window.
layout = [  [sg.Text('Produkta nosaukums', size=(15,1)), sg.InputText(key='-PNAME-', do_not_clear=False)],
            [sg.Text('Skaits', size=(15,1)), sg.InputText(key='-AMOUNT-', do_not_clear=False)],
            [sg.Text('Produkta tips (detala vai programma radioswitch)', size=(15,1)), sg.InputText(key='-TYPE-', do_not_clear=False)],
            [sg.Text('Cena', size=(15,1)), sg.InputText(key='-PRICE-', do_not_clear=False)],
            [sg.Text('Numurs', size=(15,1)), sg.InputText(key='-NUMBER-', do_not_clear=False)],
            [sg.Text("Produkti")],
            [sg.Output(size=(5,5), font=font, expand_x=True, expand_y=True,  key = 'outputt')],
            [sg.Button('Pievienot cilvēku'), sg.Button('Dzimsanas diena!'), sg.Button('Mainīt vārdu'), sg.Button('Mainīt dzimumu'), sg.Button('Beigt')]]

window = sg.Window('Window Title', layout) #create window

cilveki = []
while True:
    event, values = window.read()

    # Problema ir mainit datus nevis padot. Jaizdoma veids ka padot un lai atnak atpakal. Vai partaisit lai arrays veidojas otra dokumenta

    if event == sg.WIN_CLOSED or event == 'Beigt':
        break
    elif event == 'Pievienot cilvēku':
        window.FindElement('outputt').Update('')
        cilveki.append(Human(values["-NAME-"], values['-AGE-'], values['-GENDER-'], values['-NUMBER-']))
    elif event == 'Dzimsanas diena!':
        cilveki[int(values['-NUMBER-'])].svinetDzD()
        window.FindElement('outputt').Update('')
    elif event == 'Mainīt vārdu':
        cilveki[int(values['-NUMBER-'])].changeName(values["-NAME-"])
        window.FindElement('outputt').Update('')
    elif event == 'Mainīt dzimumu':
        cilveki[int(values['-NUMBER-'])].changeSex(values['-GENDER-'])
        window.FindElement('outputt').Update('')

    for i in range(len(cilveki)):
        cilveki[i].printArray()    
    
window.close()


