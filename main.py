import random

board = ['-'] * 9

print("Rozpoczyna gracz komputerowy (krzyżyk).")

# Wyświetlanie tablicy
for i in range(0, 9, 3):
    print(" ".join(board[i:i + 3]))

player_symbol = 'O'
computer_symbol = 'X'

while True:
    # Ruch komputera
    empty_positions = [i + 1 for i in range(9) if board[i] == '-']
    computer_position = random.choice(empty_positions)
    board[computer_position - 1] = computer_symbol
    print("\nRuch komputera (krzyżyk) na pole", computer_position)

    # Wyświetlanie tablicy po ruchu komputera
    for i in range(0, 9, 3):
        print(" ".join(board[i:i + 3]))

    # Sprawdzanie zwycięzcy
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # poziomo
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # pionowo
                      (0, 4, 8), (2, 4, 6)]  # skos
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[
            condition[2]] != '-':
            if board[condition[0]] == computer_symbol:
                print("Przegrana!")
            else:
                print("Wygrana!")
            exit()

    if '-' not in board:
        print("Remis!")
        exit()

    # Ruch gracza
    while True:
        try:
            player_position = int(input("Twój ruch (wybierz pole 1-9): "))
            if player_position < 1 or player_position > 9 or board[
                player_position - 1] != '-':
                raise ValueError
            break
        except ValueError:
            print("Błąd! Wybierz wolne pole od 1 do 9.")

    board[player_position - 1] = player_symbol

    # Wyświetlanie tablicy po ruchu gracza
    for i in range(0, 9, 3):
        print(" ".join(board[i:i + 3]))

    # Sprawdzanie zwycięzcy po ruchu gracza
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # poziomo
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # pionowo
                      (0, 4, 8), (2, 4, 6)]  # skos
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[
            condition[2]] != '-':
            if board[condition[0]] == player_symbol:
                print("Wygrana!")
            else:
                print("Przegrana!")
            exit()

    if '-' not in board:
        print("Remis!")
        exit()
