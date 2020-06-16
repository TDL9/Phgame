# tUtils.py - Utils written by TDL9
# Import this module as t

# import numpy as np
import functools as fn
import itertools as itt
import hy


# eval Hy expression
# see hy document for more details
hyc = hy.eval(hy.read_str("(comp hy.eval hy.read_str)"))

# functools.reduce(function, iterable[, initializer])
reduce = fn.reduce

# built-in function, filter(function, iterable) ~= (item for item in iterable if function(item))
filter = filter

# built-in function, map(function, iterable, ...)
map = map

# starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
starmap = itt.starmap

# product(p, q, … [repeat=1])
product = itt.product

# flatten ["foo" (, 1 2) [1 [2 3] 4] "bar"] => ['foo', 1, 2, 1, 2, 3, 4, 'bar']
flatten = hyc("flatten")

# return reversed iterator
reversed = reversed



# def call(func, para)

class Nothing():
    ''' 加法单位元, Nothing()+X => X
    '''
    def __add__(self, x):
        return x
    def __bool__(self):
        return False
    def __str__(self):
        return "nothing"
nothing = Nothing()

class Executable():
    def __init__(self, func, args, karg):
        self.func = func
        self.args = args
        self.karg = karg
    def exe(self):
        return self.func(*self.args, **self.karg)

def rgb(hexv):
    return ((hexv >> 16) & 0xFF, (hexv >> 8) & 0xFF, (hexv) & 0xFF)