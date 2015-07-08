#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Pierre Tardy
# Copyright (c) 2013 Pierre Tardy
#
# License: MIT
#
"""This module exports the Jade plugin class."""

from SublimeLinter.lint import Linter, util


class Jade(Linter):

    """Provides an interface to jade."""

    syntax = ('jade', )
    executable = 'jade'
    tempfile_suffix = 'jade'
    multiline = True
    regex = r'''(?xi)
        Error: .+?:(?P<line>\d+).*\r?\n
        (?:.*\|.*\n)+
        .*\n
        (?P<message>.*)
    '''
    error_stream = util.STREAM_STDERR

    def cmd(self):
        """Return a list with the command line to execute."""

        result = ('jade',)
        return result
