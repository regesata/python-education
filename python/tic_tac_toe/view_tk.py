"""
Module implements view part for game
uses tkinter library
"""
import sys
import tkinter
from tkinter import simpledialog
from tkinter import messagebox as mb


class View:
    """
    Class implements GUI using tkinter

    Methods
    -------
    _set_up_window()
        setups window properties
    _add_buttons()
        adds buttons for game board
    _add_menu()
        adds buttons of main menu and adds command to they
    _ask_name()
        shows dialog window and ask player name
        :return str
    _ask_char()
        asks player character for human vs cpu mode
        :return str
    _disable_menu()
        disables main menu buttons
    _enable_menu()
        enables main menu buttons and change label text to Welcome
    _enable_game_board()
        enables game board buttons and clears they text
    _disable_game_board()
        disables game board buttons
    set model(model: Model)
        sets instance of model
    human_vs_human()
        runs game in human vs human mode, asks players names and enables board
    human_vs_cpu()
        runs game in human vs cpu mode, asks player name an character for game
        if character is 0 cpu makes firs turn on its own
    _play_again()
        shows dialog window and asks for game continue
    add_callback(b: Button, func: "function")
        sets a callback function for  game board buttons

    _button_click(control: Button)
        callback function for game board buttons, has a button instance that clicked  as argument

    show_table()
        command for main menu button that shows table of winners from game.log file,
        shows file content in new window

    clear_table()
        command for main menu button that clears table of winners from game.log file

    exit_game()
          command for main menu button that closes application

    Attributes
    ----------
    root: tkinter.Tk main window
    buttons: list list of game board buttons
    menu_buttons: list list of main manu buttons
    model_part: Model instance of Model
    is_cpu_game: bool has True value is game runs in human vs cpu mode
    current_move: int turn of current player

    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.root = tkinter.Tk()
        self._set_up_window()
        self.buttons = []
        self.menu_buttons = []
        self.model_part = None
        self.is_cpu_game = False
        self.current_move = 0
        self._add_buttons()
        self._add_menu()

    def _set_up_window(self):
        """Sets up main window properties """
        self.root.title(" Tic-Tac-Toe")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.f_left = tkinter.Frame(self.root)
        self.f_bottom = tkinter.Frame(self.root)
        self.f_right = tkinter.Frame(self.root)
        self.f_right.pack(side=tkinter.RIGHT, anchor=tkinter.NW)
        self.f_left.pack(side=tkinter.TOP, anchor=tkinter.NW)
        self.f_bottom.pack(side=tkinter.BOTTOM, anchor=tkinter.NW)

    def _add_buttons(self):
        """Creates and adds game board buttons"""
        for i in range(9):
            button = tkinter.Button(self.f_left, text=" ", font="Helvetica, 20", height=3, width=6)
            button["state"] = "disable"
            self.add_callback(button, self._button_click)
            self.buttons.append(button)
        counter = 0
        for i in range(3):
            for j in range(3):
                self.buttons[counter].grid(row=i, column=j)
                counter += 1

        self.lb1 = tkinter.Label(self.f_bottom, height=4, text="Welcome!", font="Helvetica, 20")
        self.lb1.pack(side=tkinter.LEFT)

    def _add_menu(self):
        """Creates and adds main menu buttons, assign commands  as well"""
        b_text = ("Start game", "Start vs CPU", "Table of winners", "Clear table", "Exit")
        for i in range(5):
            b_menu = tkinter.Button(self.f_right, height=2, text=b_text[i], width=20)
            self.menu_buttons.append(b_menu)
        row = 0
        for button in self.menu_buttons:
            button.grid(row=row, column=0)
            row += 1
        func = (self.human_vs_human, self.human_vs_cpu, self.show_table,
                self.clear_table,self.exit_game)
        for index, m_button in enumerate(self.menu_buttons):
            m_button["command"] = func[index]

    def _ask_name(self):
        """
        Shows dialog that return user name
        :return str
        """
        user_name = simpledialog.askstring(title="Name", prompt="Enter name", parent=self.root)
        return user_name

    def _ask_char(self):
        """
        Shows dialog that asks user character for human vs cpu mode
        :return str
        """
        user_char = simpledialog.askstring(title="Char",
                                           prompt="Chose side X or 0", parent=self.root)
        return user_char

    def _disable_menu(self):
        """Disables main menu"""
        for i in range(4):
            self.menu_buttons[i]["state"] = "disable"

    def _enable_menu(self):
        """Enables main menu"""
        for m_button in self.menu_buttons:
            m_button["state"] = "normal"
        self.lb1["text"] = "Welcome!"

    def _enable_game_board(self):
        """Enables game board and resets its buttons text"""
        for button in self.buttons:
            button["state"] = "normal"
            button["text"] = ""

    def _disable_board(self):
        """Disables game board buttons"""
        for button in self.buttons:
            button["state"] = "disable"

    def set_model(self, model: "Model part"):
        """Sets model_part attribute"""
        self.model_part = model

    def human_vs_human(self):
        """Starts game in human vs human mode"""
        self._disable_menu()
        self.model_part.clear_players()
        name1 = self._ask_name()
        name2 = self._ask_name()
        if not(name1 and name2):  # if user cancels name asking dialog returns no main menu
            self._enable_menu()
            return
        self.model_part.set_players_name(name1, name2)
        self._enable_game_board()
        self.lb1["text"] = "Turn " + self.model_part.get_players()[0][1]

    def human_vs_cpu(self):
        """Starts game in human vs cpu mode"""
        self._disable_menu()
        self.model_part.clear_players()
        self.is_cpu_game = True
        h_name = self._ask_name()  # asks user name
        if h_name is None:
            self._enable_menu()  # if dialog cancels return to main menu
            return
        h_char = self._ask_char()  # asks human player character

        while True:  # Checks and set players, human and cpu
            if h_char.upper() in ("X", "O", "0"):
                if h_char.upper() == "X":
                    self.current_move = 0
                    self.model_part.set_cpu_and_human_players((h_name, "X"), ("CPU", "0"))
                    break

                self.model_part.set_cpu_and_human_players((h_name, "0"), ("CPU", "X"))
                self.current_move = 0
                break
            h_char = self._ask_char()
        self._enable_game_board()
        if h_char.upper() != "X":  # if user character is 0 cpu makes turn firs
            index = self.model_part.minimax_turn()
            self.model_part.update_board(index, "X")
            self.buttons[index]["text"] = "X"
            self.buttons[index]["state"] = "disable"
            self.lb1["text"] = "Turn " + h_name
        else:
            self.lb1["text"] = "Turn " + h_name



    @staticmethod
    def _play_again():
        """Dialog asking for another play or return in main menu"""
        answer = mb.askyesno("Tic-tac-toe", "Play again for revenge?")
        return answer

    @staticmethod
    def add_callback(control: tkinter.Button, func: "function"):
        """Callback wrapper for game board buttons"""
        def inner():
            return func(control)

        control["command"] = inner

    def _button_click(self, control: tkinter.Button):
        """
        Callback function for game board button
        :parameter control, instance of button that clicked
        """

        tmp = self.model_part.get_players(), self.model_part.get_cpu_and_human_players()
        players = tmp[1] if self.is_cpu_game else tmp[0]
        is_game = True


        control["text"] = players[self.current_move][0]
        control["state"] = "disable"
        index = self.buttons.index(control)
        self.model_part.update_board(index, players[self.current_move][0])
        if self.model_part.is_winner(players[self.current_move][0], self.model_part.get_data()):
            self._disable_board()
            self.lb1["text"] = players[self.current_move][1] + " wins!"
            is_game = False
            answer = self._play_again()
            if answer:
                players[self.current_move][2] += 1
                self.model_part.clear_board()
                self._enable_game_board()
                self.lb1["text"] = "Turn " + players[self.current_move][1]
            elif players[0][2] > 0 or players[1][2] > 0:
                players[self.current_move][2] += 1
                self.model_part.logger.info(f"{players[0][1]}: {players[0][2]} "
                                            f"{players[1][1]}: {players[1][2]}")
                for player in players:
                    player[2] = 0
                self.model_part.clear_board()
                self._enable_game_board()
                self._disable_board()
                self.is_cpu_game = False
                self._enable_menu()
                is_game = False

            else:
                self.model_part.logger.info(f"{players[self.current_move][1]} wins")
                self.lb1["text"] = f"{players[self.current_move][1]} wins"
                for player in players:
                    player[2] = 0
                self.model_part.clear_board()
                self._enable_game_board()
                self._disable_board()
                self._enable_menu()
                self.is_cpu_game = False
                is_game = False
        elif self.model_part.is_draw():
            self.lb1["text"] = "Draw"
            answer = self._play_again()
            if not answer:
                self.model_part.logger.info(f"{players[0][1]} and "
                                            f"{players[1][1]} result: Draw")
                if players[0][2] + players[1][2] > 0:
                    self.model_part.logger.info(f"{players[0][1]}: {players[0][2]} "
                                                f"{players[1][1]}: {players[1][2]}")
                    for player in players:
                        player[2] = 0
                self.model_part.clear_board()
                self._enable_game_board()
                self._disable_board()
                self._enable_menu()
                self.is_cpu_game = False
                is_game = False
            self.model_part.clear_board()
            self._enable_game_board()

        if self.is_cpu_game:  # if game runs in human vs cpu mode cpu makes own turn
            index = self.model_part.minimax_turn()
            self.model_part.update_board(index, players[1][0])
            self.buttons[index]["text"] = players[1][0]
            self.buttons[index]["state"] = "disable"
            if self.model_part.is_winner(players[1][0], self.model_part.get_data()):
                self._disable_board()
                self.model_part.clear_board()
                self.lb1["text"] = players[1][1] + " wins!"
                is_game = False
                answer = self._play_again()
                if answer:
                    players[1][2] += 1
                    self.model_part.clear_board()
                    self._enable_game_board()
                    is_game = True
                elif players[0][2] > 0 or players[1][2] > 0:
                    players[1][2] += 1
                    self.model_part.logger.info(f"{players[0][1]}: {players[0][2]} "
                                                f"{players[1][1]}: {players[1][2]}")
                    for player in players:
                        player[2] = 0
                    self.model_part.clear_board()
                    self._enable_game_board()
                    self._disable_board()
                    self._enable_menu()
                    self.is_cpu_game = False
                    is_game = False
                else:
                    self.model_part.logger.info(f"{players[1][1]} wins")
                    self.lb1["text"] = f"{players[1][1]} wins"
                    self._enable_game_board()
                    self._disable_board()
                    self.model_part.clear_board()
                    self._enable_menu()
                    is_game = False
            elif self.model_part.is_draw():
                self.lb1["text"] = "Draw"
                answer = self._play_again()
                if not answer:
                    self.model_part.logger.info(f"{players[0][1]} and "
                                                f"{players[1][1]} result: Draw")
                    if players[0][2] + players[0][2] > 0 :
                        self.model_part.logger.info(f"{players[0][1]}: {players[0][2]} "
                                                    f"{players[1][1]}: {players[1][2]}")
                        for player in players:
                            player[2] = 0

                    self._enable_game_board()
                    self.model_part.clear_board()
                    self._disable_board()
                    self._enable_menu()
                    self.is_cpu_game = False
                    is_game = False
                self._enable_game_board()
                self.model_part.clear_board()

        if not self.is_cpu_game:
            self.current_move = (self.current_move + 1) % 2
        if is_game:
            self.lb1["text"] = "Turn " + players[self.current_move][1]


    def show_table(self):
        """Create another window and shows game.log file content"""
        message_window = tkinter.Toplevel()
        message_window.title("Table of winners")
        message_window.geometry("450x450")
        text_field = tkinter.Text(message_window)
        text_field.pack(side=tkinter.TOP)
        scroll = tkinter.Scrollbar(command=text_field.yview)
        scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        text_field.config(yscrollcommand=scroll.set)
        message_window.transient()
        self.root.withdraw()

        def destroy_window():
            """Action for button in new window."""
            message_window.grab_release()
            self.root.iconify()
            message_window.destroy()

        exit_btn = tkinter.Button(message_window, text="Exit", command=destroy_window)
        exit_btn.pack(side=tkinter.BOTTOM)
        with open(self.model_part.get_log_name()) as log:
            lines = log.readlines()
            if lines:
                for num, text in enumerate(lines):
                    text_field.insert(str(num+1.0), text)
            else:
                text_field.insert("1.0", "Table is empty")

    def clear_table(self):
        """Clears game.log file"""
        with open(self.model_part.get_log_name(), "w") as log:
            log.truncate(0)
        mb.showinfo("Tic-tac_toe", "Table of winners is clear!")

    def exit_game(self):
        """Exit from application"""
        self.root.destroy()
        sys.exit(0)

    def run(self):
        """Starts application"""
        self.root.mainloop()
