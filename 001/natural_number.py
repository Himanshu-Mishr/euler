def natural_number():

	naturalList = []

	# 3
	for i in range(0, 1000, 3):
		naturalList.append(i)

	# 5
	for i in range(0, 1000, 5):
		naturalList.append(i)

	# provides more speed up, compared to adding if condition
	answer = sum(set(naturalList))

	return answer

if __name__ == '__main__':
	print(natural_number())