#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Any, Callable, Dict, Iterable, Iterator, Text, Union


Any, Callable, Dict, Iterable, Iterator, Text, Union


class Deffered(object):  # {{{1
    def then(self, fn1, fn2):  # {{{1
        # type: (Callable[[Text], None], Callable[[], None]) -> 'Deffered'
        pass


class Element(object):  # {{{1
    pass


class Event(object):  # {{{1
    pass


class jQuery(Iterable):  # {{{1
    def __init__(
        self,
        selector,     # type: Union[Text, Element, Callable[[Event], bool]]
        context=None  # type: Union[None, Text, 'jQuery']
    ):  # {{{1
        # type: (...) -> None
        pass

    @classmethod
    def ajax(cls, inf):  # {{{1
        # type: (Dict[Text, Any]) -> Deffered
        pass

    @classmethod
    def parseHTML(cls, src):  # {{{1
        # type: (Text) -> 'jQuery'
        pass

    def __iter__(self):  # {{{1
        # type: () -> Iterator[Element]
        pass

    def append(self, src):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def attr(self, name, **kw):  # {{{1
        # type: (Text, Dict[Text, Any]) -> 'jQuery'
        return self

    def text(self, *arg, **kw):  # {{{1
        # type: (Text, Dict[Text, Any]) -> 'jQuery'
        return self

    def val(self, name, **kw):  # {{{1
        # type: (Text, Dict[Text, Any]) -> 'jQuery'
        return self

    def off(self, name):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def on(self, name, fn):  # {{{1
        # type: (Text, Callable[[Event], bool]) -> 'jQuery'
        return self

# vi: ft=python
