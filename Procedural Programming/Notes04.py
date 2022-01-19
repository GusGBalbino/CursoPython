#Dictionary in Python
'''
d1 = {1: 'key1 value'}
d1[2] = 'key2 value'

d2 = dict(key3="key3 value")

print(d1, d2)

'''
#----------------------------------------------------------------------------------------------------------#

'''
d1 = {
    'str': 'value',
    123: 'another value',
    (1, 2, 3, 4): 'Tuple',
}

# d1['nkey'] = 'Gus' - Create
# d1['str'] = 'String' - Att
# d1.update({'nkey': 'new_value'}) - Create with .update
# del d1['str'] - Delete key

if d1.get('nkey') is not None:
    print(d1.get('nkey'))

print('Continue...')
print(d1)
'''
#----------------------------------------------------------------------------------------------------------#

'''
clients = {
    'Client1': {
        'Name': 'Gus',
        'LastName': 'Gomes',
    },
    'Client2': {
        'Name': 'Robert',
        'LastName': 'Vergara',
    },
}

for clients_key, clients_values in clients.items():
    print(f'Showing {clients_key}:')
    for data_key, data_value in clients_values.items():
        print(f'\t{data_key} = {data_value}')
'''
#----------------------------------------------------------------------------------------------------------#

'''
#Questions with dict

questions = {
    'Question 1': {
        'question': 'How much is 2+2?',
        'answers': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'correct_answer': 'b',
    },
    'Question 2': {
        'question': 'What color is the sky?',
        'answers': {
            'a': 'Green',
            'b': 'Yellow',
            'c': 'Blue',
        },
        'correct_answer': 'c',
    },
}

correct_answers = 0
for question_key, question_value in questions.items():
    print(f'{question_key}: {question_value["question"]}')

    print('Choose the answer:')
    for answers_key, answers_value in question_value['answers'].items():
        print(f'[{answers_key}]: {answers_value}')

    answer_user = input('Your answer: ')

    if answer_user == question_value['correct_answer']:
        print('Right answer! Grats!')
        correct_answers += 1
    else:
        print('Wrong answer! Try again!')
    print()

qtd_questions = len(questions)
porc_right = (correct_answers / qtd_questions * 100)
print(f'Your hit percentage is: {porc_right}%')
'''
#----------------------------------------------------------------------------------------------------------#

'''
# Sets in python
# add, update, clear, discard
# union (|)
# intersection (&) (all elements)
# difference (-) (left elements only)
# symmetric_difference (^)

l1 = [1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 9]
print(l1)

l1 = set(l1)

print(l1)

l1 = list(l1)

print(l1)
'''
