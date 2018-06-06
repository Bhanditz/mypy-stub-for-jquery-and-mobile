#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Any, Text


Any, Text


class _console(object):  # {{{1
    '''
        name was changed to _console,
        because to prevent transcrypt confuse.
    '''
    @classmethod
    def debug(cls, msg, *arg):  # cls {{{1
        # type: (Text, Any) -> None
        pass

# vi: ft=python
