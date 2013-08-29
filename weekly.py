import bottle
import datetime

import pickle
import os
import json

import smtplib

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

@bottle.route('/weekly/:uname/send_report')
def send_report(uname):

    # save the report first
    report_dict = save_report(uname)

    report_dict_string = bottle.request.GET.get('report_dict_string')
    report_dict        = json.loads(report_dict_string)

    print report_dict

    report_array = report_dict['report_array']

    # process the highlights first

    message = ""
    message = message + "Highlights\n"
    message = message + "==========\n"

    count = 1
    for (rp, hl) in report_array:
        count_str = "%d. " % count 
        if hl == True:
            message = message + count_str + rp + "\n"
            count = count + 1

    count = 1
    message = message + "\n\n"
    message = message + "Details\n"
    message = message + "=======\n"
    for (rp, hl) in report_array:
        count_str = "%d. " % count 
        message = message + count_str + rp + "\n"
        count = count + 1

    # this should come from a config file
    sendemail( 'test@localhost', ['shathi01@test'], [], "Week Report", message)


    return

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


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              smtpserver='localhost'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
  
    server = smtplib.SMTP(smtpserver)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

class Settings:
    def __init__(self):
        self.ms     = dict()
        self.projs  = dict()
        self.notify = dict()
        return


def main():
    bottle.run(host='blr-lin-615.blr.arm.com', port=8080)
    return

main()
