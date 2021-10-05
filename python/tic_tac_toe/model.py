"""
Module contains classes for tic tac toe  model part
"""
import logging as lg
import sys


class Model:
    """
    Class implements model for MVC

    Attributes
    ----------
    board_size: int
        stores size of board
    game_board: list
        square matrix that stores all data about game situation
        contains X or O in cells or ' '

    Methods
    ------
    get_data(): list
        returns game_board list
    update_board(i: int, j: int, char: str)
        puts char in game_board[i][g]
    """

    def __init__(self, ):
        self._game_board = [" " for _ in range(3 ** 2)]
        self.player1 = ["X", " ", 0]
        self.player2 = ["0", " ", 0]
        self.hu_player = []
        self.ai_player = []
        self.log_name = "game.log"
        logger = lg.getLogger("game_log")
        logger.setLevel(lg.INFO)
        f_logger = lg.FileHandler("game.log")
        f_formatter = lg.Formatter("%(asctime)s: %(message)s ",
                                   "%Y-%m-%d  %H:%M:%S")
        f_logger.setFormatter(f_formatter)
        logger.addHandler(f_logger)
        self.logger = logger
        with open("game.log", "a") as file:
            file.close()

    def get_log_name(self):
        """Returns a name of log.txt"""
        return self.log_name

    def get_data(self):
        """
        Returns game_board
        :return: list
        """
        return self._game_board

    def update_board(self, i: int, char: str):
        """
        Updates game_board list
        :param i: int, index of line
        :param char: X, or O
        :return: None
        """
        self._game_board[i] = char

    def set_cpu_and_human_players(self, hu_player, ai_player):
        """Set ai and human players"""
        self.hu_player.append(hu_player[1])
        self.hu_player.append(hu_player[0])
        self.hu_player.append(0)
        self.ai_player.append(ai_player[1])
        self.ai_player.append(ai_player[0])
        self.ai_player.append(0)

    def get_cpu_and_human_players(self):
        """Return ai and human players"""
        return self.hu_player, self.ai_player

    def clear_board(self):
        """
        Method clears inner list
        :return: None
        """
        self._game_board = [" " for _ in range(3 ** 2)]

    def clear_players(self):
        """Reset players data"""
        self.player1 = ["X", " ", 0]
        self.player2 = ["0", " ", 0]
        self.hu_player = []
        self.ai_player = []

    def is_free(self, i: str):
        """
        Method checks that selected cell is free
        :param i: index of cell
        :return: bool
        """
        if self._game_board[i] == " ":
            return True
        return False

    @property
    def available_turns(self):
        """
        Property that returns count of available turns
        :return: int
        """
        return self._game_board.count(" ")


    @staticmethod
    def is_winner(char: str, board) -> bool:
        """Checks winner """
        tmp_ls = board
        if tmp_ls[0] == tmp_ls[3] == tmp_ls[6] == char or \
                tmp_ls[1] == tmp_ls[4] == tmp_ls[7] == char or \
                tmp_ls[2] == tmp_ls[5] == tmp_ls[8] == char or \
                tmp_ls[0] == tmp_ls[1] == tmp_ls[2] == char or \
                tmp_ls[3] == tmp_ls[4] == tmp_ls[5] == char or \
                tmp_ls[6] == tmp_ls[7] == tmp_ls[8] == char or \
                tmp_ls[0] == tmp_ls[4] == tmp_ls[8] == char or \
                tmp_ls[2] == tmp_ls[4] == tmp_ls[6] == char:
            return True
        return False

    def set_players_name(self, name1, name2):
        """Set both human players"""
        self.player1[1] = name1
        self.player2[1] = name2

    def get_players(self):
        """Get both human players"""
        return self.player1, self.player2

    def is_draw(self):
        """Checks draw ending"""
        return not self.available_turns

    def minimax(self, new_board, depth, is_maximazing):
        """Minimax function for ai opponent"""
        if self.is_winner(self.ai_player[0], new_board):
            return 10
        if self.is_winner(self.hu_player[0], new_board):
            return -10
        if self.is_draw():
            return 0

        if is_maximazing:
            best_score = -sys.maxsize
            for i in range(9):
                if new_board[i] == " ":
                    new_board[i] = self.ai_player[0]
                    score = self.minimax(new_board, depth + 1, False)
                    new_board[i] = " "
                    best_score = max(best_score, score)
        else:
            best_score = sys.maxsize
            for i in range(9):
                if new_board[i] == " ":
                    new_board[i] = self.hu_player[0]
                    score = self.minimax(new_board, depth + 1, True)
                    new_board[i] = " "
                    best_score = min(best_score, score)
        return best_score

    def minimax_turn(self):
        """Method returns best move for ai payer"""
        best_score = -sys.maxsize
        move = None
        new_board = self._game_board

        for i in range(9):
            if new_board[i] == " ":
                new_board[i] = self.ai_player[0]
                score = self.minimax(new_board, 0, False)
                new_board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move
