#nacteni modulu ceil z math - pro zaokrouhlovani
from math import ceil
#trida Locality - kde se nemovitost nachazi
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient
#trida Property - nemovitost
class Property:
    def __init__(self, locality):
        self.locality = locality
#trida Estate - pozemek dedici od property
class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    #vypocet vyse dane pro pozemek, cele cislo
    def calculate_tax(self):
        if self.estate_type == "land":
            coefficient = 0.85
        elif self.estate_type == "building site":
            coefficient = 9
        elif self.estate_type == "forrest":
            coefficient = 0.35
        elif self.estate_type == "garden":
            coefficient = 2
        #vrati zaokrouhlene cislo
        return ceil(self.area * coefficient * self.locality.locality_coefficient)
#trida Residence - byt/dum/stavba, dedici od property
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    #vypocet dane pro residenci
    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            tax = tax * 2
        return ceil(tax)

#lokalita Manetin, koef 0.8
manetin = Locality("Manětín", 0.8)
#lokalita Brno, koef 3
brno = Locality("Brno", 3)

#priklady
zemedelsky_pozemek = Estate(manetin, "land", 900) #vratilo 612
dum = Residence(manetin, 120, False) #vratilo 1440
kancelar = Residence(brno, 90, True) #vratilo 8100

print(zemedelsky_pozemek.calculate_tax())
print(dum.calculate_tax())
print(kancelar.calculate_tax())
