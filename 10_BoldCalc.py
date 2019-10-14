# Написать программу — калькулятор с переменными и обработкой ошибок
# Команда, начинающаяся на '#' — комментарий. Команда вида Переменная=выражение задаёт переменную. Команда вида выражение выводит значение выражения.
# Если команда содержит знак "=", но не является присваиванием, выводится диагностика "invalid assignment" (см. пример).
# Если слева от "=" находится не идентификатор, выводится диагностика "invalid identifier (см. пример)".
# В случае любых других ошибок выводится текст ошибки.
# «Выражение» — это произвольное выражение Python3, в котором вдобавок можно использовать уже определённые переменные (и только их).
# Пробелов в командах нет. Пустая команда означает конец вычислений. Калькулятор вводит и исполняет команды по одной, тут же выводя диагностику,
# но в тестах это выглядит как ввод последовательности строк и вывод последовательности строк.


def find_assignment(o, expr):
	if o in expr:
		raise Exception("invalid assignment '{}'".format(expr))

def find_identifier(expr):
	if not expr[0].isalpha():
		raise Exception("invalid identifier '{}'".format(expr[:expr.find('=')]))
	return expr[:expr.find('=')], expr[expr.find('=')+1:]

expressinon = input()
calc_dict = {}
operations = ('==', '<=', '>=', '!=')

while(expressinon):
	if expressinon[0] !=  '#':
		try:
			ident = None
			for oper in operations:
				find_assignment(oper, expressinon)
			if '=' in expressinon:
				ident, expressinon = find_identifier(expressinon)
			
			comp = eval(expressinon, calc_dict)
		except Exception as e:
			print(e)
		else:
			if ident:
				calc_dict.update({ident: comp})
			else:
				print(comp)
		finally:
			pass

	expressinon = input()


# # input:
# 42
# 100500//33
# "Qq!"*(6-2)
# # Здесь ошибка
# 3,,5
# 10/(8-8)
# "wer"[2]+"qwe"[1]
# "wer"[7]+"qwe"[9]
# 1+(2+(3
# a0=5
# b0=7
# # И здесь ошибка
# 12N=12
# # И ещё где-то были
# a0+b0*8
# c=b0//2+a0
# d==100
# c+d
# sorted(dir())