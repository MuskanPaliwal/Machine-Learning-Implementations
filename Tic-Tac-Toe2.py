#!/usr/bin/env python3.4
class Board:
    """Represents one board to a Tic-Tac-Toe game."""

    def __init__(self):
        """Initializes a new board.
        A board is a dictionary which the key is the position in the board
        and the value can be 'X', 'O' or ' ' (representing an empty position
        in the board.)"""
        self.board =[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def print_board(self):
        """Prints the board."""
        print(" %c | %c | %c " % (self.board[1],self.board[2],self.board[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[4],self.board[5],self.board[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[7],self.board[8],self.board[9]))
        print("   |   |   ")

    def _is_valid_move(self, position):
        if self.board[position] is " ":
            return True
        return False

    def change_board(self, position, type):
        """Receive a position and if the player is 'X' or 'O'.
        Checks if the position is valid, modifies the board and returns the modified board.
        Returns None if the move is not valid."""
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

    def is_winner(self, player):
        """Returns True if the player won and False otherwise."""
        if self.board[1] == player.type and self.board[2] == player.type and self.board[3] == player.type or \
        self.board[4] == player.type and self.board[5] == player.type and self.board[6] == player.type or \
        self.board[7] == player.type and self.board[8] == player.type and self.board[9] == player.type or \
        self.board[1] == player.type and self.board[4] == player.type and self.board[7] == player.type or \
        self.board[2] == player.type and self.board[5] == player.type and self.board[8] == player.type or \
        self.board[3] == player.type and self.board[6] == player.type and self.board[9] == player.type or \
        self.board[1] == player.type and self.board[5] == player.type and self.board[9] == player.type or \
        self.board[7] == player.type and self.board[5] == player.type and self.board[3] == player.type:
            return True
        return False


class Player:
    """Represents one player."""
    def __init__(self, type):
        """Initializes a player with type 'X' or 'O'."""
        self.type = type
    def __str__(self):
        return "Player {}".format(self.type)


class Game:
    """Represents a Tic-Tac-Toe game.
    The game defines player 1 always playing with 'X'."""
    def __init__(self):
        """Initilize 2 Players and one Board."""
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()


    def printing_board(self):
        """Prints the board."""
        self.board.print_board()

    def change_turn(self, player):
        """Changes the player turn.
        Receives a player and returns the other."""
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        """Returns True if the player won the game, False otherwise."""
        return self.board.is_winner(player)

    def modify_board(self, position, type):
        """Receives position and player type ('X' or 'O').
        Returns modified board if position was valid.
        Asks to player try a different position otherwise."""
        if self.board.change_board(position, type) is not None:
            return self.board.change_board(position, type)
        else:
            position =int(input("Not available position. Please, try again: "))
            return self.board.change_board(position, type)


def play():
    game = Game()
    player = game.player1
    game.printing_board()
    num = 9
    while num > 0:
        num -= 1
        position =int(input("{} turn, what's your move? give your move from [1-9] ".format(player)))
        game.modify_board(position, player.type)
        game.printing_board()
        if game.won_game(player):
            print("{} is the Winner!".format(player))
            break
        else:
            player = game.change_turn(player)
    if num == 0:
        print("Game over! It's a tie!")


if __name__ == "__main__":
    play()
