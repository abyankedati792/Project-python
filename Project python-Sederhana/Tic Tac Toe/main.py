def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, player):
    
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("=== GAME TIC TAC TOE ===")
    print_board(board)

    while True:
        print(f"Pemain {current_player}'s giliran.")
        try:
            row = int(input("Masukkan baris (1-3): ")) - 1
            col = int(input("Masukkan kolom (1-3): ")) - 1
        except ValueError:
            print("Masukkan angka yang valid (1-3)!")
            continue

        if row not in range(3) or col not in range(3):
            print("Posisi tidak valid. Gunakan angka 1-3.")
            continue

        if board[row][col] != " ":
            print("Posisi sudah terisi. Pilih tempat lain.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Pemain {current_player} MENANG!")
            break
        elif is_draw(board):
            print("😐 Permainan SERI!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
