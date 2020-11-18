#!/usr/bin/env python3
'''
'''

import sys
import os
from os.path import basename as bname
import re
from tempfile import NamedTemporaryFile as tempf
from subprocess import run
import atexit
from difflib import unified_diff
from tkinter.filedialog import askopenfilename
import filecmp

try:
    from pygments.lexers import DiffLexer
    from pygments.formatters import TerminalFormatter
    from pygments import highlight
except ModuleNotFoundError:
    highlight = DiffLexer = TerminalFormatter = None

# tests location guesser
#   test dirs (input/output)
#   numbering scheme
# program location guesser
# one test runner
#  test type
#  test options
# test statistics

TestDirs = ".", "test", "tests", "data", "check"
TestIn = "in", "input", "dat", "data"
TestOut = "out", "output", "res", "result"
rePatt = r"\d+.*{}", r"{}.*?\d+"
reProj = r"\d{8}_\d+"
reProg = r"[.]py$"
ProgN = "prog proj solution task"
TMOUT = 5
MAXDIFF = 10240

_ToDelete = []


def _todelete():
    for f in _ToDelete:
        if os.path.isfile(f.name):
            f.close()
            os.remove(f.name)


atexit.register(_todelete)


def rp(d, f):
    return os.path.realpath(os.path.join(d, f))


def guess_tests(curdir=".", testdir=TestDirs, inext=TestIn, outext=TestOut):
    if type(testdir) is str:
        testdir = (testdir,)
    if type(inext) is str:
        inext = (inext,)
    if type(outext) is str:
        outext = (outext,)

    if type(testdir) is not list:
        dirs = list(testdir)
        dirs += [os.path.join("..", d) for d in testdir if d != "."]

    if type(inext) is not list:
        ins = [(patt.format(p), p) for p in inext for patt in rePatt]

    pairs = []
    for d in dirs:
        D = rp(curdir, d)
        if not os.path.isdir(D):
            continue
        files = os.listdir(D)
        for In, Ext in ins:
            r = [G.group() for f in files if (G := re.search(In, f))]
            for OExt in outext:
                io = [(i, o) for i in r if os.path.isfile(rp(D, o := i.replace(Ext, OExt)))]
                if len(pairs) < len(io):
                    pairs = [(rp(D, i), rp(D, o)) for i, o in io]
    return pairs


def guess_program(curdir=".", date="", num=""):
    if not os.path.isdir(curdir):
        return None
    if curdir.endswith("/") or re.search(reProj, os.path.realpath(curdir)):
        D = os.path.realpath(curdir)
    else:
        reD = f"{date}.*{num}"
        for d in sorted(os.listdir(curdir), reverse=True):
            D = rp(curdir, d)
            if os.path.isdir(D) and re.search(reProj, d) and re.match(reD, d):
                break
        else:
            return None

    progs = [rp(D, f) for f in os.listdir(D) if re.search(reProg, f) and os.path.isfile(rp(D, f))]
    if len(progs) == 0:
        return None
    if len(progs) == 1:
        return progs[0]

    def skey(fname):
        return f"{ProgN.find(re.sub(reProg, '', bname(fname), re.I)):06d}{os.path.getsize(fname):08x}".replace("-", "!")

    return sorted(progs, key=skey)[-1]


def py_runner(prog, infile):
    # print(f"Generate {prog} < {infile}")
    with open(infile) as fIn, tempf(prefix=bname(infile) + ".", delete=False) as fOut:
        _ToDelete.append(fOut)
        res = run([sys.executable, prog], stdin=fIn, stdout=fOut, timeout=TMOUT)
    return fOut.name


def txt_diff(out, std):
    # print(f"Compare text outputs: {out} {std}")
    if filecmp.cmp(out, std):
        return None
    outS, stdS = os.path.getsize(out), os.path.getsize(std)
    if outS > MAXDIFF or stdS > MAXDIFF:
        outT, stdT = [f"Size: {outS}\n", "Differs from {bname(std)}\n"], [f"Size: {stdS}"]
    else:
        with open(out) as fOut, open(std) as fStd:
            outT, stdT = fOut.readlines(), fStd.readlines()
    return unified_diff(outT, stdT, bname(out), bname(std))



def suite(prog, inout):
    succ, errs = [], []
    for In, Std in sorted(inout):
        # Determine runner
        Out = py_runner(prog, In)
        # Determine checker
        res = txt_diff(Out, Std)
        if res:
            # display diff
            errs.append((In, res))
        else:
            succ.append(In)
    return succ, errs


def run_tests(curdir="."):
    fd = os.path.realpath(curdir)
    if os.path.isfile(fd):
        prog = fd
        curdir = os.path.dirname(prog)
    elif not (prog := guess_program(fd)):
        return [], [(f"Cannot guess program from {curdir}", [])]
    if not (tests := guess_tests(fd)):
        return [], [(f"Cannot guess tests from {curdir}", [])]

    passed, failed = suite(prog, tests)
    if failed:
        for name, diff in failed:
            print(f"\t### {bname(name)} ###")
            if all((os.isatty(1), highlight, DiffLexer, TerminalFormatter)):
                print(highlight("".join(diff), DiffLexer(), TerminalFormatter()))
            else:
                sys.stdout.writelines(diff)
            print()
    return passed, failed


if __name__ == "__main__":
    cwd = os.getcwd()
    ex = 0

    wait = "-" in sys.argv
    if wait:
        sys.argv.remove("-")

    if len(sys.argv) < 2:
        td = askopenfilename(filetypes=[("python files", "*.py")])
    else:
        td = sys.argv[1]
    passed, failed = run_tests(td)
    if passed:
        print("Tests passed:", *map(bname, passed))
    if failed:
        print("Tests failed:", *map(bname, (e for e, d in failed)))
        ex = 2

    if wait:
        print("Generated files:", *(f.name for f in _ToDelete), sep="\n")
        input("\nPress any key…")

    sys.exit(ex)
