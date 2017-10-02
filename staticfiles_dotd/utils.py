import sys
import functools


def render(filename):
    # A default render method
    with open(filename, 'rb') as f:
        return f.read()


def monkeypatch(new, modname, target):
    __import__(modname)
    module = sys.modules[modname]

    func = getattr(module, target)
    functools.update_wrapper(new, func)
    setattr(module, target, new)
