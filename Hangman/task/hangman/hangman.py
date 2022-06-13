# Write your code here
print('H A N G M A N')

answer = 'python'
msg_win = 'You survived!'
msg_lost = 'You lost!'

print('Guess the word: > ')
guess = input()

if guess == answer:
    print(msg_win)
else:
    print(msg_lost)
