#!/bin/env python

"""Geolocation of worker nodes via lat/long
"""

from __future__ import print_function
import os
import re
import socket
import sys

import geoip2.database


def get_hostname():
    """Returns a hostname of the current host (or CE if run on the osG) that can be used for for IP geolocation.
    """
    machine_ad_file_name = os.getenv('_CONDOR_MACHINE_AD')

    try:
        with open(machine_ad_file_name, 'r') as machine_ad_file:
            machine_ad = machine_ad_file.read()

        hostname = re.search(r'GLIDEIN_Gatekeeper = "(.*):\d*/jobmanager-\w*"',
                             machine_ad,
                             re.MULTILINE).group(1)
    except AttributeError:
        try:
            hostname = re.search(r'GLIDEIN_Gatekeeper = "(\S+) \S+:9619"',
                                 machine_ad,
                                 re.MULTILINE).group(1)
        except AttributeError:
            hostname = socket.getfqdn()
    except TypeError:
        hostname = socket.getfqdn()

    return socket.gethostbyname(hostname)


def main():
    """Print the lat/long of the current host or CE if run in the OSG
    """
    geolite_db = sys.argv[1]
    reader = geoip2.database.Reader(geolite_db)

    try:
        response = reader.city(get_hostname())
    except Exception as exc:
        print(exc.message, file=sys.stderr)
        lat, lon = (0, 0)
    else:
        lat = response.location.latitude
        lon = response.location.longitude

    print("{0}, {1}".format(lat, lon))


if __name__ == '__main__':
    main()
