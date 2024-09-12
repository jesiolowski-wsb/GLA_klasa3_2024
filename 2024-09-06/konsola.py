while True:
    komenda = input("> ")  # Oczekujemy na wpisanie komendy

    if komenda.lower() == "quit":
        print("Konsola zostaje zamknięta.")
        break  # Zakończ pętlę, jeśli wpisano "quit"
    else:
        print(f"Wpisałeś: {komenda}")  # Wykonaj operacje na komendzie
