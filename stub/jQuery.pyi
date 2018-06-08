#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import (Any, Callable, Dict, Iterable, Iterator,
                    Optional, Sized, Text, Union, overload)

from stub_firefox import Element, Event


Any, Callable, Dict, Iterable, Iterator, Optional, Sized, Text, Union
Element, Event


class jqXHR(object):  # {{{1
    ...  # {{{1


class Deffered(object):  # {{{1
    def then(self,  # {{{1
             fn1,  # type: Callable[[Text, Text, jqXHR], bool]
             fn2=None  # type: Optional[Callable[[jqXHR, Text, Text], bool]]
             ):  # typ
        # type: (...) -> 'Deffered'
        pass


class Pickadate(object):  # {{{1
    def set(self, name, val):  # {{{1
        # type: (Text, Text) ->  'Pickadate'
        pass


class jQuery(Iterable, Sized):  # {{{1
    # {{{1
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

    def clone(self, fWithDataAndEvents):  # {{{1
        # type: (bool) -> 'jQuery'
        ...

    def prepend(self, src):  # {{{1
        # type: (Union[Text, 'jQuery']) -> 'jQuery'
        return self

    # attr(self, name, *arg, **kw):  # {{{1
    @overload
    def attr(self, name, arg):
        # type: (Text, Text) -> 'jQuery'
        ...

    @overload
    def attr(self, name):
        # type: (Text) -> Text
        ...

    # prop(self, name, *arg):  # {{{1
    @overload
    def prop(self, name, val):
        # type: (Text, Union[Text, float]) -> 'jQuery'
        return self

    @overload
    def prop(self, name):
        # type: (Text) -> Text
        return ""

    def css(self, dat):  # {{{1
        # type: (Dict[Text, Text]) -> 'jQuery'
        return self

    # text {{{1
    @overload
    def text(self):
        # type: () -> Text
        ...

    @overload
    def text(self, arg):
        # type: (Text) -> 'jQuery'
        ...

    # val {{{1
    @overload
    def val(self,
            arg: Union[Text, float, bool]
            ) -> 'jQuery': ...

    @overload
    def val(self) -> Text: ...

    def off(self, *name):  # {{{1
        # type: (Text) -> 'jQuery'
        return self

    def on(self, name, fn):  # {{{1
        # type: (Text, Callable[[Event], Optional[bool]]) -> 'jQuery'
        return self

    # remove {{{1
    @overload
    def remove(self):
        # type: () -> None
        ...

    @overload
    def remove(self, sel):
        # type: (Text) -> None
        ...

    def width(self):  # {{{1
        # type: () -> float
        return 0.0

    def height(self):  # {{{1
        # type: () -> float
        return 0.0

    def select(self):  # {{{1
        # type: () -> 'jQuery'
        return self

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
