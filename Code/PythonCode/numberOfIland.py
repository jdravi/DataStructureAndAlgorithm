

def valid_index(i,j,m,n):

	if i>=0 and i<m and j>=0 and j<n :

		return True
	return False




def count_iland(data,track_visited,pair,row_list,colm_list,row_count,col_count):



	queue = []
	queue.append(pair)

	while len(queue)!=0:

		poped_element = queue.pop(0)
		x = poped_element[0]
		y = poped_element[1]

		track_visited[x][y] = 1
		
		for i in range(4):
				x = x + row_list[i]
				y = y + colm_list[i]

				if valid_index(x,y,row_count,col_count) and track_visited[x][y]==0:
					temp = []
					temp.append(x)
					temp.append(y)
					queue.append(temp)



def num_of_iland_utill(data,track_visited):


	row_list = [-1, -1, -1,  0, 0,  1, 1, 1]
	colm_list = [-1,  0,  1, -1, 1, -1, 0, 1]

	row_count = len(data)
	col_count = len(data[0])

	count  = 0
	for x in range(row_count):
		for y in range(col_count):


			if data[x][y] == 1 and track_visited[x][y]==0:

				count = count + 1

				pair = []
				pair.append(x)
				pair.append(y)
				count_iland(data,track_visited,pair,row_list,colm_list,row_count,col_count)

	print("Number of ieland : " + str(count))




if __name__=='__main__':

	data = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 

	track_visited = [[0]*len(data[0])]*len(data)
	num_of_iland_utill(data,track_visited)

	