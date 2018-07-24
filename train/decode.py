import sys, xmltodict, json, os, pprint, gzip

# TODO: Create a file list for reference data and actual times
# TODO: Unzip the schedule for today
# TODO: Read in all ride id's for routes we are interested in
# TODO: Process all the files
# TODO: For each matching ride, determine if our train was delayed (and produce a report of this)
with open(sys.argv[1], "rb") as ref_in:
    #lines = ref_in.readlines()
    ref = xmltodict.parse(ref_in)
    print("Parsed, now pretty printing...")
    pprint.pprint(ref, indent=3)
    #for i in ref_in.readlines():
     #   pprint.pprint(i, indent=3)
      #  ref = xmltodict.parse(i)
      #  pprint.pprint(ref, indent=3)


#if (os.path.isfile(sys.argv[1])):
#    filename = open(sys.argv[1], "r")
#    for i in filename.readlines():
#        o = xmltodict.parse(i)
#        pprint.pprint(o, indent=3)
#        #print(json.dumps(o, indent=4) + "\n")# TODO: Write to a temp location and then convert to JSON
