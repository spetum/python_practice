

## same name functions in other packages

from html import *
from glob import *

print(help(escape))

## 둘다 escape라는 함수가 있다.
'''
(1)
Help on function escape in module html:

escape(s, quote=True)
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (') characters are also
    translated.

None
(2)
Help on function escape in module glob:

escape(pathname)
    Escape all special characters.

None
'''
