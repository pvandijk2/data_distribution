import sys, os, shutil, fnmatch, gzip, time, xmltodict, subprocess, pprint, traceback, datetime

def get_arrival(l, station_name):
    actual_arrival = None
    diff = None
    expected_arrival = None

    if isinstance(l, dict) and '@tpl' in l and l['@tpl'][:4] == station_name and '@pta' in l:
        expected_arrival = datetime.datetime.strptime(l['@pta'], '%H:%M')

        if 'ns3:arr' in l and '@et' in l['ns3:arr']:
            actual_arrival = datetime.datetime.strptime(l['ns3:arr']['@et'], '%H:%M')
            diff = ((actual_arrival  + datetime.timedelta(hours=12)) - (expected_arrival + datetime.timedelta(hours=12))) 
        elif 'ns3:arr' in l and '@at' in l['ns3:arr']:
            actual_arrival = datetime.datetime.strptime(l['ns3:arr']['@at'], '%H:%M')
            diff = ((actual_arrival  + datetime.timedelta(hours=12)) - (expected_arrival + datetime.timedelta(hours=12))) 

    return expected_arrival, actual_arrival, diff 
    
def get_departure(l, station_name):
    actual_departure = None
    expectured_departure = None
    diff = None

    if isinstance(l, dict) and '@tpl' in l and l['@tpl'] == station_name and '@ptd' in l:
        expected_departure = datetime.datetime.strptime(l['@ptd'], '%H:%M')

        if 'ns3:dep' in l and '@et' in l['ns3:dep']:
            actual_departure = datetime.datetime.strptime(l['ns3:dep']['@et'], '%H:%M')
            diff = ((actual_departure  + datetime.timedelta(hours=12)) - (expected_departure + datetime.timedelta(hours=12))) 
        elif 'ns3:dep' in l and '@at' in l['ns3:dep']:
            actual_departure = datetime.datetime.strptime(l['ns3:dep']['@at'], '%H:%M')
            diff = ((actual_departure  + datetime.timedelta(hours=12)) - (expected_departure + datetime.timedelta(hours=12))) 
 
    return expected_departure, actual_departure, diff

date = sys.argv[1]
date_match = date[:4] + "-" + date[4:6] + "-" + date[6:8]
dirname = "/home/pi/schedule/" + date_match
# Unzip the gz files
#For filename in os.listdir(dirname):
#    if ( fnmatch.fnmatch(filename, '*.xml.gz')):
#        print("Unziping " + filename)
#        with gzip.open(filename, 'rb') as f_in:
#            with open(dirname + "/" + filename[:-3], 'wb') as f_out:
#                shutil.copyfileobj(f_in, f_out)
#                print("Unzipped the file: " + f_out.name) 
#
## Split the Schedule
#For filename in os.listdir(dirname):
#    if ( fnmatch.fnmatch(filename, '*_v8.xml')):
#        print("Spliting: " + filename)
#        rc = subprocess.call(["xml_split", "-s 1Mb", dirname + "/" + filename]) 

# Read in the schedule
rid = []
#for filename in os.listdir(dirname):
#    if ( fnmatch.fnmatch(filename, '*_v8-*.xml')):
#        with open(dirname + "/" + filename) as fd:
#            doc = xmltodict.parse(fd.read())
#            
#            if 'xml_split:root' in doc and 'Journey' in doc['xml_split:root']:
#                for j in doc['xml_split:root']['Journey']:
#                    try:
#                        if '@rid' in j and '@toc' in j and j['@toc'] == 'SW' and 'OR' in j and isinstance(j['OR'], dict) and j['OR']['@tpl'][:4] == 'WATR':
#                            if 'IP' in j and isinstance(j['IP'], list):
#                                for ip in j['IP']:
#                                    if '@tpl' in ip and ip['@tpl'] == 'WNCHSTR':
#                                        print("Found route: " + j['@rid'] + " filename: " + filename)
#                                        rid.append([j['@rid']])
#                    except Exception as e:
#                        print(e)
#                        pprint.pprint(j)
#                        exit()
for filename in os.listdir(dirname):
    #print("Comparing " + filename + " against: pPortData.log.*") 
    if ( fnmatch.fnmatch(filename, 'pPortData.log.*')):
        with open(dirname + "/" + filename) as fd:
            for line in fd.readlines():
                try:
                    #if '201807168711349' in line and 'WNCHSTR' in line:

                    if 'WATR' in line and 'WNCHSTR' in line and 'LateReason' in line:
                        doc = xmltodict.parse(line)
                        try:
                            wat_expected_arrival = None
                            wat_actual_arrival = None
                            wat_expected_departure = None
                            wat_actual_departure = None

                            win_expected_arrival = None
                            win_actual_arrival = None
                            win_expected_departure = None
                            win_actual_departure = None

                            for l in doc['Pport']['uR']['TS']['ns3:Location']:
                                win_expected_arrival, win_actual_arrival, diff = get_arrival(l, "WNCHSTR")
                                if win_expected_arrival != None:
                                    print("Winchester Expected Arrival: " + str(win_expected_arrival) + " actual arrival: " + str(win_actual_arrival) + " Time difference: " + str(diff))
#                                if isinstance(l, dict) and '@tpl' in l and l['@tpl'][:4] == 'WATR' and '@pta' in l:
#                                    actual_arrival = 0
#                                    offset = datetime.datetime.strptime('12:00', '%H:%M')
#                                    expected_arrival = datetime.datetime.strptime(l['@pta'], '%H:%M')
#                                    #expected_arrival = l['@pta']
#
#                                    if 'ns3:arr' in l and '@et' in l['ns3:arr']:
#                                        actual_arrival = datetime.datetime.strptime(l['ns3:arr']['@et'], '%H:%M')
#                                        #print("Winchester time difference: " + str((actual_arrival  + offset) - (expected_arrival + offset)))
#                                        diff = ((actual_arrival  + datetime.timedelta(hours=12)) - (expected_arrival + datetime.timedelta(hours=12))) 
#                                        print("Waterloo time difference: " + str(diff.seconds//3600) + ":" + str((diff.seconds//60)%60) + " Actual Arrival: " + str(actual_arrival.hour) + ":" + str(actual_arrival.minute) + " Expected Arrival: " + str(expected_arrival.hour) + ":" + str(expected_arrival.minute) )
#                                    elif 'ns3:arr' in l and '@at' in l['ns3:arr']:
#                                        actual_arrival = datetime.datetime.strptime(l['ns3:arr']['@at'], '%H:%M')
#                                        diff = ((actual_arrival  + datetime.timedelta(hours=12)) - (expected_arrival + datetime.timedelta(hours=12))) 
#                                        print("Waterloo time difference: " + str(diff.seconds//3600) + ":" + str((diff.seconds//60)%60) + " Actual Arrival: " + str(actual_arrival.hour) + ":" + str(actual_arrival.minute) + " Expected Arrival: " + str(expected_arrival.hour) + ":" + str(expected_arrival.minute) )
#
                                if isinstance(l, dict) and '@tpl' in l and l['@tpl'] == 'WNCHSTR':
                                    actual_arrival = 0
                                    offset = datetime.datetime.strptime('12:00', '%H:%M')
                                    expected_arrival = datetime.datetime.strptime(l['@pta'], '%H:%M')
                                    #expected_arrival = l['@pta']

                                    if 'ns3:arr' in l and '@et' in l['ns3:arr']:
                                        actual_arrival = datetime.datetime.strptime(l['ns3:arr']['@et'], '%H:%M')
                                        #print("Winchester time difference: " + str((actual_arrival  + offset) - (expected_arrival + offset)))
                                        diff = ((actual_arrival  + datetime.timedelta(hours=12)) - (expected_arrival + datetime.timedelta(hours=12))) 
                                        print("Winchester time difference: " + str(diff.seconds//3600) + ":" + str((diff.seconds//60)%60) + " Actual Arrival: " + str(actual_arrival.hour) + ":" + str(actual_arrival.minute) + " Expected Arrival: " + str(expected_arrival.hour) + ":" + str(expected_arrival.minute) )
                                    elif 'ns3:arr' in l and '@at' in l['ns3:arr']:
                                        actual_arrival = datetime.datetime.strptime(l['ns3:arr']['@at'], '%H:%M')
                                        diff = ((actual_arrival  + datetime.timedelta(hours=12)) - (expected_arrival + datetime.timedelta(hours=12))) 
                                        print("Winchester time difference: " + str(diff.seconds//3600) + ":" + str((diff.seconds//60)%60) + " Actual Arrival: " + str(actual_arrival.hour) + ":" + str(actual_arrival.minute) + " Expected Arrival: " + str(expected_arrival.hour) + ":" + str(expected_arrival.minute) )

                                if isinstance(l, dict) and '@tpl' in l and l['@tpl'][:4] == 'WATR' and '@ptd' in l:
                                    actual_depival = 0
                                    offset = datetime.datetime.strptime('12:00', '%H:%M')
                                    expected_depival = datetime.datetime.strptime(l['@ptd'], '%H:%M')
                                    #expected_depival = l['@pta']

                                    if 'ns3:dep' in l and '@et' in l['ns3:dep']:
                                        actual_depival = datetime.datetime.strptime(l['ns3:dep']['@et'], '%H:%M')
                                        #print("Waterloo time difference: " + str((actual_depival  + offset) - (expected_depival + offset)))
                                        diff = ((actual_depival  + datetime.timedelta(hours=12)) - (expected_depival + datetime.timedelta(hours=12))) 
                                        print("Waterloo time difference: " + str(diff.seconds//3600) + ":" + str((diff.seconds//60)%60) + " Actual Departure: " + str(actual_depival.hour) + ":" + str(actual_depival.minute) + " Expected Departure: " + str(expected_depival.hour) + ":" + str(expected_depival.minute) )
                                    elif 'ns3:dep' in l and '@at' in l['ns3:dep']:
                                        actual_depival = datetime.datetime.strptime(l['ns3:dep']['@at'], '%H:%M')
                                        diff = ((actual_depival  + datetime.timedelta(hours=12)) - (expected_depival + datetime.timedelta(hours=12))) 
                                        print("Waterloo time difference: " + str(diff.seconds//3600) + ":" + str((diff.seconds//60)%60) + " Actual Departure: " + str(actual_depival.hour) + ":" + str(actual_depival.minute) + " Expected Departure: " + str(expected_depival.hour) + ":" + str(expected_depival.minute) )
                                          
                        except Exception as e:
                            print("Could not process line")
                            pprint.pprint(doc)    
                            traceback.print_exc(file=sys.stdout)
                            exit()

                        #if 'Pport' in doc and 'uR' in doc['Pport'] and 'schedule' in doc['Pport']['uR'] and '@rid' in doc['Pport']['uR']['schedule'] and 'ns2:OR' in doc['Pport']['uR']['schedule'] and 'ns2:IP' in doc['Pport']['uR']['schedule'] and '@tpl' in doc['Pport']['uR']['schedule']['ns2:OR'] and doc['Pport']['uR']['schedule']['ns2:OR']['@tpl'][:4] == 'WATR':
                        #    for j in doc['Pport']['uR']['schedule']['ns2:IP']:
                        #        if '@tpl' in j and j['@tpl'] == 'WNCHSTR' and '@wta' in j and '@pta' in j:
                        #            print("Predicted: " + j['@pta'] + " Actual: " + j['@wta'] + " Found RID and origin: " + doc['Pport']['uR']['schedule']['@rid']  )

#0                        if 'Pport' in doc and 'uR' in doc['Pport'] and 'TS' in doc['Pport']['uR'] and '@rid' in doc['Pport']['uR']['TS']:# and doc['Pport']['uR']['schedule']['@rid'] in rid: 
#0                            print("Found TS RID: " + doc['Pport']['uR']['TS']['@rid'])
#0                            pprint.pprint(doc)    
#
#                        elif 'Pport' in doc and 'uR' in doc['Pport'] and 'association' in doc['Pport']['uR'] and '@rid' in doc['Pport']['uR']['association']:# and doc['Pport']['uR']['schedule']['@rid'] in rid: 
#                            print("Found association RID: " + doc['Pport']['uR']['association']['@rid'])
#
#                        #else:
                         #   print("Line does not have rid:")
                         #   pprint.pprint(doc)
                         #   exit()
                        #pprint.pprint(doc)    
                except Exception as e:
                    print("Could not process line: " + line)
                    print(e)
                    exit()
#                else:
#                    print("Rid size: " )
#                    print(len(rid))
#                    pprint.pprint(doc)
#                    exit()
            # Identify all southwest trains leaving Waterloo and arriving in Winchester

# Process timetable XML files
#for filename in os.listdir(dirname):
#    if ( fnmatch.fnmatch(filename, 'pPort.xml')):
#        print("Reading in times: " + filename)
#        with open(dirname + "/" + filename) as fd:
#            doc = xmltodict.parse(fd.read())
#            print("Doc: ")
#            print(doc)
#            time.sleep(15)
# Output all match train services
# Detect those that are canceled or late


#if not os.path.exists("../" + date_match):
#    os.makedirs("../" + date_match)
#
#for file in os.listdir(os.curdir):
##for root, dirs, file in os.walk(os.curdir, topdown=True):
##        dirs[:] = [d for d in dirs if d not in exclude]
#        if ( fnmatch.fnmatch(file, date + '*') or fnmatch.fnmatch(file, "*" + date_match + "*") ) and os.path.isfile(file):
#            print("Moving " + file + " to " + date_match + "/" + file)
#            shutil.move(file, date_match + "/" + file)
#with gzip.open(date + "*_v8.xml.gz", 'rb') as f_in:
#        with open(date + '_v8.xml', 'wb') as f_out:
#                    shutil.copyfileobj(f_in, f_out)

