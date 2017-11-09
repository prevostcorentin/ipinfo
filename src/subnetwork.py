

class Subnetwork(object):

    def __init__(self, network, nb):
        if nb > network.subnetworks:
            raise Exception('Network has {} subnetworks but you want to reach {}'.format(network.subnetworks, nb))
        self._network = network
        self._nb = nb

    @property
    def machine_part(self):
        pass

    # TODO
    @property
    def beginning_addr(self, subnetwork_index):
        pass

    # TODO
    @property
    def broadcast_addr(self, subnetwork_index):
        pass
