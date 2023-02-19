from random import *

def is_valid(char):
	result = True
	if len(char) != 1:
		result = False
	char = char.lower()
	if 'а' > char or char > 'я':
		result = False
	return result

words = ["адмирал","алмаз","конь","география","велосипед","виеслица", "пальто", "перфоратор"]

w = choice(words)
word = [c for c in w]
opened = [0] * len(word)

print(opened)

print("Начинаем игру!")
print('_' * (len(word) * 2 + 1))
print('|',end='')
for i in range(len(word)):
	if opened[i] == 1:
		print(word[i], end='')
	else:
		print(' ', end='')
	print('|',end ='')
print()
print('_' * (len(word) * 2 + 1))
char = ''
while True:
	miss_count = 0
	while True:
		print('Введите букву!')
		char = input()
		if is_valid(char):
			break
		else:
			print("Ошибка! Попробуйте ввести букву!")
	if char in word:
		for i in range(len(word)):
			if char == word[i]:
				opened[i] = 1
	else:
		miss_count += 1
	print('_' * (len(word) * 2 + 1))
	print('|',end='')
	for i in range(len(word)):
		if opened[i] == 1:
			print(word[i], end='')
		else:
			print(' ', end='')
		print('|',end ='')
	print()
	print('_' * (len(word) * 2 + 1))
	char = ''
	if miss_count >= 1:
		print(" " * 4 + "***" + " " * 4)
		print(" " * 3 +"*" + " "* 3 + "*" + " "* 3)
		print(" " * 3 +"*" + " "* 3 + "*" + " "* 3)
		print(" " * 4 + "***" + " " * 4)
		print(" "*5 +"*" + " "*5)
		print(" "*5 +"*" + " "*5)
	if miss_count == 2:
		print(" "*4 + "***" + " "* 4)
		print(" " * 4 +"*" + " " + "*" + " "* 4)
		print(" " * 4 +"*" + " " + "*" + " "* 4)
		print(" " * 4 + "***" + " " * 4)
	if miss_count == 3:
		print(" " * 3 + "****" + " "* 4)
		print(" " * 2 + "*"+" " +"*" + " " + "*" + " "* 4)
		print(" " * 1 + "*"+" "*2 +"*" + " " + "*" + " "* 4)
		print(" " * 4 + "***" + " " * 4)
	if miss_count >= 4:
		print(" " * 3 + "*****" + " "* 3)
		print(" " * 2 + "*"+" " +"*" + " " + "*"+" " +"*"+" "* 2)
		print(" " * 1 + "*"+" "*2 +"*" + " " + "*"+" "*2 +"*"+" "* 1)
		print(" " * 4 + "***" + " " * 4)
	if miss_count == 5:
		print(" "*4 + "*" + " "* 6)
		print(" "*3 + "*" + " "* 7)
		print(" "*2 + "*" + " "* 8)
	if miss_count == 6:
		print(" "*4 + "*" + " " + "*" + " "*4)
		print(" "*3 + "*" + " "*3 + "*" + " "*3)
		print(" "*2 + "*" + " "*5 + "*" + " "*2)
	if opened.count(1) == len(word):
		break
print("Конец")