import model
VRSTICE = 6

def izpis_igre(igra):
    tekst = ""
    for vrstica in range(VRSTICE):
        tekst += "{vrstica}\n".format(igra.tabela[vrstica])
    return tekst

def izpis_zmage(igra):
    return "Zmagali ste"

def izpis_poraza(igra):
    return "Izgubili ste!"

def zahtevaj_vnos():
    vnos = input("izberite stolpec: ")
    return vnos

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
        if not preveri_vnos(poskus):
            continue
        igra.ugibaj(poskus)
        # prverimo, ce je igre konec
        if igra.poraz():
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return 