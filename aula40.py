def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen
    yield 4
    yield 5
    yield 6

def gen3():
    yield 7
    yield 8
    yield 9

g = gen2(gen3())
for n in g:
    print(n)