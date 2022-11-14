
class UI:
	"""
	Класс UI():
	-- хранит в себе интерфейс
	-- позваляет достать или убрать интерфейс

	содержит 4 функции:
	-- __init__: инициализирует словарь в котором будет храниться интерфейс
	-- get_ui: возвращает значение по ключу из словаря с интерфейсом, если нету значения - False
	-- set_ui: задаёт значение по ключу в словарь
	-- clean_ui: позволяет убрать интерфейс из словаря

	"""

	def __init__(self) -> None:
		self.__all_ui = {}

	def get_ui(self, name):

		return self.__all_ui.get(name, False)

	def set_ui(self, name, value):
		self.__all_ui[name] = value

	def clean_ui(self, name):
		self.__all_ui.pop(name)
