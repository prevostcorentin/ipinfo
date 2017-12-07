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
def cli(ip_cidr, machines, mask, binary):
    """ Get ip adresses info

        Can deal with subnetworks
    """
    ip, mask = ip_cidr.split('/')
    ip = IPAddress(ip)
    network = Network(ip, mask)
    print 'IP Address:', ip
    if mask:
        print 'Mask:', ip.mask
    if binary:
        print 'Binary', ip.binary
    if machines:
        print 'Number of machines:', network.machines

if __name__ == '__main__':
    cli()
