import sys, os, shutil, fnmatch, gzip, time, xmltodict, subprocess, pprint

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
                    if '201807168711349' in line and 'WNCHSTR' in line:
                        doc = xmltodict.parse(line)
                        if 'Pport' in doc and 'uR' in doc['Pport'] and 'schedule' in doc['Pport']['uR'] and '@rid' in doc['Pport']['uR']['schedule']:# and doc['Pport']['uR']['schedule']['@rid'] in rid: 
                            print("Found RID: " + doc['Pport']['uR']['schedule']['@rid'])

                        elif 'Pport' in doc and 'uR' in doc['Pport'] and 'TS' in doc['Pport']['uR'] and '@rid' in doc['Pport']['uR']['TS']:# and doc['Pport']['uR']['schedule']['@rid'] in rid: 
                            print("Found RID: " + doc['Pport']['uR']['TS']['@rid'])

                        elif 'Pport' in doc and 'uR' in doc['Pport'] and 'association' in doc['Pport']['uR'] and '@rid' in doc['Pport']['uR']['association']:# and doc['Pport']['uR']['schedule']['@rid'] in rid: 
                            print("Found RID: " + doc['Pport']['uR']['association']['@rid'])

                        else:
                            print("Line does not have rid:")
                            pprint.pprint(doc)
                            exit()
                        pprint.pprint(doc)    
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

