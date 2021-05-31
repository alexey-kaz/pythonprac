import gettext
import os

import pyfiglet

gettext.install("fig", os.path.dirname(__file__), names=("ngettext",))


def solve(a, b):
    if a == 0:
        return None
    return -b / a


def fig(res):
    if res is None:
        root = _('NO ROOTS')
    else:
        root = _('Root: ')
        root += str(res)
    f = pyfiglet.Figlet(font="banner")
    return f.renderText(root)
