#!/usr/bin/env python

# A simple script to get member details.
# Input : 'Print' view of ceg86 member table

import re

f = open('ceg-86.html', 'r')

def st(s):
    s = re.sub('&nbsp;|amp;|&#\d+;', '', re.sub('<[^<]*>', '', s))
    return s.replace(',','')

def nl():
    line = f.readline()
    return line.rstrip()

def members():
    while True:
        line = nl()
        if line.find('selected') > -1:
            yield line
        if not line:
            break;

def details(line):
    fn = st(line)
    ln = st(nl())
    dept = st(nl())
    section = st(nl())
    mobile = st(nl())
    email = st(nl())
    location = st(nl())
    company = st(nl())
    attendees = st(nl())
    home = st(nl())
    return (fn, ln, dept, section, mobile, email, location, company, home)

# the proverbial main
for m in members():
    d = [s.strip() for s in details(m)]
    print '|'.join([d[0], d[1], d[2], d[3], d[6] if d[6] else 'India'])

f.close()
