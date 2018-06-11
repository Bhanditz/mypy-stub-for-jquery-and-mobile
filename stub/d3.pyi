from typing import (Any, Callable, Dict, List, Text, Union,
                    overload, )


if False:
    Any, Callable, Dict, List, Text


# Primitive Values
JsPrims = Union[bool, int, float, Text]


class D3obj(object):  # {{{1
    def selectAll(self, sel):  # {{{1
        # type: (Text) -> 'D3obj'
        ...

    # attr {{{1
    @overload
    def attr(self, attr, val):
        # type: (Text, JsPrims) -> 'D3obj'
        ...

    @overload
    def attr(self, attr, val):
        # type: (Text, 'D3obj') -> 'D3obj'
        ...

    @overload
    def attr(self, attr, fn):
        # type: (Text, Callable[[D3Point], JsPrims]) -> 'D3obj'
        ...

    # style {{{1
    @overload
    def style(self, attr, val):
        # type: (Text, Text) -> 'D3obj'
        ...

    @overload
    def style(self, attr, fn):
        # type: (Text, Callable[[D3Point], Text]) -> 'D3obj'
        ...

    def append(self, elname):  # {{{1
        # type: (Text) -> 'D3obj'
        ...

    # text {{{1
    @overload
    def text(self, val):
        # type: (Text) -> 'D3obj'
        ...

    @overload
    def text(self, fn):
        # type: (Callable[[D3Point], Text]) -> 'D3obj'
        ...

    def data(self, dat):  # {{{1
        # type: (List[Dict[Text, Any]]) -> 'D3obj'
        ...

    def datum(self, dat):  # {{{1
        # type: (List[Dict[Text, Any]]) -> 'D3obj'
        ...

    def call(self, chart):  # {{{1
        # type: (D3Chart) -> 'D3obj'
        ...

    def enter(self):  # {{{1
        # type: () -> 'D3obj'
        ...

    def outerRadius(self, rad):  # {{{1
        # type: (float) -> 'D3obj'
        ...   # split to D3arc

    def innerRadius(self, rad):  # {{{1
        # type: (float) -> 'D3obj'
        ...   # split to D3arc

    def centroid(self, v):  # {{{1
        # type: ('D3Point') -> Text
        ...   # split to D3arc


class D3Option(object):  # {{{1
    def enabled(self, onoff):  # {{{1
        # type: (bool) -> 'D3Option'
        ...


class D3Point(object):  # {{{1
    def __init__(self):  # {{{1
        # type: () -> None
        self.x = ...  # type: JsPrims
        self.value = ...  # type: JsPrims
        self.data = ...  # type: Dict[Text, JsPrims]

    def __getitem__(self, idx):  # {{{1
        # type: (int) -> JsPrims
        # for d[0], d[1] pattern.
        ...


class D3Axis(object):  # {{{1
    def tickFormat(self, fn):  # {{{1
        # type: (Callable[[JsPrims], Text]) -> 'D3Axis'
        ...


class D3Chart(object):  # {{{1
    def color(self, seq):  # {{{1
        # type: (D3Ordinal) -> 'D3Chart'
        ...

    def value(self, fn):  # {{{1
        # type: (Callable[[D3Point], JsPrims]) -> 'D3Chart'
        ...

    def x(self, fn):  # {{{1
        # type: (Callable[[D3Point], JsPrims]) -> 'D3Chart'
        ...

    def y(self, fn):  # {{{1
        # type: (Callable[[D3Point], JsPrims]) -> 'D3Chart'
        ...

    @property
    def xAxis(self):  # {{{1
        # type: () -> D3Axis
        ...

    @property
    def yAxis(self):  # {{{1
        # type: () -> D3Axis
        ...

    def __call__(self, dat):  # {{{1
        # type: (List[Dict[Text, Any]]) -> List[Dict[Text, Any]]
        ...

    # nvd3 {{{1
    def update(self):  # prop {{{1
        # type: () -> bool
        ...

    # multiBarChart {{{1
    def stacked(self, enabled):  # {{{1
        # type: (bool) -> 'D3Chart'
        ...

    def reduceXTicks(self, enabled):  # {{{1
        # type: (bool) -> 'D3Chart'
        ...

    def showControls(self, enabled):  # {{{1
        # type: (bool) -> 'D3Chart'
        ...

    def groupSpacing(self, spc):  # {{{1
        # type: (float) -> 'D3Chart'
        ...

    @property
    def tooltip(self):  # {{{1
        # type: () -> 'D3Option'
        ...

    # descreteBarChart {{{1
    def staggerLabels(self, enabled):  # {{{1
        # type: (bool) -> 'D3Chart'
        ...

    def showValues(self, enabled):  # {{{1
        # type: (bool) -> 'D3Chart'
        ...

    def duration(self, msec):  # {{{1
        # type: (int) -> 'D3Chart'
        ...

    def tooltips(self, enabled):  # {{{1
        # type: (bool) -> 'D3Chart'
        ...


class D3Ordinal(object):  # {{{1
    # range {{{1
    @overload
    def range(self, seq):  # {{{1
        # type: (List[Text]) -> 'D3Ordinal'
        ...

    @overload
    def range(self):  # {{{1
        # type: () -> 'D3Ordinal'
        ...

    def __call__(self, dat):  # {{{1
        # type: (JsPrims) -> Text
        ...


class Layout(object):  # {{{1
    def pie(self):  # {{{1
        # type: () -> D3Chart
        ...


layout = Layout()


class scale(object):  # {{{1
    # {{{1
    @classmethod
    def ordinal(cls):  # {{{1
        # type: () -> D3Ordinal
        ...

    @classmethod
    def category10(cls):  # {{{1
        # type: () -> D3Ordinal
        ...


class svg(object):  # {{{1
    @classmethod
    def arc(cls):  # {{{1
        # type: () -> D3obj
        ...


def csv(url,  # type: Text  # {{{1
        fn  # type: Callable[[Text, List[Dict[Text, JsPrims]]], bool]
        ):  # {{{1
    # type: (...) -> None
    ...


def format(src):  # {{{1
    # type: (Text) -> Callable[[JsPrims], Text]
    ...


def select(sel):  # {{{1
    # type: (Text) -> D3obj
    ...


def selectAll(sel):  # {{{1
    # type: (Text) -> D3obj
    ...


# end of file {{{1
# vi: ft=python:ts=4:et:fdm=marker:nowrap
