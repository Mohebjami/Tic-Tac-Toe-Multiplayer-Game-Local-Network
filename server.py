import socket
import threading

# Game Board
board = [' '] * 9
current_player = 'X'

# Function to print the board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

# Check for a win or draw
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return ' ' not in board

# Handle a player's connection
def handle_client(client_socket, addr):
    global current_player
    client_socket.send(f"You are Player {current_player}.\n".encode())
    player = current_player
    current_player = 'O' if current_player == 'X' else 'X'

    while True:
        print_board()
        client_socket.send(f"Current Board:\n{''.join(board)}\n".encode())
        client_socket.send("Enter your move (1-9): ".encode())
        move = int(client_socket.recv(1024).decode()) - 1

        if board[move] == ' ':
            board[move] = player
            if check_winner():
                print_board()
                client_socket.send("You win!\n".encode())
                client_socket.close()
                break
        else:
            client_socket.send("Invalid move. Try again.\n".encode())

# Main server setup
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(2)
    print("Server started. Waiting for players...")

    while True:
        client_socket, addr = server.accept()
        print(f"Player connected from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    main()