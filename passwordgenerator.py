from random import *


def generate_password(length, pattern):
	chars = ''
	for _ in range(length):
		chars += choice(pattern)
	return chars


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1Lo0O'

print('Сколько паролей нужно сгенерировать?')

num = int(input())

print("Какова должна быть длина пароля?")

length = int(input())

pattern = []

print("Включать в пароль цифры?")

answer = input()

if answer in ['Yes', 'yes', 'Да', 'да']:
	pattern.extend(digits)

print("Включать в пароль строчные буквы")

answer = input()

if answer in ['Yes', 'yes', 'Да', 'да']:
	pattern.extend(lowercase_letters)

print("Включать в пароль прописные буквы")

answer = input()

if answer in ['Yes', 'yes', 'Да', 'да']:
	pattern.extend(uppercase_letters)

print("Включать в пароль символы")

answer = input()

if answer in ['Yes', 'yes', 'Да', 'да']:
	pattern.extend(punctuation)

print("Исключать ли неоднозначные символы ")

answer = input()

if answer in ['Yes', 'yes', 'Да', 'да']:
	for c in exceptions:
		pattern.remove(c)

for _ in range(num):
	print(generate_password(length, pattern))
	
