person = {
    'name': 'Gabriel Sousa de Abreu',
    'surname': 'Matos',
    'age': 24,
    'height': 1.75,
    'address':[
        {'road': 'Cidade Ecologica', 'number': 420},
        {'road': 'Visconde de Maua', 'number': 662},
    ],
}

#print(list(person.items()))  

dont_exist = 'Dont exist'

print(person.get('hair_cut', dont_exist))