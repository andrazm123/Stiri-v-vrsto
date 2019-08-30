import copy
import random
import json


# "Spremeljive" količine, a z omejitvami.
STOLPCI = 7
VRSTICE = 6

# Nujno morajo biti nizi.
PRAZNO = "Prazno"
IG = "Igralec"
RAC = "Racunalnik"
ZAČETEK = "Začetek"
REMI = "Remi"
NAPAKA = "Napaka"
TEZKO = "Tezko"
LAHKO = "Lahko"
DVA_IGRALCA_1 = "Dva_igralca_1"
DVA_IGRALCA_2 = "Dva_igralca_2"


#Nujno mora biti vsaj en od STOLPCI ali VRSTICE sod, drugace ni pošteno.
if not STOLPCI * VRSTICE % 2 == 0 or STOLPCI < 4 or VRSTICE < 4:
    assert False, "Napačne dimenzije tabele!"
#Spodnje kolicine morajo biti nizi, saj drugace bottle sprozi error.
if not(isinstance(IG, str) == isinstance(RAC, str) == isinstance(LAHKO, str) == isinstance(TEZKO, str) == isinstance(DVA_IGRALCA_1, str) == isinstance(DVA_IGRALCA_2, str)):
    assert False, "Te količine morajo biti nizi!"


class Igra:

    def __init__(self, tabela=[[PRAZNO for _ in range(STOLPCI)] for _ in range(VRSTICE)], tezavnost=TEZKO, igralec=IG):
        self.igralec = igralec
        self.tezavnost = tezavnost
        self.tabela = tabela
        if self.igralec == RAC:
            self.tabela[VRSTICE - 1][(STOLPCI - 1) // 2] = RAC
            self.igralec = IG


    # TEST ZMAGE AND RACUN POTENCJALA
    def stiri_okolica(self, vrstica, stolpec):
        baza = self.tabela[vrstica][stolpec]
        if not baza == PRAZNO:
            for vektor in {(0, 1), (1, 1), (1, 0), (1, -1)}:
                x, y = vektor
                if 0 <= vrstica + 3 * y < VRSTICE and  0 <= stolpec + 3 * x < STOLPCI:
                    if baza == self.tabela[vrstica + y][stolpec + x] == self.tabela[vrstica + 2 * y][stolpec + 2 * x] == self.tabela[vrstica + 3 * y][stolpec + 3 * x]:
                        return baza
        else:
            return PRAZNO
    

    # POMOŽNI, KER SODELUJETA TUDI PRI SPLOŠNIH TABELAH NISTA V CLASSU.
    @staticmethod
    def mogoca_poteza(tabela, stolpec):
        return tabela[0][stolpec] == PRAZNO
    

    @staticmethod
    def poteza_na_stolpec(igralec, tabela, stolpec):
        for vrstica in range(VRSTICE - 1, -1, -1):
            if tabela[vrstica][stolpec] == PRAZNO:
                tabela[vrstica][stolpec] = igralec
                return tabela


    # POTEZA RACUNALNIKA    
    def zapri_zakljuci(self):
        baza = set()
        shramba = copy.deepcopy(self.tabela)
        for stolpec in range(STOLPCI):
            tabela = copy.deepcopy(shramba)
            if Igra.mogoca_poteza(tabela, stolpec):
                self.tabela = Igra.poteza_na_stolpec(RAC, tabela, stolpec)
                if self.zmaga() == RAC:
                    baza.add((RAC, stolpec))
                tabela = copy.deepcopy(shramba)
                self.tabela = Igra.poteza_na_stolpec(IG, tabela, stolpec)
                if self.zmaga() == IG:
                    baza.add((IG, stolpec))
        self.tabela = copy.deepcopy(shramba)
        return baza
    

    # TEST ZMAGE
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
    

    # POTEZA RACUNALNIKA   
    def pametna_poteza(self, stolpec):
        shramba = copy.deepcopy(self.tabela)
        self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
        if not Igra.mogoca_poteza(self.tabela, stolpec):
            self.tabela = copy.deepcopy(shramba)
            return True
        else:
            self.tabela = Igra.poteza_na_stolpec(IG, self.tabela, stolpec)
            if self.zmaga() == IG:
                self.tabela = copy.deepcopy(shramba)
                return False
            else:
                self.tabela = copy.deepcopy(shramba)
                return True


    # POTEZA RACUNALNIKA
    def potencjali(self):
        baza = set()
        shramba = copy.deepcopy(self.tabela)
        for stolpec1 in range(STOLPCI):
            tabela1 = copy.deepcopy(shramba)
            if Igra.mogoca_poteza(tabela1, stolpec1):
                tabela1 = Igra.poteza_na_stolpec(RAC, tabela1, stolpec1)
                for stolpec2 in range(STOLPCI):
                    tabela2 = copy.deepcopy(tabela1)
                    if Igra.mogoca_poteza(tabela2, stolpec2):
                        self.tabela = Igra.poteza_na_stolpec(RAC, tabela2, stolpec2)
                        if self.zmaga() == RAC:
                            baza.add(stolpec1)
        self.tabela = copy.deepcopy(shramba)
        return baza


    # POTEZA RACUNALNIKA
    def poteza_racunalnik_del1(self):
        #STOPNJA NUJNOSTI 1
        izbire1 = self.zapri_zakljuci()
        if izbire1 == set():
            return "nic"
        for izb in izbire1:
            if izb[0] == RAC:
                stolpec = izb[1]
                self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
                return "konec"
        for izb in izbire1:
            if izb[0] == IG:
                stolpec = izb[1]
                self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
                return "konec"


    # POTEZA RACUNALNIKA
    def poteza_racunalnik_del2(self):
        #STOPNJA NUJNOSTI 2
        izbire2 = []
        for stolpec in range(STOLPCI):
            for vrstica in range(VRSTICE):
                if self.tabela[vrstica][stolpec] != PRAZNO:
                    izbire2.append(stolpec)
        if len(izbire2) == 1:
            stolpec = izbire2[0]
            if stolpec == 0:
                self.tabela[VRSTICE - 1][3] = RAC
                return "konec"
            elif stolpec == STOLPCI - 1:
                self.tabela[VRSTICE - 1][STOLPCI - 4] = RAC
                return "konec"
            elif stolpec <= STOLPCI // 2:
                self.tabela[VRSTICE - 1][stolpec + 1] = RAC
                return "konec"
            elif stolpec > STOLPCI // 2:
                self.tabela[VRSTICE - 1][stolpec - 1] = RAC
                return "konec"
            else:
                assert False, "Do sem se nebi smelo dati priti."
        #STOPNJA NUJNOSTI 3
        izbire3 = self.potencjali()
        if not izbire3 == set():
            stolpec = random.sample(izbire3, 1)[0]
            if self.pametna_poteza(stolpec):
                self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
                return "konec"
        return "nic"


    # POTEZA RACUNALNIKA
    def poteza_racunalnik_del3(self):
        #STOPNJA NUJNOSTI 4
        izbire4 = set()
        izbire5 = set()
        for stolpec in range(STOLPCI):
            if Igra.mogoca_poteza(self.tabela, stolpec):
                izbire5.add(stolpec)
                if self.pametna_poteza(stolpec):
                    izbire4.add(stolpec)
        if not izbire4 == set():
            stolpec = random.sample(izbire4, 1)[0]
            self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
            return "konec"
        #STOPNJA NUJNOSTI 5
        else:
            stolpec = random.sample(izbire5, 1)[0]
            self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
            return "konec"
    
    
    # POTEZA RACUNALNIKA
    def poteza_racunalnik(self):
        if self.tezavnost == TEZKO:
            test = self.poteza_racunalnik_del1()
            if test == "nic":
                test = self.poteza_racunalnik_del2()
                if test == "nic":
                    test = self.poteza_racunalnik_del3()
        elif self.tezavnost == LAHKO:
            test = self.poteza_racunalnik_del1()
            if test == "nic":
                test = self.poteza_racunalnik_del3()
        else:
            assert False, "Do sem se nebi smelo dati priti."


    # POTEZA IGRALCA
    def poteza_en_igralec(self, stolpec): 
        tabela = copy.deepcopy(self.tabela)
        if not Igra.mogoca_poteza(tabela, stolpec):
            return NAPAKA
        else:
            self.tabela = Igra.poteza_na_stolpec(IG, self.tabela, stolpec)
            rezultat = self.zmaga()
            if rezultat == IG or rezultat == REMI:
                return rezultat
            else:
                self.poteza_racunalnik()
                return self.zmaga()


    # POTEZA IGRALCA
    def poteza_dva_igralca(self, stolpec):
        if self.igralec == DVA_IGRALCA_1:
            tabela = copy.deepcopy(self.tabela)
            if not Igra.mogoca_poteza(tabela, stolpec):
                return NAPAKA
            else:
                self.tabela = Igra.poteza_na_stolpec(IG, self.tabela, stolpec)
                rezultat = self.zmaga()
                self.igralec = DVA_IGRALCA_2
                if rezultat == IG or rezultat == REMI:
                    return rezultat
        elif self.igralec == DVA_IGRALCA_2:
            tabela = copy.deepcopy(self.tabela)
            if not Igra.mogoca_poteza(tabela, stolpec):
                return NAPAKA
            else:
                self.tabela = Igra.poteza_na_stolpec(RAC, self.tabela, stolpec)
                rezultat = self.zmaga()
                self.igralec = DVA_IGRALCA_1
                if rezultat == RAC or rezultat == REMI:
                    return rezultat
        else:
            assert False, "Do sem se nebi smelo dati priti."


    # POTEZA IGRALCA
    def poteza(self, stolpec):
        if self.igralec == DVA_IGRALCA_1 or self.igralec == DVA_IGRALCA_2:
            return self.poteza_dva_igralca(stolpec)
        else:
            return self.poteza_en_igralec(stolpec)





class Stiri_v_vrsto:

    def __init__(self, datoteka_s_stanjem):
        # V slovarju igre ima vsaka igra svoj celoštevilski id.
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.igre = {}
        

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            # Preverimo za n+1 stevil izmed n iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
    

    def nova_igra(self, igralec=IG, tezavnost=TEZKO):
        # Naredi novo igro in shrani v slovar z novim ID, shrani (začetek, igra)
        self.nalozi_igre_iz_datoteke()
        igra = Igra(igralec=igralec, tezavnost=tezavnost)
        nov_id = self.prost_id_igre()
        self.igre[nov_id] = (igra, ZAČETEK)
        self.zapisi_igre_v_datoteko()
        return nov_id


    def poteza(self, id_igre, stolpec):
        self.nalozi_igre_iz_datoteke()
        (igra, _) = self.igre[id_igre]
        poteza = igra.poteza(stolpec)
        self.igre[id_igre] = (igra, poteza)
        self.zapisi_igre_v_datoteko()
        return


    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as datoteka:
            zakodirane_igre = json.load(datoteka) #Dobimo slovar z (geslom, crke)
            igre = {}
            for id_igre in zakodirane_igre:
                igra = zakodirane_igre[id_igre]
                igre[int(id_igre)] = (Igra(tabela=igra["tabela"], igralec=igra["igralec"], tezavnost=igra["tezavnost"]), igra["poteza"])
            self.igre = igre
        return


    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, "w") as datoteka:
            zakodirane_igre = {}
            for id_igre in self.igre:
                (igra, poteza) = self.igre[id_igre]
                zakodirane_igre[id_igre] = {"igralec": igra.igralec, "tezavnost": igra.tezavnost, "tabela": igra.tabela, "poteza": poteza}
            json.dump(zakodirane_igre, datoteka)
        return





