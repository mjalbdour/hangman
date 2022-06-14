# Write your code here
import random

msg_win = 'You survived!'
msg_lost = 'You lost!'

random.seed()

answers = ['python', 'java', 'swift', 'javascript']
answer = random.choice(answers)

print('H A N G M A N')
print('Guess the word: > ')
guess = input()

if guess == answer:
    print(msg_win)
else:
    print(msg_lost)
