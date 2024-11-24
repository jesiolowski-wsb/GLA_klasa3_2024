from random import randrange
with open("popular.txt", "r") as file:
    # rozumiem że w kolejnych liniach losujesz słowo
    # takie rozwiązanie sprytne i mega kreatywne, ale ma kilka wad:
    # 1. musimy znać granice pliku
    # 2. W zasadzie pewnym jest ze ustawimy wskaznik w polowie slowa
    # 3. wiec uzywamy readline() tylko po to aby przeniesc wskaznik do nowej 'pełnej' linii
    file.seek(randrange(1, 185189))
    file.readline()
    original_answer = list(file.readline().strip())

    # Jak myslisz, czy nie byloby czytelniej tak:
    # lines = file.readlines()
    # original_answer = list(random.choice(lines).strip())

    # a alternatywnie (jesli plik wejsciowy bylby baaaaardzo duzy):
    # mozna by z calego pliku wziac tylko jedna losowa linie - nie byloby potrzeby wczytywania
    # calego pliku do pamieci - performance idzie w gore:)
    #     chosen_line = random.choice(file.readlines()).strip()
lives = 7
win_status = False
active_answer = ["_"]*len(original_answer)
print("".join(active_answer))
print("Lives:", lives)
while True:
    guess = input("Zgadnij literę lub słowo: ")

    # tutaj można by dodać obsługę tylko znaków alfanumerycznych (sprawdz 'xxx'.isalpha())

    if len(guess) > 1:
        if list(guess) == original_answer:
            active_answer = original_answer

        else:
            lives -= 1

    elif len(guess) == 1:

        if original_answer.count(guess) > 0 and active_answer.count(guess) == 0:
            # fajne rozwiazanie, wiec tylko jako sugestia do rozważenia
            # correct_guesses = set()
            # wrong_guesses = set()
            # if guess in correct_guesses or guess in wrong_guesses:
            # print("Już zgadłeś tę literę!")

            locations = [index for index in range(len(original_answer)) if original_answer[index] == guess]
            for index in locations:
                active_answer[index] = guess

            '''counter = original_answer.count(guess)
            print(counter)
            start_counting = 0
            while counter > 0:
                print(counter)
                active_answer[original_answer[start_counting:].index(guess)] = guess
                start_counting = original_answer[start_counting:].index(guess)
                counter -= 1'''
        else: lives -= 1

    print("".join(active_answer))
    print("Lives:", lives)
    if active_answer == original_answer:
        win_status = True
        break
    if lives < 1:
        win_status = False
        break
if win_status: print("You won!")
else: print("You lost!\nThe answer was:", "".join(original_answer))