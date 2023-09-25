moneySpent = 0.00
class Shop:
    def __init__(self, pname='prece', skaits = 0, gtips ='detaLa', cena=0.0): #Pamata struktūra
        self.productname = pname
        self.amount = skaits
        self.tips = gtips
        self.price = cena

    def printShop(self, numb): # Izprinto informāciju
        print(numb,'. ', self.productname,', ',"Skaits: ", self.amount,", ", self.tips, ", Cena: ", self.price ,sep='') 

    def buyProduct(self, daudzums): # Preces pārdošana, tiek noņemta prece no saraksta. Ja cenšas nopirkt vairāk, kā ir tad automatiski uzsetto uz 0 un pārdod tikai cik ir.
        if self.amount >= daudzums:
            self.amount -= daudzums
        else:
            self.amount = 0

    def shopDelivery(self, daudzums): # Preces piegāde, pievieno produktus
        self.amount += daudzums

    def getAmountPrice(self): # Iegūst preces daudzumu un cenu un agriež to main.py lai izrēķinātu iztērēto naudu 
        return self.amount, self.price
    
    def changeName(self, newName): #Nomaina produkta vārdu
        self.productname = newName

    def changeAmount(self, newAmount): # Nomaina produktu skaitu 
        self.amount = newAmount

    def changeType(self, newType): # Nomaina produkta tipu
        self.tips = newType
    
    def changePrice(self, newPrice): #Nomaina produkta cenu
        self.price = float(newPrice)
    def getPName(self, namee):
        if self.productname == namee:
            return 'yes'


  
class Computer(Shop): # Klase, ja prece ir 'dators'
    def __init__(self, skaits, gtips, cena, razotajs):
        super().__init__("Dators", skaits, gtips, cena)
        self.manufacture = razotajs

    def printShop(self, numb):
        print(numb,'. ', self.manufacture," " , self.productname,', ',"Skaits: ", self.amount,", ", self.tips, ", Cena: ", self.price,sep='')

