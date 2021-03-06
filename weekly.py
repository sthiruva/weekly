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
def save_report(uname, respond = True):
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

    if respond == True:
        print "Report Saved"
        return "Report Saved"

    return uname

@bottle.route('/weekly/:uname/send_report')
def send_report(uname):

    # save the report first
    report_dict = save_report(uname, False)

    report_dict_string = bottle.request.GET.get('report_dict_string')
    report_dict        = json.loads(report_dict_string)


    report_array = report_dict['report_array']
    dri          = report_dict['dri']

    message = ""

    # process the DRI
    message = message + "DRI\n"
    message = message + "===\n"
    message = message + dri + "\n\n"

    # process the highlights
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
    from_user = settings["members"][uname]["email"]
    to        = []

    members = settings['members']
    for key in members.keys() :
        email = members[key]["email"]
        to.append(email)

    sendemail( from_user, to, [], "Week Report", message)

    return "Report Sent"

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

@bottle.route('/weekly/:uname/send_consolidated_report')
def send_consolidated_report(uname):

    global settings


    week_no = bottle.request.GET.get('week_no')
    year_no = bottle.request.GET.get('year_no')

    print "send_consolidated_report :: week_no = %s year_no = %s"% (week_no, year_no)

    not_found  = ""

    dri        = ""
    dri        = dri + "DRI\n"
    dri        = dri + "===\n"

    highlights = ""
    highlights = highlights + "Highlights\n"
    highlights = highlights + "==========\n"


    details = ""
    details    = details + "Details\n"
    details    = details + "=======\n"

    members = settings['members']

    for key in members.keys() :

        print key

        name  = members[key]["name"]
        email = members[key]["email"]

        fname = "data/%s/%s/%s" % (key, year_no, week_no)

        if os.path.exists(fname) : 
            f = open( fname, "r")
            lines = f.read()
            f.close()
        else:
            not_found = not_found + "%s's Weekly report not found \n" % (name)
            continue

        report_dict  = json.loads(lines)
        report_array = report_dict['report_array']
        dri          = dri + report_dict['dri'] + "\n"

        highlights = highlights + name + "\n"
        count = 1
        for (rp, hl) in report_array:
            count_str = "%d. " % count 
            if hl == True:
                highlights = highlights + count_str + rp + "\n"
                count = count + 1
        highlights = highlights + "\n"

        details = details + name + "\n"
        count = 1
        for (rp, hl) in report_array:
            count_str = "%d. " % count 
            details = details + count_str + rp + "\n"
            count = count + 1

        details = details + "\n"

    message = dri + "\n" + highlights + "\n" + details + "\n" + not_found


    from_user = settings["members"][uname]["email"]
    to        = [from_user]
    sendemail( from_user, to, [], "Week Report", message)

    return



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

    global settings

    f = open("data/settings.json", "r")
    lines = f.read()
    f.close()

    settings = json.loads(lines)

    bottle.run(host=settings["hostname"], port=8080)


    return

main()
