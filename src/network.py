import math
from math import pow


class Network(object):

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

    @property
    def mask(self):
        addr = []
        for x in xrange(self._mask / 8):
            addr.append(255)
        left_bytes = self._mask % 8
        if left_bytes:
            last_index = len(addr)
            addr.append(0)
            for x in xrange(1, left_bytes+1):
                addr[last_index] += pow(2, 8 - x)
        while len(addr) < 3:
            addr.append(0)
        return '.'.join([str(p) for p in addr])

    @property
    def beginning_addr(self, subnetwork_nb):
        pass

    @property
    def broadcast_addr(self, subnetwokr_nb):
        pass
