import telebot
from config.load_data import token
from interface.UI import *
from keyboards.reply import *
from keyboards.inline import *
from keyboards.remove import *


def load(b_token: str) -> telebot.TeleBot:
	"""
	Функция load:

	принимает 1 аргумент:
	-- b_token = str(), токен для бота

	Возвращает самого бота для подальшей работы с ним.
	"""

	tele_bot = telebot.TeleBot(b_token)
	return tele_bot


bot = load(token)
bot.enable_save_next_step_handlers(delay=2)

ui = UI()
add_reply_keyboard(ui, 3, 'Инфо об онлайн уроках', 'Записаться на урок', 'Почему мы', 'Назад в меню', board = 'info')
add_reply_keyboard(ui, 3, 'Курсы', 'FAQ', board = 'main')
add_reply_keyboard(ui, 3, 'Тут пусто', 'Назад в меню', board = 'faq')
ui.set_ui('in_info', add_inline_keyboard(['Инфо об онлайн уроках', 'Записаться на урок', 'Почему мы']))
add_remove_keyboard(ui, 'del')
interface = ui

if __name__ == '__main__':
	pass
