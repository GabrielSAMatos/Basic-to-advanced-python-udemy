list_ = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'name': 'Gabriel'}
]

for item in list_:
    if isinstance(item, int):
        print(item, isinstance(item, int))
