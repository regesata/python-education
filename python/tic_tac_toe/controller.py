"""
Module contains classes for tic tac toe controller part
"""

import model
import view


class Controller:
    """
        Class realize main part of game logic
    """

    def __init__(self, model_part: model.Model, view_part: view.View):
        self.model_part = model_part
        self.view_part = view_part

    def __str__(self):
        return "Controller part for game"


    def start(self):
        """Runs game"""
        self.view_part.set_model(self.model_part)
        self.view_part.run()
