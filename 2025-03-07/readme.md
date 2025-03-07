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


Odpowiedzi jak zwykle poproszę wrzucić do bieżącego folderu jako pliki nazwane imieniem i nazwiskiem
