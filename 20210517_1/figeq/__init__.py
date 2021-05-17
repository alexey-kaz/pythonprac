import pyfiglet
def solve(a,b):
    f = pyfiglet.Figlet()
    if a == 0:
        return None
    return -b/a

def fig(res):
    f = pyfiglet.Figlet()
    if res is None:
        return f.renderText('NO ROOTS')
    return f.renderText('Root: {}'.format(res))
