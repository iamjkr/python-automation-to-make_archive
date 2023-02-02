import sys
import os
from shutil import make_archive

with open(sys.argv[1]) as f:
    for line in f.readlines():
        root, filedir = line.rstrip('\n').split(',')
        make_archive(filedir,'zip', root)
       
 ## Create file.txt in the same directory and write the source path and destination path in it
#C:\Users\Kumar\Desktop\python-projects\Git-Clone,C:\Users\Kumar\Desktop\Python-Zip
#D:\DevOps_Test, C:\Users\Kumar\Desktop\Python-Zip
   # here source path seperated by , and destination path after ,(coma)
