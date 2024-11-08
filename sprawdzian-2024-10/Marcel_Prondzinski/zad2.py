# Zdobyte punkty: 5/5

with open("tekst.txt", "r") as file:
    content = file.read()

words = [word for word in content.split() if len(word) > 3 and word[0].isupper()]
with open("analiza.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
