def quick_sort(arr: list):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i >= pivot]
		return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
	print(quick_sort([62,7,2,7,845,3,6,1]))# == 1, 2, 3, 6, 7, 7, 7, 62, 845
	print(quick_sort([61,9,96,34,21,22,3]))# == 3, 9, 21, 22, 34, 61, 96