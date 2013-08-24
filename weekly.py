import bottle
import datetime

import pickle
import os
import json

bottle.debug(True)

@bottle.route('/weekly/:uname')
def weekly(uname):

    if os.path.exists("data/%s" %uname) == False:
        os.mkdir("data/%s" % uname)

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

@bottle.route('/weekly/:uname/save_report')
def save_report(uname):
    report_dict_string = bottle.request.GET.get('report_dict_string')

    print "report_dict_string = %s" % report_dict_string

    report_dict = json.loads(report_dict_string)

    week_no = report_dict["week_no"]
    year_no = report_dict["year_no"]

    if os.path.exists("data/%s/%s" % (uname, year_no)) == False:
        os.mkdir("data/%s/%s" % (uname, year_no))


    fname = "data/%s/%s/%s" % (uname, year_no, week_no)
    print fname
    f = open(fname, "w+")

    # Write the json string. 
    # We can return this as is.. on a request
    lines = f.write(report_dict_string)

    # close.. since we are done
    f.close()

    return uname

@bottle.route('/weekly/:uname/get_weekly')
def get_weekly(uname):
    week_no = bottle.request.GET.get('week_no')
    year_no = bottle.request.GET.get('year_no')

    status = 1

    fname = "data/%s/%s/%s" % (uname, year_no, week_no)

    # No data for that week/year
    if os.path.exists(fname) == False:
        status = 0
        lines  = "[]"
    else:

        f = open(fname, "r")
        lines = f.read()
        f.close()

    sdict = {
            "status" : status,
            "status_str" : lines
    };

    report = json.dumps(sdict)

    print report

    return report


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
