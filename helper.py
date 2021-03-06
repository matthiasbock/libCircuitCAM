#!/usr/bin/python

from struct import unpack

#
# String to integer conversion
#
def uint16(s):
    return unpack('<H', s)[0]

def uint32(s):
    return unpack('<L', s)[0]

def float32(s):
    return unpack('<f', s)[0]

def int32(s):
    return unpack('<i', s)[0]

def uint24(s):
    return unpack('<L', '\0'+s)[0]

def sint8(s):
    return unpack('b', s)[0]

def sint16(s):
    return unpack('h', s)[0]
