import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # Connect to the server

    while True:
        server_message = client.recv(1024).decode()
        print(server_message)

        if "Enter your move" in server_message:
            move = input("Your move: ")
            client.send(move.encode())

if __name__ == "__main__":
    main()