class Human:
    def __init__(self, vards, vecums, dzimums, cipars='0'):
        self.name = vards
        self.age = vecums
        self.sex = dzimums
        self.number = cipars
        # self.info()


    def svinetDzD(self):
        self.age = int(self.age) + 1


    def changeName(self, newWord):
        self.name = newWord
        self.info()

    def changeSex(self, newSex = ""):
        if newSex == "":
            if self.sex == "s":
                self.sex = "m"
            else:
                self.sex = "s"
        else:
            self.sex = newSex 
        self.info()


    def info(self):
        print("Sveiki mani sauc", self.name, "Mani ir", self.age, "gadi")
        if self.sex == "m":
            print("Es esmu vīrietis")
        elif self.sex == "f":
            print("Es esmu sieviete")
        else:
            print("Es esmu", self.sex)

    def infoDead(self):
        if self.sex == "m":
            print("Sveiki, mani sauca", self.name, "Man bija", self.age, "gadi un es biju vīrietis")
        elif self.sex == "f":
            print("Sveiki, mani sauca", self.name, "Man bija", self.age, "gadi un es biju sieviete")
        else:
            print("Sveiki, mani sauca", self.name, "Man bija", self.age, "gadi un es biju", self.sex)

    # def __del__(self): #kas papiluds jaizdara pirms objektu iznicina, izmantojot del
    #     print("atā...")

    def printArray(self):
        print(self.number,'. ', self.name,', ', self.age,", ", self.sex,sep='')

# Mantošana
class Woman(Human):
    def __init__(self, name, age, matuKrasa):
        Human.__init__(self, name, age, "f")
        self.hairColor = matuKrasa
        self.info()

    def info(self):
        super().info()
        print("Mana matu krāsa ir", self.hairColor)


pirmais = Woman("Anna", 21, "blondi")
print(pirmais)
