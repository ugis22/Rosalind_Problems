
def symbol_to_number(symbol):
	symbols_list = {
		'A' : 0,
		'C' : 1,
		'G' : 2,
		'T' : 3,
	}
	return symbols_list[symbol]

def pattern_to_number(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	
	return 4*pattern_to_number(prefix)+symbol_to_number(symbol)

def results(pattern):
	result = pattern_to_number(pattern)
	print(result)


results('GTTGCGATACGTCCACGACCTCTAATATGC')	
