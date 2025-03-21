## Walidacja ruchu postaci na planszy (gra turowa)
<div><p>Hipotetyczna gra turowa ze statkiem poruszającym się w określony sposób. Siatka / plansza zawiera wartości <em>True</em> jeśli na pozycji znajduje się woda oraz <em>False</em> jeśli na pozycji znajduje się suchy ląd.</p>
<p>Gracz kontroluje łódź w ściśle określonny sposób. Jednostka może poruszać się po planszy jedynie po linii prostej i o określoną ilość pól (w zależności od kierunku w którym obecnie zwraca się dziób łodzi)</p>
<p>
<img width="297" alt="image" src="https://github.com/jesiolowski-wsb/GLA_klasa3_2023/assets/67168776/7968d6d7-650f-4148-9157-04ace31a433b">

</p>
<p>Jednostka może poruszać się tylko po wodzie, tak więc przeszkoda typu wysepka / inna wariacja nt. suchego lądu blokuje możliwośc poruszania się - statek nie może się tam przemieścić.</p>
<p>Stwórz funkcję <em>can_travel_to</em>, która będzie sprawdzać czy cel podróży łodzi jest dla gracza osiągalny. Funkcja powinna zwracać <em>True </em>dla celów osiągalnych w oparciu o wzorzec przemieszczania się, oraz <em>False </em>dla pól nieosiągalnych / zablokowanych / poza zakresem poruszania się / poza planszą</p>
<p>Jako przykład, kod poniżej:</p>
<pre><code class="language-python hljs">gameMatrix = [
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
    [<span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
    [<span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
]

<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment"># True, ruch jest dopuszczalny</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>)) <span class="hljs-comment"># False, nie można przepłynąć przez ląd</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">3</span>)) <span class="hljs-comment"># False, nie można przepłynąć przez ląd</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>)) <span class="hljs-comment"># False, nie można przepłynąć przez ląd + zbyt daleko</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">6</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment"># False, poza dopuszczalnym zakresem</span></code></pre>

<p>Obrazek poniżej ilustruje wszystkie dopuszczalne ruchy wynikające ze statku na pozycji (3, 2):</p>

<p><img width="297" alt="image" src="https://github.com/jesiolowski-wsb/GLA_klasa3_2023/assets/67168776/e408e14c-7198-4f28-a5b5-90e02b4cd48f">
</p></div>


Odpowiedzi poproszę wrzucić do bieżącego folderu jako pliki nazwane imieniem i nazwiskiem

# Propozycja rozwiązania
```python
def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    allowed_offset = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 2)]

    for idy, row in enumerate(game_matrix):
        if from_row == idy:

            for idx, column in enumerate(row):
                if from_column == idx:
                    # print('\ngoing from', (idy, idx))
                    # print('going to:', (to_row, to_column))

                    distance = (to_row - idy, to_column - idx)
                    if distance in allowed_offset and game_matrix[to_row][to_column]:  # && if target tile is true (water)
                        # print(f"distance {distance} is allowed")
                        # print("destination", (to_row, to_column), "is as:", game_matrix[to_row][to_column])

                        # check for distant distance
                        isYDistant = abs(to_row - idy) > 1
                        isXDistant = abs(to_column - idx) > 1
                        if isYDistant:
                            # print(f"distant destination ({abs(to_row - idy)} fields), iterating down along the route")
                            for current_row in range(to_row - 1, idy, -1):
                                if not game_matrix[current_row][to_column]:
                                    return False
                        if isXDistant:
                            # print(f"distant destination ({abs(to_column - idx)} fields), iterating down along the route")
                            for current_column in range(to_column - 1, idx, -1):
                                if not game_matrix[to_row][current_column]:
                                    return False
                    else:
                        return False
    return True


gameMatrix = [
    [False, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, True],

     # [False, True, True, True, True, True],
    # zmiana 'wody' na 'ziemie' na pozycji 3
     [False, True, True, False, True, True],

    [False, True, True, True, False, True],
    [False, False, False, False, False, False],
]

print("->", can_travel_to(gameMatrix, 3, 2, 2, 2))  # True, Valid move
print("->", can_travel_to(gameMatrix, 3, 2, 3, 4))  # False, Can't travel through land
print("->", can_travel_to(gameMatrix, 3, 2, 3, 3))  # False, Can't travel through land
print("->", can_travel_to(gameMatrix, 3, 2, 3, 5))  # False, Can't travel through land + too far away
print("->", can_travel_to(gameMatrix, 3, 2, 6, 2))  # False, Out of bounds

```
