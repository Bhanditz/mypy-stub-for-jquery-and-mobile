mypy stub files for transcrypt, jQuery and jQueryMobile combination
===============================================================================


Demonstration
----------------------
### running

```
  $ transcrypt test.py
  $ wget https://code.jquery.com/jquery-1.8.3.min.js
  $ python -m http.server &
  $ browser test.html
```


### mypy

```
  $ export MYPYPATH=stub
  $ mypy --strict test.py
```

or, edit test.py with vim ALE plugin.


.. vi: ft=markdown
