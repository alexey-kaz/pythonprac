def sub(a,b):
    if hasattr(a,'__sub__') and hasattr(b,'__sub__'):
        return a-b
    return type(a)(i for i in a if i not in b)
