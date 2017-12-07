# coding: utf-8

from util import dec2base


class IPAddress(object):

    def __init__(self, ip):
        self._ip = ip
        self._parts = ip.split('.')
        self._ipclass = ''

    def __str__(self):
        return '.'.join(self._parts)

    def __iter__(self):
        for p in self._parts:
            yield int(p)

    def __getitem__(self, n):
        return int(self._parts[n])

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
