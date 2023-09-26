from shop import *
import PySimpleGUI as sg

sg.theme('DarkAmber') # Aplikacijas izskats
font = ("Arial", 12) # fonts lai informcijas OUTPUTS skaidrāks

layout = [  [sg.Text('Produkta nosaukums', size=(19,1)), sg.InputText(key='-PNAME-', do_not_clear=False)],
            [sg.Radio("Detaļa", "tips",key='-DETALA-', default=True), sg.Radio("Programmatūra", "tips",key='-PROGRAMMATURA-')],
            [sg.Text('Skaits', size=(19,1)), sg.InputText(key='-AMOUNT-', do_not_clear=False)],
            [sg.Text('Cena', size=(19,1)), sg.InputText(key='-PRICE-', do_not_clear=False)],
            [sg.Text('Nosaukums (rediģēšanai)', size=(19,1)), sg.InputText(key='-ENAME-', do_not_clear=False)],
            [sg.Text("Produkti")],
            [sg.Output(size=(5,5), font=font, expand_x=True, expand_y=True,  key = 'outputt')],
            [sg.Button('Pievienot produktu'), sg.Button('Produktu piegāde'), sg.Button('Pārdot'), sg.Button('Rediģēt datus'), sg.Button('Beigt')]]

window = sg.Window('Window Title', layout) # Izveido window

products = []
money = 0
while True:
    event, values = window.read()
    window.FindElement('outputt').Update('')

    for i in range(len(products)):
        if values['-ENAME-'] != '':
            check = products[i].getPName(values['-ENAME-'])
            if check == 'yes':
                num = i

    if event == sg.WIN_CLOSED or event == 'Beigt':
        break
    elif event == 'Pievienot produktu':
        if values["-PNAME-"].lower() == 'dators':
            text = sg.popup_get_text('Datora ražotājs', title="Manufacturer")
            if values['-DETALA-']:
                products.append(Computer(int(values['-AMOUNT-']), 'detala', float(values['-PRICE-']), text))
            else:
                products.append(Computer(int(values['-AMOUNT-']), 'programmatura', float(values['-PRICE-']), text))
        else:
            if values['-DETALA-']:
                products.append(Shop(values["-PNAME-"], int(values['-AMOUNT-']), 'detala', float(values['-PRICE-'])))
            else:
                products.append(Shop(values["-PNAME-"], int(values['-AMOUNT-']), 'programmatura', float(values['-PRICE-'])))
    elif event == 'Produktu piegāde':
        window.FindElement('outputt').Update('')
        products[num].shopDelivery(int(values['-AMOUNT-']))
    elif event == 'Pārdot':
        window.FindElement('outputt').Update('')
        amount, price = products[num].getAmountPrice()
        if amount >= int(values['-AMOUNT-']):
            money += float(values['-AMOUNT-']) * float(price)
        else:
            money += float(amount) * float(price)
        products[num].buyProduct(int(values['-AMOUNT-']))
    elif event == 'Rediģēt datus':
        window.FindElement('outputt').Update('')
        if values["-PNAME-"].lower() != '':
            products[num].changeName(values["-PNAME-"])
        if values['-AMOUNT-'] != '':
            products[num].changeAmount(int(values['-AMOUNT-']))
        if values['-DETALA-']:
            products[num].changeType('detala')
        else:
            products[num].changeType('programmatura')
        if values['-PRICE-'] != '':
            products[num].changePrice(float(values['-PRICE-']))

    for i in range(len(products)):
        products[i].printShop(i) 
    print('Money earned:', round(money, 2))
window.close()