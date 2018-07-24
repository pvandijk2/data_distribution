import sys, shutil, fnmatch, gzip
import ftputil, os, time
# TODO: Store username/password in a secure storage
try:
    with ftputil.FTPHost('datafeeds.nationalrail.co.uk', 'ftpuser', 'A!t4398htw4ho4jy') as host:
        for name in host.listdir(host.curdir):
            # Modify destination path
            dir_name = "unknown"
            if ( fnmatch.fnmatch(name, 'pPortData.log.*')):
                dir_name = name[14:24]
            if (fnmatch.fnmatch(name, "*.xml.gz") ):
                dir_name = name[:4] + "-" + name[4:6] + "-" + name[6:8] 
            dest =  "/home/pi/schedule/" + dir_name   
            if not os.path.exists(dest):
                os.makedirs(dest)
                print( "Created the directory: " + dest)
            dest = dest + "/" + name
            if host.path.isfile(name) and host.download_if_newer(name, dest): 
                # TODO: Write this to an appropriate location
                print("Downloaded " + name + " to: " + dest) # TODO: Output download size
except Exception as e:
    print("Could not download files due to error: ")
    print(e)
