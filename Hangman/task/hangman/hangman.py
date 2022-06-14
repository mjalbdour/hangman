# Write your code here
import random


def replace_with_letter(word, guess_word, letter_):
    for i, c in enumerate(word):
        if c == letter_:
            if i < len(word) - 1:
                guess_word = guess_word[:i] + letter_ + guess_word[i + 1:]
            else:
                guess_word = guess_word[:i] + letter_

    return guess_word


random.seed()

title_game = 'H A N G M A N'
msg_win = 'You survived!'
msg_lost = 'You lost!'
msg_letter_prompt = 'Input a letter: '
msg_letter_doesnt_appear = "That letter doesn't appear in the word."
msg_no_improvements = "No Improvements."
msg_guessed = "You guessed the word"
msg_single_letter = "Please, input a single letter."
msg_lowercase_letter = "Please, enter a lowercase letter from the English alphabet."
msg_already_guessed = "You've already guessed this letter."
# msg_thanks = "Thanks for playing!"

attempts = 8

answers = ['python', 'java', 'swift', 'javascript']
answer = random.choice(answers)
answer_set = set(answer)

guess = "-" * len(answer)
guess_set = set()
inputs = set()

print(title_game, " #", attempts, "attempts\n")
while attempts > 0:
    if guess_set == answer_set:
        print(f'{msg_guessed} {answer}!')
        print(msg_win)
        break

    print(guess)
    print(msg_letter_prompt)
    letter = input()

    if len(letter) != 1:
        print(msg_single_letter)
        continue

    if not letter.isalpha() or not letter.islower():
        print(msg_lowercase_letter)
        continue

    if letter in inputs:
        print(msg_already_guessed)
        continue

    inputs.add(letter)

    if letter in guess_set:
        print(msg_no_improvements, "  #", attempts, 'attempts')
    elif letter not in answer_set:
        print(msg_letter_doesnt_appear, "  #", attempts, 'attempts')
    else:
        guess_set.add(letter)
        guess = replace_with_letter(answer, guess, letter)
        continue

    attempts -= 1
else:
    print(msg_lost)
