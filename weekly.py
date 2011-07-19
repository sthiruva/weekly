import bottle
import datetime

bottle.debug(True)

@bottle.route('/weekly')
def weekly():
    return bottle.template('index')

@bottle.route('/css/:filename')
def server_static(filename):
    return bottle.static_file(filename, root='css/')


bottle.run(host='blr-lin-484', port=8080)
