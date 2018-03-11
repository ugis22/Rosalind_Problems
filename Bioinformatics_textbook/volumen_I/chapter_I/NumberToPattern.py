def number_to_symbol(index):
	symbols_list = {
		0 : 'A',
		1 : 'C',
		2 : 'G',
		3 : 'T',
	}
	return symbols_list[index]


def number_to_pattern(index, k):
	if k == 1:
		return number_to_symbol(index)
	prefix_index = index // 4
	rest = index % 4
	symbol = number_to_symbol(rest)
	prefix_pattern = number_to_pattern(prefix_index, k-1)
	return prefix_pattern + symbol
