from sys import argv
from os.path import exists
script, filename1 = argv


print "Does the output file exist? %r" % exists(filename1)
open(filename1, 'w').write("I have a dream")

