from urllib.request import urlopen
from random import randrange
from os.path import isfile


if not isfile('./popular.txt'):
    with urlopen( 'https://raw.githubusercontent.com/dolph/dictionary/refs/heads/master/popular.txt' ) as webpage:
        content = webpage.read().decode()
    with open('popular.txt', 'w') as output:
        output.write(content)

with open("popular.txt", "r") as file:
    file.seek(randrange(1, 185189))
    file.readline()
    original_answer = list(file.readline().strip())

guessed_words = []
lives = 7
win_status = False
active_answer = ["_"]*len(original_answer)


print("".join(active_answer))
print("Lives:", lives)


while True:
    guess = input("Zgadnij literę lub słowo: ").lower()

    if len(guess) > 1:
        if list(guess) == original_answer:
            active_answer = original_answer

        else:
            lives -= 1

    elif len(guess) == 1:
        if guess not in guessed_words: guessed_words.append(guess)
        if guess in original_answer and guess not in active_answer:
            locations = [index for index in range(len(original_answer)) if original_answer[index] == guess]
            for index in locations:
                active_answer[index] = guess

        else: lives -= 1

    print("".join(active_answer))
    print("Lives:", lives)
    print(f"Guessed words: {", ".join(guessed_words)}")

    if active_answer == original_answer:
        win_status = True
        break

    if lives < 1:
        win_status = False
        break

if win_status: print("You won!")
else: print("You lost!\nThe answer was:", "".join(original_answer))
