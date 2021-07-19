def merge_sort(array):
	if len(array) <= 1:
		return array
	middle = len(array) // 2
	sorted_array_left = merge_sort(array[:middle])
	sorted_array_right = merge_sort(array[middle:])
	return merge(sorted_array_left, sorted_array_right)


def merge(array_l, array_r):
	sorted_list = []
	len_right = len(array_r)
	len_left = len(array_l)
	left_i, right_i = 0, 0
	steps = 0

	while left_i < len_left and right_i < len_right:
		if array_l[left_i] <= array_r[right_i]:
			sorted_list.append(array_l[left_i])
			left_i += 1
			steps += 1
		else:
			sorted_list.append(array_r[right_i])
			right_i += 1
			steps += 1
	sorted_list.extend(array_l[left_i:])
	sorted_list.extend(array_r[right_i:])
	return sorted_list


unsorted_array = [12, 16, 25, 28, 3, 7, 10, 11, 15, 26, 4, 6, 30]

print(merge_sort(unsorted_array))
