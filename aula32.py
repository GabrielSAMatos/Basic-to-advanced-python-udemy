# Exercício - sistema de perguntas e respostas
quentions = [
    {
        'Question': 'How much is 2+2?',
        'Option': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5*5?',
        'Option': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10/2?',
        'Option': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]
count = 0 

for question in quentions:
    print(f'Question: {question['Question']}')
    print()

    options = question['Option']

    for op in range(len(options)):
        print(f'{op}) {question['Option'][op]}')
    print()
    
    ans = input('Choose an option: ')
    correct_answer = False
    
    if ans.isdigit():
        ans_int = int(ans)
        if ans_int >= 0 and ans_int < len(options):
            if options[ans_int] == question['Answer']:
                correct_answer = True

    if correct_answer:
        print('Congrats, You got it right! 🤓')
        print()
        count += 1
    else:
        print('Wrong answer 😭')
        print()
print(f'You got {count} out of {len(quentions)} questions right!')
