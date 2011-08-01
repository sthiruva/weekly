import bottle
import datetime

import pickle
import os

bottle.debug(True)

@bottle.route('/weekly/:uname')
def weekly(uname):
    return bottle.template('index')

@bottle.route('/weekly/:uname/addpc')
def addpc(uname):
    return uname

@bottle.route('/weekly/:uname/addms')
def addms(uname):
    ms = bottle.request.GET.get('ms')

    if os.path.isfile("data/%s/settings.pickle" % uname):
        print "path present load pickle"
    else:
        print "path not present"

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

class Settings:
    def __init__(self):
        self.ms     = dict()
        self.projs  = dict()
        self.notify = dict()
        return


def main():
    bottle.run(host='localhost', port=8080)
    return

main()
