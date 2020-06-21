#Implementing Backtracking algorithm


#function to implement backtracking
def Backtracking(array, column, status, n, occupied, queen):

	for row in range (n):
		array[row][column]=1
		queen[column].x, queen[column].y = column, row


		#checking whether a conflict happens
		for i in range(len(occupied)):
			if row!=occupied[i][0] and (abs(occupied[i][0]-row)!=abs(occupied[i][1]-column)):
				status=True
			else:
				status=False
				break


		if status == True:
			if column<n-1:
				occupied.append([row,column])
				if Backtracking(array, column+1, status, n, occupied, queen):
					return True
				else:
					array[row][column]=0
					occupied.pop(-1)
					
			else:
				return True
		else:
			array[row][column]=0
			

		
	return False




