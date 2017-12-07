# coding: utf-8

import click
import ipinfo
from ipinfo import IpAddress, Network

@click.group()
@click.version_option()
def cli():
    """ Get ip adresses info

        Can deal with subnetworks
    """

@click.command()
@click.option('--ip', help='IP address')
@click.option('--mask', default=None, help='Subnetwork mask')
def machines(ip, mask):
    ip = IpAddress(ip)
    if not mask:
        mask = ip.mask
    print Network(ip).machines

@click.command()
@click.option('--ip', help='IP address')
def mask(ip):
    print IpAdress(ip).mask

@click.command()
@click.option('--ip', help='IP address')
def binary(ip):
    print IpAdress(ip).binary
