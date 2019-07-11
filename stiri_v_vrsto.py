import bottle, model

stiri_v_vrsto = model.Stiri_v_vrsto()
SKRIVNI_KLJUC = "bravo, uganil si kluc"

@bottle.get('/')
def prva_stran():
    return bottle.template('views/index.tpl')

@bottle.post('/nova_igra/')
def zacni_novo_igro():
    # POST naredi novo igro, reusmeri na naslov za igranje te nove igre
    id_igre = stiri_v_vrsto.nova_igra()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNI_KLJUC, path="/")
    bottle.redirect('/igra/')
    return

#Moramo preusmeruti na GET ker bi drugače ob osvežitvi vse izgubili
@bottle.get('/igra/')
def prikazi_igro():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    (igra, poteza) = stiri_v_vrsto.igre[id_igre]
    return bottle.template('views/igre.tpl', igra=igra, id_igre=id_igre, poteza=poteza)

#Če imaš post metodo VEDNO nato redirectaj na GET
@bottle.post('/igra/')
def ugibaj_crko():
    stolpec = bottle.request.forms.getunicode("poskus")
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    stiri_v_vrsto.poteza(id_igre, stolpec)
    bottle.redirect('/igra/')


bottle.run(debug=True, reloder=True)