# coding: utf-8

import sys
from sys import argv
import math
from math import pow


class NetworkConfiguration(object):

    def __init__(self, ip, mask):
        self._ip = ip
        self._mask = int(mask)
        self._subnetwork_bits = int(mask) - ip.mask

    @property
    def subnetworks(self):
        return int(pow(2, self._subnetwork_bits))

    @property
    def machines(self):
        return int(pow(2, 32 - self._mask))

    # TODO
    @property
    def beginning_addr(self):
        pass

    # TODO
    @property
    def broadcast_addr(self):
        pass


class IpAddress(object):

    def __init__(self, ip):
        self._parts = ip.split('.')
        self._ipclass = ''

    def __str__(self):
        s = ''
        for p in self._parts:
            s += p+'.'
        return s.rstrip('.')

    def __iter__(self):
        for p in self._parts:
            yield p

    @property
    def mask(self):
        if self.ipclass == 'A':
            return 8
        elif self.ipclass == 'B':
            return 16
        elif self.ipclass == 'C':
            return 24

    @property
    def ipclass(self):
        if self._ipclass:
            return self._ipclass
        first_byte = int(self._parts[0])
        if first_byte > 0:
            if first_byte < 126:
                return 'A'
            elif first_byte < 192:
                return 'B'
            elif first_byte < 223:
                return 'C'
        return None

    @property
    def machine_part(self):
        if self.ipclass == 'A':
            parts = self._parts[1:]
        elif self.ipclass == 'B':
            parts = self._parts[2:]
        elif self.ipclass == 'C':
            parts = self._parts[3:]
        s = ''
        for p in parts:
            s += p+'.'
        return s.rstrip('.')

    @property
    def binary(self):
        converted = ''
        for p in self._parts:
            converted += dec2base(2, int(p))+'.'
        return converted.rstrip('.')

def dec2base(base, decimal):
    binaries = []
    while decimal > 0:
        rest = decimal % base
        binaries.append(rest)
        decimal = decimal / base
    s = ''
    for addr_part in reversed(binaries):
        s += str(addr_part)
    while len(s) < 8:
        s = '0' + s
    return s

# TODO: format a mask integer into address format

if __name__ == "__main__":
    if len(argv) < 3:
        print 'Manque l\'adresse IP et le masque de sous-réseau'
    else:
        subnet_mask = argv[2]
        ip = IpAddress(argv[1])
        conf = NetworkConfiguration(ip, subnet_mask)
        print '{}/{}'.format(ip, ip.mask)
        print 'class:', ip.ipclass
        print 'binary:', ip.binary
        print 'machine:', ip.machine_part
        print
        print 'with subnetwork mask', subnet_mask
        print 'subnetworks number:', conf.subnetworks
        print 'machines number:', conf.machines
