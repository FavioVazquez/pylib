#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2014-09-15 20:49:22 +0100 (Mon, 15 Sep 2014)
#
#  http://github.com/harisekhon/pylib
#
#  License: see accompanying LICENSE file
#

# ============================================================================ #
#                   PyUnit Tests for HariSekhon.CLI
# ============================================================================ #

from __future__ import print_function

import os
import sys
import unittest
from optparse import OptionConflictError
# inspect.getfile(inspect.currentframe()) # filename
# libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
libdir = os.path.dirname(__file__).rsplit('test')[0]
sys.path.append(libdir)
from harisekhon.utils import *
from harisekhon import CLI

class test_cli(unittest.TestCase):

    # XXX: must prefix with test_ in order for the tests to be called

    class SubCLI(CLI):
        def run(self):
            print("running SubCLI()")

    # bails on unit2 discover -v / python -m unittest discover -v
    # because the -v switch trips optparse
    def test_SubCLI(self):
        c = self.SubCLI()
        c.add_hostoption(name='Ambari', default_port=8080)
        c.add_useroption(name='Ambari')
        try:
            c.add_hostoption()
            raise Exception('failed to throw OptionConflictError from optparse OptionParser')
        except OptionConflictError, e:
            pass
        try:
            c.main()
        except SystemExit, e:
            if e.code != 2:
                raise Exception('wrong exit code != 2 when exiting main() from base class CLI')
        try:
            c.usage()
            raise Exception('failed to exit on CLI.usage()')
        except SystemExit, e:
            if e.code != 3:
                raise Exception('wrong exit code != 3 when exiting usage() from base class CLI')

    # disabled abstract enforcement as it's Python 2.6+ only
    # but base class exits 2 in run() so can catch that too
    def test_CLI_abstract(self):
        try:
            c = CLI()
            c.main()
            raise Exception('failed to raise a TypeError when attempting to instantiate abstract class CLI')
        except TypeError:
            pass
        except CodingErrorException, e:
            if not re.search('abstract', e.message):
                raise Exception('raised CodingErrorException from CLI.main() but message mismatch')
        except SystemExit, e:
            if e.code != 2:
                raise Exception('wrong exit code != 2 when exiting main() from base class CLI')


if __name__ == '__main__':
    # increase the verbosity
    # verbosity Python >= 2.7
    #unittest.main(verbosity=2)
    log.setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(test_cli)
    unittest.TextTestRunner(verbosity=2).run(suite)