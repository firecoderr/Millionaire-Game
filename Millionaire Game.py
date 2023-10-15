# I avoid * imports most of the time
# Plus there's no sense importing the whole module if you only need one function from it
from random import sample

Questions = ['What is the capital of the United States of America? ',
             'Who is the current president of the United States of America? ',
             'What is the capital of Nigeria? ',
             'Muhammadu Buhari is the president of which country? ',
             'Uhuru Kenyatta is the president of which country? ',
             'What is the capital of France? ',
             'Which state has only one neighbor? ',
             'Where is Amsterdam located? ',
             'Emmanuel Macron is the president of which country? ',
             'Sir Alex Ferguson until his retirement coached which team? '
             ]

Answers = ['Washington DC',
           'President Donald Trump',
           'Abuja',  # <-- comma added
           'Nigeria',
           'Kenya',
           'Paris',
           'Maine',
           'Netherland',
           'France',
           'Manchester United'
           ]

num_right = 0

# Personal taste, I prefer the zipped list of Q & A rather than an index lookup in the for loop
# Ex: key[0] == ('What is the capital of the United States of America? ', 'Washington DC')
# Final note, the zip function returns a generator, so we need to transform it to a list object for sample()
key = list(zip(Questions, Answers))

# Sample from key now instead of Questions
s = sample(key, 4)

for i in s:
    # in each "i" tuple [0] is the question, [1] is the answer
    print(i[0])
    user_answer = input('Your Guess: ')
    if user_answer.lower() == i[1].lower():
        print('Correct!!!')
        num_right += 1
    else:
        print('Not Correct')
# Added a final fraction of correct statement
print('{}/4 Questions Correct'.format(num_right))



input();