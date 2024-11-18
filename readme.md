Tic-Tac-Toe Multiplayer Game (Local Network)

This is a simple two-player multiplayer Tic-Tac-Toe game that runs over a local network using Python’s socket library. Players can connect to the server, take turns to make moves, and the game will announce the winner or a draw.

Features

	•	Play Tic-Tac-Toe between two players on a local network.
	•	Players take turns to make moves.
	•	The game announces the winner or a draw when the game is over.
	•	Simple console-based UI for both server and client.

Requirements

	•	Python 3.x
	•	No external libraries are required beyond Python’s built-in libraries (socket, threading).

How to Run

1. Server (Host)

	•	The server listens for incoming player connections.
	•	Once two players have connected, it alternates between them, allowing each to make a move.

To start the server:
	1.	Clone the repository.
	2.	Navigate to the directory containing the server code.
	3.	Run the following command:

python server.py



2. Client (Player)

	•	The client connects to the server and takes turns to make a move.
	•	Each player will input their move in the form of a number from 1 to 9, corresponding to a cell on the Tic-Tac-Toe grid.

To start the client:
	1.	Clone the repository.
	2.	Navigate to the directory containing the client code.
	3.	Run the following command:

python client.py



Play the Game

	1.	The server will display the Tic-Tac-Toe board and prompt the first player to make a move.
	2.	The second player will then take their turn, and the game continues.
	3.	The game will announce the winner when a player has won, or indicate a draw if the board is full without a winner.

How the Game Works

	•	Board Representation: The board is represented as a list of 9 elements, where each element corresponds to a cell in the 3x3 Tic-Tac-Toe grid.
	•	Player Turns: The game alternates between Player ‘X’ and Player ‘O’. Each player inputs their move (a number between 1-9) to place their symbol on the grid.
	•	Victory Conditions: The game checks for a win after every move by verifying rows, columns, and diagonals for three matching symbols.
	•	Game Over: If a player wins or the board is full without a winner, the game ends.

Code Structure

	•	server.py: The server code that listens for incoming player connections, manages game logic, and alternates turns.
	•	client.py: The client code that allows players to connect to the server, input their moves, and interact with the game.


