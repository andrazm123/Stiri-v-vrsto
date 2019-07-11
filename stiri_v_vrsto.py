import bottle, model


@bottle.get('/')
def prva_stran():
    return bottle.template('views/index.tpl')




bottle.run(debug=True, reloder=True)