"""
Module contains classes for tic tac toe view part
"""
import os
import sys



class View:
    """
    Class realize view part of MVC
    Methods
    -------
    draw(list):
        static method, draws game board
    make_turn(): tuple
        static method that realize player turn
        returns tuple with cell`s indexes

    """
    def __init__(self):
        self.model = None


    def set_model(self, model: "Model part"):
        """

        :type model: Model
        """
        self.model = model


    def draw_board(self):
        """
        Draws a game board according m_list
        :param m_list: list form Model class
        :return: None
        """
        os.system("clear")
        m_list = self.model.get_data()
        for i in range(0, 9, 3):
            item1 = m_list[i]
            item2 = m_list[i + 1]
            item3 = m_list[i + 2]

            print(f" {item1} | {item2} | {item3}")
            if i == 6:
                print("   |   |   ")
            else:
                print("___|___|___")


    def make_turn(self, name):
        """
        Method realize player turn
        :param name: str player that makes turn
        :return: tuple  with indexes of selected cell
        """
        print(f"Turn: {name}")

        while True:
            i = input("Enter the cell`s number, "
                      "Numeration starts from a left top cell,\n"
                      "Use a digits only: ")
            if i.isdigit() and 1 <= int(i) <= 9 and self.model.is_free(int(i)-1):
                return int(i)-1
            print("Error, input correct cell`s number")



    def run(self):
        """
        Method draws main menu and returns picked number
        """
        actions = {1: self.play_human_vs_human,
                   2: self.play_human_vs_cpu,
                   3: self.show_winner_table,
                   4: self.clear_winner_table,
                   5: self.exit_game}
        while True:
            os.system("clear")
            self.model.clear_board()
            print("'1' - to start game")
            print("'2' - to start vs CPU")
            print("'3' - to see winners table")
            print("'4' - to clear winners table")
            print("'5' - to exit")
            try:
                menu_choice = int(input())
            except ValueError:
                continue
            if not 1 <= menu_choice <= 5:
                continue
            actions[menu_choice]()

    def show_winner_table(self):
        """Method shows log.txt with winner table"""
        with open(self.model.get_log_name()) as log:
            os.system("clear")
            lines = log.readlines()
            if lines:
                for line in lines:
                    print(line.rstrip())
            else:
                print("Winner table is empty")
        input("Press enter to return the menu")
        return self.draw_menu()

    def clear_winner_table(self):
        """Method clears log.txt"""
        with open(self.model.get_log_name(), "w") as log:
            log.truncate(0)
        input("Press enter to return the menu")
        return self.draw_menu()

    @staticmethod
    def exit_game():
        """Exit game"""
        sys.exit(0)

    def ask_name(self):
        """Method ask about players names and return its"""
        print("Enter first player name: ")
        name1 = input()
        print("Enter second player name: ")
        name2 = input()
        self.model.set_players_name(name1, name2)

    @staticmethod
    def play_again():
        """
        Method prints dialog after end of game and return answer
        :return: int
        """
        while True:
            print("Play again for revenge?")
            print("1 - plays")
            print("0 - exit to menu")
            try:
                i = int(input())
                if i in (0, 1):
                    return i
            except ValueError:
                continue

    def play_human_vs_human(self):
        """Method runs a game in human vs human mode"""
        self.ask_name()
        i = 1
        players = self.model.get_players()
        while True:
            i = (i + 1) % 2
            os.system("clear")
            self.draw_board()
            player_turn = self.make_turn(players[i][1])
            self.model.update_board(player_turn,players[i][0])
            self.draw_board()
            if self.model.is_winner(players[i][0], self.model.get_data()):
                print(f"{players[i][1]} is winner")
                answer = self.play_again()
                if answer == 1:
                    players[i][2] += 1
                    self.model.clear_board()
                elif players[0][2] > 0 or players[1][2] > 0:
                    self.model.logger.info(f"{players[0][1]}: {players[0][2]} "
                                           f"{players[1][1]}: {players[1][2]}")
                    for player in players:
                        player[2] = 0
                    self.model.clear_board()
                    break
                else:
                    self.model.logger.info(f"{players[i][1]} wins")
                    break
            elif self.model.is_draw():
                print("Draw")
                answer = self.play_again()
                if answer == 0:
                    self.model.logger.info(f"{players[0][1]} and "
                                           f"{players[1][1]} result: Draw")
                    break


    def ask_human_name_and_char(self):
        """Ask player name for human vs cpu mode"""
        name1 = input("Enter first player name: ")
        while True:
            os.system("clear")
            char = input("Chose your side: X or 0")
            if char.upper() in ("X", "O", "0"):
                if char.upper() == "X":
                    self.model.set_cpu_and_human_players((name1, "X"), ("CPU", "0"))
                    return

                self.model.set_cpu_and_human_players((name1, "0"), ("CPU", "X"))
                return


    def play_human_vs_cpu(self):
        """Method starts human vs cpu mode"""
        self.ask_human_name_and_char()
        players = self.model.get_cpu_and_human_players()
        if players[0][0] == "X":
            i = 1
        else:
            i = 0
        while True:
            i = (i + 1) % 2
            os.system("clear")
            self.draw_board()
            if players[i][1] =="CPU":
                player_turn = self.model.minimax_turn()
            else:
                player_turn = self.make_turn(players[i][1])
            self.model.update_board(player_turn, players[i][0])
            self.draw_board()
            if self.model.is_winner(players[i][0], self.model.get_data()):
                print(f"{players[i][1]} is winner")
                answer = self.play_again()
                if answer == 1:
                    players[i][2] += 1
                    self.model.clear_board()
                elif players[0][2] > 0 or players[1][2] > 0:
                    self.model.logger.info(f"{players[0][1]}: {players[0][2]} "
                                           f"{players[1][1]}: {players[1][2]}")
                    for player in players:
                        player[2] = 0
                    self.model.clear_board()
                    break
                self.model.logger.info(f"{players[i][1]} wins")
                self.model.clear_board()
                break
            elif self.model.is_draw():
                print("Draw")
                answer = self.play_again()
                if answer == 0:
                    self.model.logger.info(f"{players[0][1]} and "
                                           f"{players[1][1]} result: Draw")
                    self.model.clear_board()
                    break
                self.model.clear_board()
