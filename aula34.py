list_ = [
    {'name':'Gabriel', 'surname':'Matos'},
    {'name':'José', 'surname':'AJosé'},
    {'name':'Gell', 'surname':'aMaluco'},
    {'name':'ALuana', 'surname':'BPiranha'},
    {'name':'BRelampago', 'surname':'CMarcos'},

]

def show(list):
    for i in list:
        print(i)
    print()

l1 = sorted(list_, key=lambda item:item['name'])
l2 = sorted(list_, key=lambda item:item['surname'])

show(l1)
show(l2)