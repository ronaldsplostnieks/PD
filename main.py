from shop import *
import PySimpleGUI as sg

sg.theme('DarkAmber') # Aplikacijas izskats
font = ("Arial", 12) # fonts lai informcijas OUTPUTS skaidrāks

layout = [  [sg.Text('Produkta nosaukums', size=(15,1)), sg.InputText(key='-PNAME-', do_not_clear=False)],
            [sg.Radio("Detaļa", "tips",key='-DETALA-', default=True), sg.Radio("Programmatūra", "tips",key='-PROGRAMMATURA-')],
            [sg.Text('Skaits', size=(15,1)), sg.InputText(key='-AMOUNT-', do_not_clear=False)],
            [sg.Text('Cena', size=(15,1)), sg.InputText(key='-PRICE-', do_not_clear=False)],
            [sg.Text('Numurs', size=(15,1)), sg.InputText(key='-NUMBER-', do_not_clear=False)],
            [sg.Text("Produkti")],
            [sg.Output(size=(5,5), font=font, expand_x=True, expand_y=True,  key = 'outputt')],
            [sg.Button('Pievienot produktu'), sg.Button('Produktu piegāde'), sg.Button('Pārdot'), sg.Button('Rediģēt datus'), sg.Button('Beigt')]]

window = sg.Window('Window Title', layout) # Izveido window

products = []
money = 0
while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED or event == 'Beigt':
        break
    elif event == 'Pievienot produktu':
        window.FindElement('outputt').Update('')
        if values["-PNAME-"].lower() == 'dators':
            text = sg.popup_get_text('Datora ražotājs', title="Manufacturer")
            if values['-DETALA-']:
                products.append(Computer(int(values['-AMOUNT-']), 'detala', float(values['-PRICE-']), values['-NUMBER-'], text))
            else:
                products.append(Computer(int(values['-AMOUNT-']), 'programmatura', float(values['-PRICE-']), values['-NUMBER-'], text))
        else:
            if values['-DETALA-']:
                products.append(Shop(values["-PNAME-"], int(values['-AMOUNT-']), 'detala', float(values['-PRICE-']), values['-NUMBER-']))
            else:
                products.append(Shop(values["-PNAME-"], int(values['-AMOUNT-']), 'programmatura', float(values['-PRICE-']), values['-NUMBER-']))
    elif event == 'Produktu piegāde':
        window.FindElement('outputt').Update('')
        products[int(values['-NUMBER-'])].shopDelivery(int(values['-AMOUNT-']))
    elif event == 'Pārdot':
        window.FindElement('outputt').Update('')
        amount, price = products[int(values['-NUMBER-'])].getAmountPrice()
        if amount >= int(values['-AMOUNT-']):
            money += float(values['-AMOUNT-']) * float(price)
        else:
            money += float(amount) * float(price)
        products[int(values['-NUMBER-'])].buyProduct(int(values['-AMOUNT-']))
    elif event == 'Rediģēt datus':
        window.FindElement('outputt').Update('')
        if values["-PNAME-"].lower() != '':
            products[int(values['-NUMBER-'])].changeName(values["-PNAME-"])
        if values['-AMOUNT-'] != '':
            products[int(values['-NUMBER-'])].changeAmount(int(values['-AMOUNT-']))
        if values['-DETALA-']:
            products[int(values['-NUMBER-'])].changeType('detala')
        else:
            products[int(values['-NUMBER-'])].changeType('programmatura')
        if values['-PRICE-'] != '':
            products[int(values['-NUMBER-'])].changePrice(float(values['-PRICE-']))

    for i in range(len(products)):
        products[i].printShop() 
    print('Money earned:', money)
window.close()