# Write your code here
import random

msg_win = 'You survived!'
msg_lost = 'You lost!'

random.seed()

answers = ['python', 'java', 'swift', 'javascript']
answer = random.choice(answers)
hint = answer[:3] + "-" * len(answer[3:])

print('H A N G M A N')
print(f'Guess the word {hint}: > ')
guess = input()

if guess == answer:
    print(msg_win)
else:
    print(msg_lost)
