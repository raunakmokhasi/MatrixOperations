def swapRows(A,row1,row2):
	A[row1],A[row2] = A[row2],A[row1]
	return A
#print(swapRows([[1,2,3],[4,5,6],[7,8,9]],0,2))


def Row_Transformation(A,x,row1,row2):
	for i in range(len(A[row1])):
		A[row2][i] = A[row2][i] + (x*A[row1][i])
	return A
#print(Row_Transformation([[1,2,3],[4,5,6],[7,8,9]],3,0,2))


def MatrixRank(A):
	rank = min(len(A[0]),len(A))
	
	i=0
	while (i<rank):
		if A[i][i]!=0:
			j=0
			while(j<len(A)):
				if (i!=j):
					x=(A[j][i]/A[i][i])*(-1)
					m=0
					while(m<rank-1):
						A=Row_Transformation(A,x,m,j)
						m+=1	
					A[j][i] = 0
				j+=1	
		else:
			flag = 0
			k=i+1
			while (k<rank):	
				if A[k][i]:
					swapRows(A,i,k)
					flag = 1
					break
				k+=1
			if flag==0:
				count=1
				
				for y in range(i+1,rank):
					if (A[y][i]!=0):
						count=0
						break
				if count==1:
					for k in range(len(A)):
						A[k][i],A[k][len(A[0])-1]=A[k][len(A[0])-1],A[k][i]
					rank-=1
			i-=1
		i+=1
	return rank

#MatrixRank([[1,2,3],[0,0,0]])