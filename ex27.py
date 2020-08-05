def count_vowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	lower_string = string.lower()
	vowel_count = 0
	for char in lower_string:
		for vowel in vowels:
			if char == vowel:
				vowel_count+=1
	return vowel_count
    
