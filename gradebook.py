grades = [[72, 70, 73, 75],
		  [45, 70, 83, 39],
		  [42, 82, 75, 68],
		  [50, 50, 50, 50]]

def averageGrades(grades):
	times = ''
	list = []
	for rowIndex in grades:
		x = 0
		length = len(rowIndex)
		for eachNumber in rowIndex:
			x = x + eachNumber
		x = x/length
		times = times + str(x) + ' '
		list.append(x)
	
	average = 0
	counter = 0
	for numb in list:
		average = average + numb
		counter += 1
	
	average = average/counter
	times = times + ' ' + str(average)
	return times

print(averageGrades(grades))
	
