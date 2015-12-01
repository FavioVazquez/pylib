#!/usr/bin/env python
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2015-11-29 15:32:25 +0000 (Sun, 29 Nov 2015)
#
#  https://github.com/harisekhon/pytools
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback to help improve or steer this or other code I publish
#
#  http://www.linkedin.com/in/harisekhon
#

from __future__ import print_function

__author__  = 'Hari Sekhon'
__version__ = '0.1'

import coverage
import os
import sys
# using optparse rather than argparse for servers still on Python 2.6
#from optparse import OptionParser
sys.path.append(os.path.join(os.path.dirname(__file__), '/lib'))
try:
    from harisekhon.utils import *
    #from harisekhon import CLI
except ImportError, e:
    print('module import failed: %s' % e)
    sys.exit(4)

def main():
    cov = coverage.Coverage()
    cov.start()

    

    cov.stop()
    cov.save()

    cov.html_report()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
