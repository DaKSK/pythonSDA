def bubble_sort(array):
	counter = 0
	while True:
		counter += 1
		swapped_values = False
		for i in range(1, len(array)):
			if array[i] < array[i - 1]:
				temp = array[i]
				array[i] = array[i - 1]
				array[i - 1] = temp
				swapped_values = True
		if not swapped_values:
			print(f"{counter} loops")
			break  # List is sorted!


numbers = [5, 3, 7, 10, 4, 4, 2, 10]
bubble_sort(numbers)
print(f"Sorted list: {numbers}")
