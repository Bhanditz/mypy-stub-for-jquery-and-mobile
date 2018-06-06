#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Any, Dict, Callable, Optional, Text, Union

# __pragma__("skip")
from jQuery import Deffered, Element, Event, jQuery  # stub

if False:
    _jq = Any
    Deffered, Element, Event, jQuery
    Any, Callable, Dict, Optional, Text, Union
# __pragma__("noskip")
# __pragma__("alias", "jQuery", "$")


def jq(sel, ctx=None):  # {{{1
    # type: (Union[Element, Text], Optional[jQuery]) -> jQuery
    if ctx is None:
        return jQuery(sel)
    return jQuery(sel, ctx)


def ajax(dct):  # {{{1
    # type: (Dict[Text, Any]) -> Deffered
    return jQuery.ajax(dct)


def parseHTML(src):  # {{{1
    # type: (Text) -> jQuery
    return jQuery.parseHTML(src)


def dummy_event():  # {{{1
    # type: () -> Event
    return Event()


def on_load(fn):  # {{{1
    # type: (Callable[[Event], bool]) -> None
    jQuery(fn)

# vi: ft=python:et:ts=4:fdm=marker:nowrap
