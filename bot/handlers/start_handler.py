import telebot
import telebot.types as tp
from loader import bot, interface


@bot.message_handler(commands = ['start'])
def start_func(
		# bot: telebot.Telebot
		message: tp.Message
		
	):

	bot.send_message(
		message.from_user.id,
		'Привет!',
		reply_markup = interface.get_ui('del')
	)

	bot.send_message(
		message.from_user.id,
		'Я бот для изучения английского языка LanguageToGo'
	)

	bot.send_message(
		message.from_user.id,
		'Выберите действие: ',
		reply_markup = interface.get_ui('main')
	)


@bot.message_handler()
def main_handler(
		message: tp.Message
	):
	resp = message.text

	if resp == 'FAQ':
		bot.send_message(
			message.from_user.id,
			'Частые вопросы:',
			reply_markup = interface.get_ui('faq')
		)

		bot.register_next_step_handler(
			message,
			faq_answ
		)
	elif resp == 'Курсы':
		bot.send_message(
			message.from_user.id,
			"Курс 'Начало положено':",
			reply_markup = interface.get_ui('info')
		)

		bot.register_next_step_handler(
			message,
			info_handler
		)

	else:
		bot.send_message(
			message.from_user.id,
			'Не удалось распознать сообщение\n'
			'Повторите попытку!'
		)

		bot.register_next_step_handler(
			message,
			main_handler
		)


def faq_answ(
		message: tp.Message
	):

	if message.text == 'Назад в меню':
		bot.send_message(
			message.from_user.id,
			'Возвращение в главное меню произошло успешно',
			reply_markup = interface.get_ui('main')
		)

	elif message.text == 'Тут пусто':
		bot.send_message(
			message.from_user.id,
			'Пока что нет faq',
		)
		bot.register_next_step_handler(
			message,
			faq_answ
		)

	else:
		bot.send_message(
			message.from_user.id,
			'Не удалось распознать сообщение\n'
			'Повторите попытку!'
		)

		bot.register_next_step_handler(
			message,
			faq_answ
		)


def info_handler(
		message: tp.Message
	):
	resp = message.text

	if resp == 'Инфо об онлайн уроках':
		bot.send_message(
			message.from_user.id,
			'Как проходит запись'
		)

		bot.register_next_step_handler(
			message,
			info_handler
		)

	elif resp == 'Записаться на урок':
		bot.send_message(
			message.from_user.id,
			'Запись на урок'
		)

		bot.register_next_step_handler(
			message,
			info_handler
		)

	elif resp == 'Почему мы':
		bot.send_message(
			message.from_user.id,
			'Наши плюсы и минусы'
		)

		bot.register_next_step_handler(
			message,
			info_handler
		)

	elif resp == 'Назад в меню':
		bot.send_message(
			message.from_user.id,
			'Возвращение в главное меню произошло успешно',
			reply_markup = interface.get_ui('main')
		)

	else:
		bot.send_message(
			message.from_user.id,
			'Не удалось распознать сообщение\n'
			'Повторите попытку!'
		)

		bot.register_next_step_handler(
			message,
			info_handler
		)
