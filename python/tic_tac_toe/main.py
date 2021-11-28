"""
Main module of game
"""

import model
import view
import controller
import view_tk

data = model.Model()
field = view_tk.View()
game = controller.Controller(data, field)
game.start()
