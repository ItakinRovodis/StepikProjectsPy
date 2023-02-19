def is_valid(n):
	result = True
	for i in n:
		if '0'> i or i > '9':
			result = False
			break
	return result
rejim = ''
alphabet = ''
n = 0

while True:
	print("Выберите режим: шифрование(1) / дешифрование(2)")
	rejim = input()
	if is_valid(rejim):
		rejim = int(rejim)
		break
	else:
		print("Неверно! Попробуйте ввести число")

while True:
	print("Выберите язык алфавита : ru / en")
	alphabet = input()
	if alphabet == 'ru' or alphabet == 'en':
		break
	else:
		print("Неверно! Попробуйте ввести ru / en")



while True:
	print("Выберите шаг сдвига")
	n = input()
	if is_valid(n):
		n = int(n)
		break
	else:
		print("Неверно! Попробуйте ввести число")

upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

print("Введите строку")
string = [c for c in input()]

if rejim == 1:
	if alphabet == 'ru':
		for i in range(len(string)):
			if string[i] in upper_rus_alphabet:
				index = upper_rus_alphabet.index(string[i]) + n
				while index >= 32:
					index -= 32
				string[i] = upper_rus_alphabet[index]

			elif string[i] in lower_rus_alphabet:
				index = lower_rus_alphabet.index(string[i]) + n
				while index >= 32:
					index -= 32
				string[i] = lower_rus_alphabet[index]
	else:
		for i in range(len(string)):
			if string[i] in upper_eng_alphabet:
				index = upper_eng_alphabet.index(string[i]) + n
				while index >= 26:
					index -= 26
				string[i] = upper_eng_alphabet[index]

			elif string[i] in lower_eng_alphabet:
				index = lower_eng_alphabet.index(string[i]) + n
				while index >= 26:
					index -= 26
				string[i] = lower_eng_alphabet[index]
else:
	if alphabet == 'ru':
		for i in range(len(string)):
			if string[i] in upper_rus_alphabet:
				index = upper_rus_alphabet.index(string[i]) - n
				while index < 0:
					index = 32 + index
				string[i] = upper_rus_alphabet[index]

			elif string[i] in lower_rus_alphabet:
				index = lower_rus_alphabet.index(string[i]) - n
				while index < 0:
					index = 32 + index
				string[i] = lower_rus_alphabet[index]
	else:
		for i in range(len(string)):
			if string[i] in upper_eng_alphabet:
				index = upper_eng_alphabet.index(string[i]) - n
				while index < 0:
					index = 26 + index
				string[i] = upper_eng_alphabet[index]

			elif string[i] in lower_eng_alphabet:
				index = lower_eng_alphabet.index(string[i]) - n
				while index < 0:
					index = 26 + index
				string[i] = lower_eng_alphabet[index]
print(*string,sep='')

