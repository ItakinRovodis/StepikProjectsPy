from random import *

def is_valid(c):
	result = True
	for char in c:
		if char < '0' or char > '9':
			result = False
			break
	if result:
		if int(c) > 100:
			result = False
	return result

left = 1
right = 100


print("Добро пожаловать в числовую угадайку")

print("Укажите правую границу")

right = int(input())
n = randint(left, right)

count_p = 0

while True:
	print("Введите число от %d до %d" %(left, right))
	st = input()
	if is_valid(st):
		count_p += 1
		st = int(st)
		if st > n:
			print("Ваше число больше загаданного, попробуйте еще разок")
		elif st < n:
			print("Ваше число меньше загаданного, попробуйте еще разок")
		else:
			print("Вы угадали, поздравляем!")
			break
	else:
		print("А может быть все-таки введем целое число от %d до %d?" %(left, right))

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
print("Число попыток %d" %(count_p))
