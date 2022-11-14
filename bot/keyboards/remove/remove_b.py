from telebot import types
from interface.UI import UI


def add_remove_keyboard(ui: UI, board: str = '') -> None:
	"""
	Функция add_remove_keyboard:

	принимает 2 аргумента:
	-- ui = UI()
	-- board = str()

	Функция создаёт ReplyKeyboardRemove()
	и добавяет его в класс с интерфейсом
	"""
	ui.set_ui(name = board, value = types.ReplyKeyboardRemove())
