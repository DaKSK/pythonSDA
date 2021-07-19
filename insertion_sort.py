def insertion_sort(array):
	swap_counter = 0
	for index in range(1, len(array)):
		value = array[index]
		i = index - 1
		while i >= 0:
			if value < array[i]:
				array[i + 1] = array[i]
				array[i] = value
				swap_counter += 1
				i -= 1
			else:
				break
	print(f"Swaps counter got {swap_counter} swaps")


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
insertion_sort(numbers)
print(numbers)
