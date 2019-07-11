import copy
import random

STOLPCI = 7
VRSTICE = 6
PRAZNO = 0
IG = 3
RAC = -1
VEKTORJI = {(0, 1), (1, 1), (1, 0), (1, -1)} # Y SMER JE RAVNO OBRATNA


class Igra:

    def __init__(self, igralec=IG):
        self.igralec = igralec
        self.tabela = [[PRAZNO for _ in range(STOLPCI)] for _ in range(VRSTICE)]

    def potencjali_dve_potezi(self):
        potencjali = []
        for stolpec1 in range(STOLPCI):
            test_tabela1 = copy.deepcopy(self.tabela)
            for vrstica1 in range(VRSTICE - 1, -1, -1):
                if test_tabela1[vrstica1][stolpec1] == PRAZNO:
                    test_tabela1[vrstica1][stolpec1] = RAC
                    break
            for stolpec2 in range(STOLPCI):
                test_tabela2 = copy.deepcopy(test_tabela1)
                for vrstica2 in range(VRSTICE - 1, -1, -1):
                    if test_tabela2[vrstica2][stolpec2] == PRAZNO:
                        test_tabela2[vrstica2][stolpec2] = RAC
                        potencjali.append((potencjal(test_tabela2), stolpec1, stolpec2))
                        break
        return potencjali

    def poteza_racunalnik(self):
        potencjali = self.potencjali_dve_potezi()
        potencjali.sort(key=lambda x: x[0])
        maxi = potencjali[0][0]
        izbira = [pot[1] for pot in potencjali if pot[0] == maxi]
        stolpec = random.choice(izbira)
        for vrstica in range(VRSTICE - 1, -1, -1):
            if self.tabela[vrstica][stolpec] == PRAZNO:
                self.tabela[vrstica][stolpec] = RAC
                break
    
    def stiri_okolica(self, vrstica, stolpec):
        baza = self.tabela[vrstica][stolpec]
        if not baza == PRAZNO:
            for vektor in VEKTORJI:
                x, y = vektor
                if vrstica + 3 * y < VRSTICE and stolpec + 3 * x < STOLPCI:
                    if baza == self.tabela[vrstica + y][stolpec + x] == self.tabela[vrstica + 2 * y][stolpec + 2 * x] ==self. tabela[vrstica + 3 * y][stolpec + 3 * x]:
                        return baza
            return PRAZNO
        else:
            return PRAZNO
    
    def zmaga(self):
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if self.stiri_okolica(vrstica, stolpec) == IG:
                    return IG
                elif self.stiri_okolica(vrstica, stolpec) == RAC:
                    return RAC
        return PRAZNO
    
    def poteza(self, stolpec):
        if self.igralec == RAC:
            self.tabela[5][3] = RAC
            self.igralec = IG
        for vrstica in range(VRSTICE - 1, -1, -1):
            if self.tabela[vrstica][stolpec] == PRAZNO:
                self.tabela[vrstica][stolpec] = IG
                break
        self.poteza_racunalnik()
        # CE NAREDIS NEMOGOCO POTEZO VRNE ERROR ALI PA SE NE ZGODI NIC.




# OTEŽENO (+1, -1) PREŠTEJE ČE JE POLJE IZHODIŠČE ZA TRI V VRSTO.
def tri_okolica(tabela, stolpec, vrstica):
    baza = tabela[vrstica][stolpec]
    if not baza == PRAZNO:
        vsota = 0
        for vektor in VEKTORJI:
            x, y = vektor
            if vrstica + 3 * y < VRSTICE and stolpec + 3 * x < STOLPCI:
                if baza == tabela[vrstica + y][stolpec + x] == tabela[vrstica + 2 * y][stolpec + 2 * x] == tabela[vrstica + 3 * y][stolpec + 3 * x]:
                    vsota += 1
        return baza * vsota     # Pomembno je da sta IG in RAC ravno 1 in -1.
    else:
        return PRAZNO

# VRNE OTEŽENO VSOTO POLJ IZ TRI_OKOLICA
def potencjal(tabela):
    potencjal = 0
    for vrstica in range(VRSTICE):
        for stolpec in range(STOLPCI):
            potencjal += tri_okolica(tabela, stolpec, vrstica)
    return potencjal

#ig = Igra()
#print(ig.poteza(3))
#print(ig.poteza(2))
#print(ig.poteza(4))
#print(ig.poteza(5))
#print(ig.tabela)