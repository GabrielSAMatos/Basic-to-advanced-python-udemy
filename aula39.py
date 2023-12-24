def generator(n=0):
    yield '1 pausa'
    print('Eita online')
    yield '2 pausa'


g = generator(n=0)

for i in g:
    print(i)