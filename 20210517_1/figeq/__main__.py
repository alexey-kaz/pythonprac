import gettext
import os

from . import solve, fig

gettext.install("fig", os.path.dirname(__file__), names=("ngettext",))

a, b = map(float, input(_("input a, b: ")).split())
print(fig(solve(a, b)))
