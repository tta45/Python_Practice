import chess
import chess.svg

def print_board(board):
    # Print the chess board to the console
    print(board)

def main():
    # Initialize the chess board
    board = chess.Board()

    # Game loop
    while not board.is_game_over():
        print_board(board)
        
        # Player's move
        move = input("Enter your move (e.g., e2e4): ")
        
        try:
            # Try to make the move
            move = chess.Move.from_uci(move)
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Invalid move. Try again.")
        except:
            print("Invalid move format. Use UCI format (e.g., e2e4).")

    # Print the final game result
    print("Game Over!")
    print("Result:", board.result())

if __name__ == "__main__":
    main()