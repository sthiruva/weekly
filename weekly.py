import bottle
import datetime

bottle.debug(True)

@bottle.route('/weekly/:uname')
def weekly(uname):
    return bottle.template('index')

@bottle.route('/weekly/:uname/addpc')
def addpc(uname):
    return uname


@bottle.route('/css/:filename')
def server_static(filename):
    return bottle.static_file(filename, root='css/')

@bottle.route('/js/:filename')
def server_static(filename):
    return bottle.static_file(filename, root='js/')

@bottle.route('/fonts/:filename')
def server_static(filename):
    return bottle.static_file(filename, root='fonts/')

bottle.run(host='localhost', port=8080)
