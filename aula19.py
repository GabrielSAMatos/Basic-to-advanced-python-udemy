sentence = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum'

i = 0
more_more = ['',0]
while i < len(sentence):
    if sentence[i] != ' ':
        letter = sentence[i]
        many_times = sentence.count(letter)
        more_times = letter, many_times
        if more_more[1] <= more_times[1]:
            more_more = more_times
    i += 1
print(f'The letter that appears most of the time is "{more_more[0]}" which appears {more_more[1]} times.')