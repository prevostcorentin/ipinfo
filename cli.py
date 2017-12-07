# coding: utf-8

import click
import src as ipinfo
import src.IPAddress
from src.IPAddress import IPAddress
import src.network
from src.network import Network


@click.command()
@click.argument('ip_cidr', nargs=1,
                required=True)
@click.option('--machines/--no-machines', 
              default=True,
              help='Display number of machines')
@click.option('--mask/--no-mask',
              default=True,
              help='Display mask')
@click.option('--binary/--no-binary',
              default=False,
              help='Display ip to binary format')
@click.option('--subnetworks/--no-subnetworks',
              default=True,
              help='Display ip to binary format')
@click.option('--parts/--no-parts',
              default=True,
              help='Display parts of ip address without mask')
def cli(ip_cidr, machines, mask, 
        binary, parts, subnetworks):
    """ Get ip adresses info

        Can deal with subnetworks
    """
    ip, mask = ip_cidr.split('/')
    ip = IPAddress(ip)
    network = Network(ip, mask)
    print 'IP Address:', ip
    if mask:
        print 'Mask: {}'.format(network.mask)
    if binary:
        print 'Binary: {}'.format(ip.binary)
    if subnetworks:
        print 'Number of subnetworks: {}'.format(network.subnetworks)
    if machines:
        print 'Number of machines: {}'.format(network.machines)
    if parts:
        print 'Machine part from mask {mask}: {part}'.format(mask=ip.mask,
                                                             part=ip.machine_part)

if __name__ == '__main__':
    cli()
