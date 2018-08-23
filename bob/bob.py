def hey(phrase):
	phrase = phrase.strip()
	if phrase.isupper():
		if phrase.endswith('?'):
			return "Calm down, I know what I'm doing!"
		else:
			return 'Whoa, chill out!'
	elif phrase.endswith('?'):
		return 'Sure.'	
	elif len(phrase) == 0:
		return  'Fine. Be that way!' 
	else:
		return 'Whatever.'
