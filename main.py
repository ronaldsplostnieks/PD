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

    for i in range(len(products)):
        check = products[i].getPName(values['-ENAME-'])
        print(check) 
        if check == 'yes':
            num = i

    if event == sg.WIN_CLOSED or event == 'Beigt':
        break
    elif event == 'Pievienot produktu':
        window.FindElement('outputt').Update('')
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
        products[int(values[num])].shopDelivery(int(values['-AMOUNT-']))
    elif event == 'Pārdot':
        window.FindElement('outputt').Update('')
        amount, price = products[int(values[num])].getAmountPrice()
        if amount >= int(values['-AMOUNT-']):
            money += float(values['-AMOUNT-']) * float(price)
        else:
            money += float(amount) * float(price)
        products[int(values[num])].buyProduct(int(values['-AMOUNT-']))
    elif event == 'Rediģēt datus':
        window.FindElement('outputt').Update('')
        if values["-PNAME-"].lower() != '':
            products[int(values[num])].changeName(values["-PNAME-"])
        if values['-AMOUNT-'] != '':
            products[int(values[num])].changeAmount(int(values['-AMOUNT-']))
        if values['-DETALA-']:
            products[int(values[num])].changeType('detala')
        else:
            products[int(values[num])].changeType('programmatura')
        if values['-PRICE-'] != '':
            products[int(values[num])].changePrice(float(values['-PRICE-']))

    for i in range(len(products)):
        products[i].printShop(i) 
    print('Money earned:', round(money, 2))
window.close()