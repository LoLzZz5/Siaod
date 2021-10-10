def binary_search(numbers : list, digit : int):
	numbers.sort()
	low = 0
	high = len(numbers) - 1

	while low <= high:
		mid = low + high
		search = numbers[mid]

		if search == digit:
			return mid

		if search < digit:
			low = mid + 1
		else:
			high = mid - 1

	return 'No digit found'

if __name__ == '__main__':
	print(binary_search([1,5,7,10,3,8,4], 4))# == 2
	print(binary_search([1,5,7,10,3,8,4], 8))# == 5