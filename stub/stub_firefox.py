#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Any, Text


Any, Text


class console(object):  # {{{1
    '''
        name was changed to _console,
        because to prevent transcrypt confuse.
    '''
    @classmethod
    def debug(cls, msg, *arg):  # cls {{{1
        # type: (Text, Any) -> None
        pass

    @classmethod
    def error(cls, msg, *arg):  # cls {{{1
        # type: (Text, Any) -> None
        pass

    @classmethod
    def info(cls, msg, *arg):  # cls {{{1
        # type: (Text, Any) -> None
        pass

    @classmethod
    def warn(cls, msg, *arg):  # cls {{{1
        # type: (Text, Any) -> None
        pass


class This(object):  # {{{1
    '''keyword 'this' is the special keyword and will not be
        treat as well typed statement,
        so I did not recommend use 'this' in the transcrypt.

        I offen choice :code:`Event.target` and :code:`$(ev.target)`.
    '''
    pass


this = This()


class Window(object):  # {{{1
    def open(self, _id):  # {{{1
        # type: (Text) -> None
        pass

    @property
    def hash(self):  # prop {{{1
        # type: () -> Text
        return ""


window = Window()


class Document(object):  # {{{1
    def execCommand(self, cmd):  # cls {{{1
        # type: (Text) -> None
        pass


document = Document()


class History(object):  # {{{1
    def back(self):  # {{{1
        # type: () -> None
        pass

    def pushState(self, json, title, url):  # prop {{{1
        # type: (Any, Text, Text) -> None
        pass


history = History()


class Location(object):  # {{{1
    # {{{1
    @property
    def href(self):  # prop {{{1
        # type: () -> Text
        return ""

    @href.setter
    def href(self, url):
        # type: (Text) -> None
        pass

    @property
    def pathname(self):  # prop {{{1
        # type: () -> Text
        return ""

    @property
    def hash(self):  # prop {{{1
        # type: () -> Text
        return ""


location = Location()


class Element(object):  # {{{1
    pass


class SelectTag(Element):  # {{{1
    def __init__(self):
        # type: () -> None
        self.selectedIndex = 0


class Event(object):  # {{{1
    def __init__(self):  # {{{1
        # type: () -> None
        self.target = Element()


# vi: ft=python:fdm=marker
