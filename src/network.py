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

