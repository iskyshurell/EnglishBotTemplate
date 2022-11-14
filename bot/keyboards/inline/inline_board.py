import re
from telebot import types
from typing import List


def add_inline_keyboard(iter_k: List) -> types.InlineKeyboardMarkup:
	"""
	Функция add_inline_keyboard:

	принимает 2 аргумента:
	-- iter_k = dict()
	-- func = str()

	Возвращает готовый InlineKeyboardMarkup()
	"""

	inline_keyboard = types.InlineKeyboardMarkup()

	for i_key in iter_k:
		short_name = re.search(r'\w+', i_key).group()
		inline_keyboard.add(types.InlineKeyboardButton(text = i_key, callback_data = f'{short_name}'))

	return inline_keyboard
