#!/usr/bin/python

import csv
import sys

def extract_name_and_email(r):
    # First Name,_,Last Name,_,_,_,_,_,_,_,_,_,_,_,E-mail Address,
    # E-mail 2 Address,E-mail 3 Address,...
    first, last, email0, email1, email2 = r[0], r[2], r[14], r[15], r[16]
    email = None
    for val in email0, email1, email2:
        if val != None and val != "":
            email = email0
            break
    return first, last, email

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Insufficient arguments.\n")
        sys.exit(1)
    path = sys.argv[1]
    reader = csv.reader(open(path, 'r'))
    for row in reader:
        first, last, email = extract_name_and_email(row)
        if email == None:
            sys.stderr.write("Bad email for %s %s.\n" % (first, last))
        else:
            sys.stdout.write("%s,%s,%s\n" % (first, last, email))


