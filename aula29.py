def salutation(salute):
    def with_name(name):
        return f'{salute}, {name}!'
    return with_name

good_morning = salutation('Good morning')
good_afternoon = salutation('Good afternoon')
good_night = salutation('Good night')

names = ['Gabriel', 'Joaquim', 'Fernadim']

for name in names:
    print(good_morning(name))
