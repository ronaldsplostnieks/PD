class Shop:
    def __init__(self, pname='prece', skaits = 0, gtips ='detaļa', cena=0, cipars='0'):
        self.productname = pname
        self.amount = skaits
        self.tips = gtips
        self.price = cena
        self.number = cipars

    def printShop(self):
        print(self.number,'. ', self.productname,', ',"Skaits: ", self.amount,", ", self.tips, ", Cena: ", self.price ,sep='')

    def buyProduct(self, daudzums):
        if self.amount >= daudzums:
            self.amount -= daudzums
        else:
            self.amount = 0

    def delivery(self, daudzums): #Produktu piegāde
        self.amount += daudzums
  
class Computer(Shop):
    def __init__(self, skaits, gtips, cena, cipars, razotajs):
        super().__init__("Dators", skaits, gtips, cena, cipars)
        self.manufacture = razotajs

    def printComputer(self):
        print(self.number,'. ', self.manufacture," " , self.productname,', ',"Skaits: ", self.amount,", ", self.tips, ", Cena: ", self.price,sep='')

# x = Shop("detaļa", 10, "programmatūra", 1.99, 0)
# x.printShop()
# x = Computer(10, "programmatūra", 1.99, 0, "HyperX")
# x.printComputer()
