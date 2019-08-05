import copy
import random

#Nujno mora biti vsaj en od STOLPCI ali VRSTICE sod. 
STOLPCI = 7
VRSTICE = 6
PRAZNO = 0
IG = 3
RAC = -1
VEKTORJI = {(0, 1), (1, 1), (1, 0), (1, -1)} # Y SMER JE RAVNO OBRATNA
ZAČETEK = "zmaga"
REMI = "remi"
NAPAKA = "napaka"


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
        remi_test = True
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if self.tabela[vrstica][stolpec] == PRAZNO:
                    remi_test = False
                if self.stiri_okolica(vrstica, stolpec) == IG:
                    return IG
                elif self.stiri_okolica(vrstica, stolpec) == RAC:
                    return RAC
        if remi_test:
            return REMI
        else:
            return PRAZNO
    
    def poteza(self, stolpec): #igralca
        if self.igralec == RAC:
            self.tabela[VRSTICE - 1][(STOLPCI - 1) // 2] = RAC
            self.igralec = IG
        prostor_test = True
        for vrstica in range(VRSTICE - 1, -1, -1):
            if self.tabela[vrstica][stolpec] == PRAZNO:
                self.tabela[vrstica][stolpec] = IG
                prostor_test = False
                break
        if prostor_test:
            return NAPAKA
        rezultat = self.zmaga()
        if rezultat == IG or rezultat == REMI:
            return rezultat
        else:
            self.poteza_racunalnik()
            return self.zmaga()
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

def nova_igra():
    return Igra()




class Stiri_v_vrsto:

    def __init__(self):
        # V slovarju igre ima vsaka igra svoj celoštevilski id.
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            # Preverimo za n+1 stevil izmed n iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
    
    def nova_igra(self):
        # Naredi novo igro in shrani v slovar z novim ID, shrani (začetek, igra)
        igra = nova_igra()
        nov_id = self.prost_id_igre()
        self.igre[nov_id] = (igra, ZAČETEK)
        return nov_id

    def poteza(self, id_igre, stolpec):
        (igra, _) = self.igre[id_igre]
        poteza = igra.poteza(stolpec)
        self.igre[id_igre] = (igra, poteza)

