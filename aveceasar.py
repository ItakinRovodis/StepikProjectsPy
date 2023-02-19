
upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'

string = [c for c in input()]

i = 0
length = len(string)

while i < length:
	word_length = 0
	j = i
	while j < length:
		if string[j].isalpha():
			j+=1
		else:
			break
	word_length = j - i
	while i < j:
		if string[i] in upper_eng_alphabet:
			index = upper_eng_alphabet.index(string[i]) + word_length
			while index >= 26:
				index -= 26
			string[i] = upper_eng_alphabet[index]
		elif string[i] in lower_eng_alphabet:
			index = lower_eng_alphabet.index(string[i]) + word_length
			while index >= 26:
				index -= 26
			string[i] = lower_eng_alphabet[index]
		i += 1
	i += 1
print(*string, sep='')
