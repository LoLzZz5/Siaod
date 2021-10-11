def small(arr):
	smallest_elem = arr[0]
	smallest_index = 0

	for i in range(1, len(arr)):
		if arr[i] < smallest_elem:
			smallest_elem = arr[i]
			smallest_index = i

	return smallest_index

def selection_sort(arr):
	result = []

	for i in range(len(arr)):
		smallest_index = small(arr)
		result.append(arr.pop(smallest_index))

	return result

if __name__ == '__main__':
	print(selection_sort([5,7,2,0,6,3,5,1]))# == [0, 1, 2, 3, 5, 5, 6, 7]
	print(selection_sort([63,16,9,5,234,76,4,59,1,547]))# == [1, 4, 5, 9, 16, 59, 63, 76, 234, 547]