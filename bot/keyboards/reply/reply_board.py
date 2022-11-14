from telebot import types
from interface.UI import UI


def add_reply_keyboard(ui: UI, k: int, *args, **kwargs) -> None:
	"""
	Функция add_reply_keyboard():

	принимает 2 аргумента и *args с **kwargs:
	-- ui = UI()
	-- k = int()
	В args передаётся название кнопок,
	в kwargs название клавиатуры

	присваивает ui клавиатуру ReplyKeyboardMarkup()

	"""

	keyboard = types.ReplyKeyboardMarkup()
	buttons = [types.KeyboardButton(i_btn) for i_btn in args]

	for i in range(0, 9, k):
		keyboard.row(*buttons[i: min(len(buttons), i + k)])

	ui.set_ui(name = kwargs['board'], value = keyboard)