#
# Reads file from current directory 
# Filters the images 
# Renames the files
#
from os import listdir
from os.path import isfile, join
import magic
import os

onlyfiles = [f for f in listdir('.') if isfile(join('.', f)) and magic.from_file(f, mime=True).startswith('image')]

print(onlyfiles)
i = 0
for f in onlyfiles:
    i+=1
    print('chanyon' + str(i) + '.' + (str.split(f, '.')[-1]))
    os.rename(f, 'chanyon' + str(i) + '.' + (str.split(f, '.')[-1]))
