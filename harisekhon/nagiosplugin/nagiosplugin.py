#!/usr/bin/env python
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2014-09-15 20:49:37 +0100 (Mon, 15 Sep 2014)
#
#  https://github.com/harisekhon/pylib
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback
#  to help improve or steer this or other code I publish
#
#  https://www.linkedin.com/in/harisekhon
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# from __future__ import unicode_literals

import os
import sys
import traceback
# import logging
# Python 2.6+ only
from abc import ABCMeta, abstractmethod
libdir = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(libdir)
# pylint: disable=wrong-import-position
from harisekhon.utils import ERRORS, qquit, CodingErrorException, log
from harisekhon import CLI
from harisekhon.nagiosplugin.threshold import Threshold
from harisekhon.nagiosplugin.threshold import InvalidThresholdException

__author__ = 'Hari Sekhon'
__version__ = '0.6'

class NagiosPlugin(CLI):
    """
    HariSekhon.NagiosPlugin class for rapid development of Nagios Plugins in Python
    """
    __version__ = __version__
    # abstract class
    __metaclass__ = ABCMeta

    def __init__(self):
        # Python 2.x
        super(NagiosPlugin, self).__init__()
        # Python 3.x
        # super().__init__()
        # redirect_stderr_stdout()
        self.__status__ = 'UNKNOWN'
        self.msg = 'MESSAGE NOT DEFINED'
        self.__thresholds = {'warning': None, 'critical': None}

    # ============================================================================ #
    #                           Nagios Exit Code Functions
    # ============================================================================ #

    # Set status safely - escalate only

    # there is no ok() since that behaviour needs to be determined by scenario

    def get_status(self):
        return self.__status__

    def set_status(self, status):
        if not ERRORS.has_key(status):
            raise CodingErrorException("invalid status '%(status)s' passed to harisekhon.NagiosPlugin.set_status()")
        self.__status__ = status

    def ok(self): # pylint: disable=invalid-name
        self.set_status('OK')

    def warning(self):
        if self.get_status() != 'CRITICAL':
            self.set_status('WARNING')

    def critical(self):
        self.set_status('CRITICAL')

    def unknown(self):
        if self.get_status() == 'OK':
            self.set_status('UNKNOWN')

    ############################
    def is_ok(self):
        return self.get_status() == 'OK'

    def is_warning(self):
        return self.get_status() == 'WARNING'

    def is_critical(self):
        return self.get_status() == 'CRITICAL'

    def is_unknown(self):
        return self.get_status() == 'UNKNOWN'

    # ============================================================================ #

    def set_threshold(self, name, threshold):
        if not isinstance(threshold, Threshold):
            raise CodingErrorException('passed a non-threshold to NagiosPlugin.set_threshold()')
        self.__thresholds[name] = threshold

    def get_threshold(self, name):
        try:
            _ = self.__thresholds[name]
            if _ is None:
                raise CodingErrorException('threshold {0} is not set (None)'.format(name))
            return _
        except KeyError:
            raise CodingErrorException("threshold '%s' does not exist" % name +
                                       "invalid name passed to NagiosPlugin.check_threshold() - typo?")

    # Generic exception handler for Nagios to rewrite any unhandled exceptions as UNKNOWN rather than allowing
    # the default python exit code of 1 which would equate to WARNING in Nagios compatible systems
    def main(self):
       try:
            # Python 2.x
            super(NagiosPlugin, self).main()
            # Python 3.x
            # super().__init__()
            # redirect_stderr_stdout()
       except Exception as _:
           print('UNKNOWN: {0}'.format(_))
           # prints to stderr, Nagios spec wants stdout
           # traceback.print_exc()
           print('\n{0}'.format(traceback.format_exc()), end='')
           sys.exit(ERRORS['UNKNOWN'])

    @abstractmethod
    def run(self): # pragma: no cover
        pass

    def end(self):
        log.info('end\n{0}\n'.format('='*80))
        qquit(self.get_status(), self.msg)
