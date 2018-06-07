#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import (Any, Callable, Dict, Iterable, Iterator,
                    Optional, Sized, Text, Union, )

from stub_firefox import Element, Event


Any, Callable, Dict, Iterable, Iterator, Optional, Sized, Text, Union
Element, Event


class Deffered(object):  # {{{1
    def then(self,  # {{{1
             fn1,  # type: Callable[[Text], None]
             fn2=None  # type: Optional[Callable[[], None]]
             ):  # typ
        # type: (...) -> 'Deffered'
        pass


class Pickadate(object):  # {{{1
    def set(self, name, val):  # {{{1
        # type: (Text, Text) ->  'Pickadate'
        pass


class jQuery(Iterable, Sized):  # {{{1
    def __init__(
        self,
        selector,     # type: Union[Text, Element, Callable[[Event], bool]]
        *context      # type: Union[Element, 'jQuery']
    ):  # {{{1
        # type: (...) -> None
        self.length = 0

    # class method {{{1
    @classmethod
    def ajax(cls, inf):  # {{{1
        # type: (Dict[Text, Any]) -> Deffered
        pass

    @classmethod
    def extend(cls, src, upd):  # {{{1
        # type: (Any, Dict[Text, Any]) -> Dict[Text, Any]
        pass

    @classmethod
    def param(cls, src):  # {{{1
        # type: (Any) -> Text
        pass

    @classmethod
    def parseHTML(cls, src):  # {{{1
        # type: (Text) -> Element
        pass

    def __iter__(self):  # {{{1
        # type: () -> Iterator[Element]
        pass

    # instance method {{{1
    def __getitem__(self, key):  # {{{1
        # type: (int) -> Element
        return Element()

    def __len__(self):  # {{{1
        # type: () -> int
        return 0

    def filter(self, sel):  # {{{1
        # type: (Text) -> 'jQuery'
        return jQuery("")  # just indicate new object...

    def addClass(self, classes):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def append(self, src):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def attr(self, name, *arg, **kw):  # {{{1
        # type: (Text, Text, Dict[Text, Any]) -> Union[Text, 'jQuery']
        return self

    def prop(self, name, *arg):  # {{{1
        # type: (Text, Text) -> Union[Text, 'jQuery']
        return self

    def css(self, dat):  # {{{1
        # type: (Dict[Text, Text]) -> 'jQuery'
        return self

    def text(self, *arg, **kw):  # {{{1
        # type: (Text, Dict[Text, Any]) -> Union[Text, 'jQuery']
        return self

    def val(self, *arg):  # {{{1
        # type: (Union[bool, float, Text]) -> Union[Text, 'jQuery']
        return ""

    def off(self, name):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def on(self, name, fn):  # {{{1
        # type: (Text, Callable[[Event], Optional[bool]]) -> 'jQuery'
        return self

    def remove(self):  # {{{1
        # type: () -> None
        pass

    def width(self):  # {{{1
        # type: () -> float
        return 0.0

    def height(self):  # {{{1
        # type: () -> float
        return 0.0

    def serialize(self):  # {{{1
        # type: () -> Text
        pass

    def submit(self):  # {{{1
        # type: () -> None
        pass

    def fadeIn(self, mode):  # {{{1
        # type: (Text) -> 'jQuery'
        pass

    def fadeOut(self, mode):  # {{{1
        # type: (Text) -> 'jQuery'
        pass

    def focus(self, *arg):  # {{{1
        # type: (Text) -> 'jQuery'
        pass

    # method of pickadate {{{1
    def pickadate(self, dat):  # {{{1
        # type: (Union[Text, Dict[Text, Any]]) -> Pickadate
        '''monkey patching by pickadate javascript library
        '''
        return Pickadate()

    # method of jQueryMobile {{{1
    def dialog(self, cmd):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def selectmenu(self, cmd):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

# end of file {{{1
# vi: ft=python:et:ts=4:nowrap:fdm=marker
