import bottle, model

stiri_v_vrsto = model.Stiri_v_vrsto("stanje.json")
SKRIVNI_KLJUC = "bravo, uganil si kluc"


#ZAČETNA STRAN
@bottle.get('/')
def prva_stran():
    return bottle.template('views/index.tpl')


#RESET
@bottle.post('/')
def reset():
    bottle.redirect('/')
    return


#GUMB-NOVA IGRA
@bottle.post('/nova_igra/<igralec>/<tezavnost>')
def zacni_novo_igro_prvi(igralec, tezavnost):
    #POST naredi novo igro, reusmeri na naslov za igranje te nove igre
    if igralec == model.IG and tezavnost == model.LAHKO:
        id_igre = stiri_v_vrsto.nova_igra(igralec=model.IG, tezavnost=model.LAHKO)
    elif igralec == model.IG and tezavnost == model.TEZKO:
        id_igre = stiri_v_vrsto.nova_igra(igralec=model.IG, tezavnost=model.TEZKO)
    elif igralec == model.RAC and tezavnost == model.LAHKO:
        id_igre = stiri_v_vrsto.nova_igra(igralec=model.RAC, tezavnost=model.LAHKO)
    elif igralec == model.RAC and tezavnost == model.TEZKO:
        id_igre = stiri_v_vrsto.nova_igra(igralec=model.RAC, tezavnost=model.TEZKO)
    elif igralec == model.DVA_IGRALCA_1 and tezavnost == model.TEZKO:
        id_igre = stiri_v_vrsto.nova_igra(igralec=model.DVA_IGRALCA_1, tezavnost=model.TEZKO)
    else:
        assert False, "Do sem se nebi smelo dati priti."
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNI_KLJUC, path="/")
    bottle.redirect('/igra/')
    return


#IGRA SAMA
#Moramo preusmeruti na GET ker bi drugače ob osvežitvi vse izgubili
@bottle.get('/igra/')
def prikazi_igro():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    (igra, poteza) = stiri_v_vrsto.igre[id_igre]
    return bottle.template('views/igra.tpl', igra=igra, id_igre=id_igre, poteza=poteza)


#GUMBI ZA UGIBATI
@bottle.post("/ugibaj/<n:int>")
def ugibaj(n):
    stolpec = n
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    stiri_v_vrsto.poteza(id_igre, stolpec)
    bottle.redirect('/igra/')
    return


#SKLIKE
@bottle.get("/static/<filename>")
def server_static(filename):
    return bottle.static_file(filename, root="./images")


bottle.run(reloader=True, debug=True)