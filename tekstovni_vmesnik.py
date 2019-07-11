import model
VRSTICE = 6
IG = 3
RAC = -1 

def izpis_igre(igra):
    tekst = ""
    for vrstica in range(VRSTICE):
        tekst += "{}\n".format(igra.tabela[vrstica])
    return tekst

def izpis_zmage(igra):
    return "Zmagali ste"

def izpis_poraza(igra):
    return "Izgubili ste!"

def zahtevaj_vnos():
    vnos = input("izberite stolpec: ")
    return int(vnos) - 1

def preveri_vnos(vnos):
    if not len(vnos) == 1:
        print("Neveljaven vnos, vnesite le eno crko")
        return False
    else:
        return True


# Izvajanje vmesnika
def zazeni_vmesnik():
    igra = model.Igra()
    while True:
        print(izpis_igre(igra))
        # ugiba
        poskus = zahtevaj_vnos()
        igra.poteza(poskus)
        # prverimo, ce je igre konec
        if igra.zmaga() == RAC:
            return print(izpis_poraza(igra))
        elif igra.zmaga() == IG:
            return print(izpis_zmage(igra))
    return 

print(zazeni_vmesnik())