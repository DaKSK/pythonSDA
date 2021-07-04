def sum_array_recurs(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	return array[0] + sum_array_recurs(array[1:])

