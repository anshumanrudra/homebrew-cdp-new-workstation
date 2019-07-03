#!/usr/bin/env python

import re

def test_matching():
    result = "Error: Cask 'maven' is unavailable: No Cask with this name exists. Did you mean one of these?\nmavensmate\nmavensmate"
    p = re.compile('.*( is unavailable:)')
    if p.match(result):
        print 'matched'
    else:
        print 'not matched'

if __name__ == '__main__':
    test_matching()