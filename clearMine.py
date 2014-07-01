input_file = open("E:\pythonFile\нд╪Ч\mineClear.txt","r")
s0=input_file.read()
def getMatrix(s):
	for i in range(1,5):
		for j in range(1,5):
			matrix[i-1][j-1]=s[i][j]
return matrix
getMatrix(s0)
a=[][],b=[[]]
def countMine(a):
	for i in range(0,4):
		for j in range(0,4):
			if i==0:
				if a[i][j]=="*"
					b[i+1][j]+=1,b[i+1][j+1]+=1

		