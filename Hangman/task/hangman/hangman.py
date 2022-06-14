# Write your code here
import random


def replace_with_letter(word, guess_word, l):
    for i, c in enumerate(word):
        if c == l:
            if i < len(word) - 1:
                guess_word = guess_word[:i] + l + guess_word[i + 1:]
            else:
                guess_word = guess_word[:i] + l

    return guess_word


random.seed()

title_game = 'H A N G M A N'
msg_win = 'You survived!'
msg_lost = 'You lost!'
msg_letter_prompt = 'Input a letter: '
msg_letter_doesnt_appear = "That letter doesn't appear in the word."
msg_thanks = "Thanks for playing!"

attempts = 8

answers = ['python', 'java', 'swift', 'javascript']
answer = random.choice(answers)
answer_set = set(answer)

guess = "-" * len(answer)
guess_set = set()

print(title_game, " #", attempts, "attempts\n")
while attempts > 0:
    if guess_set == answer_set:
        break

    print(guess)
    print(msg_letter_prompt)
    letter = input()
    attempts -= 1

    if letter not in answer_set:
        print(msg_letter_doesnt_appear, "  #", attempts)
    else:
        guess_set.add(letter)
        guess = replace_with_letter(answer, guess, letter)

print(msg_thanks)
