# what is matrix?
# 2-dimentional matrix1ay that consists of rows and columns. 
# matrix is an matrix1angement of elements in horizontal or vertical lines of entries.
# matrices are very important data structures for many mathematical and scientific
# calculations (for these perposes it's better to use numpuy library). 
# newlist = [expression for item in iterable if condition == True]
# what is list comprehension?
# is an elegant way to define and create a list in python.
# a list comprehension consists of these parts : 
# 1- output expression,
# 2- input sequence,
# 3- a variable representing a member of the input sequence
# 4- optional predicate part.
# newList = [ 1-expression(element) for 3-element in 2-range|string|list 4-if condition ] 


# 1- creating a matrix with a list of list
matrix1 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]] 
matrix2 = [ [ 1, 2, 3], [ 5, 6, 7 ], [ 10, 11, 12] ]

# 2- printing the matrix's entire
def show(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")

# 3- give matrix's inputs from user
def getInput():
    matrix= []
    row = int(input("Enter row:"))
    col = int(input("Enter column:"))
    print("Enter elements:")
    # loop for getting row's item
    for r in range(row):
        x = []
        # loop for getting column's item
        for c in range(col):
            x.append(int(input()))
        matrix.append(x)
    return matrix

# test creating matrix by give inputs from user
show(getInput())

# 4- searching an element in matrix
def search(matrix, x):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == x):
                return True
    return False

# test searching in matrix
print("YES, found the element") if(search(matrix2, 7)) else print("NO, not found the element" )

# 5- transpose a matrix
def transpose(matrix):
    # using list comprehension for makeing an empty matrix
    rows, cols = (len(matrix), len(matrix[0]))
    result = [[0 for i in range(cols)] for j in range(rows)]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            result[column][row] = matrix[row][column]
    return result

# testing transpose
print('current matrix is:')
show(matrix1)
print('transpose is: ')
show(transpose(matrix1))

# 6- add two matrices
def add2martix(x, y):
    # using list comprehension for makeing an empty matrix
    rows, cols = (len(x), len(x[0]))
    result = [[0 for i in range(cols)] for j in range(rows)]
    for r in range(len(x)):
        for c in range(len(x[0])):
            result[r][c] = x[r][c] + y[r][c]
    return result

# 7- sub two matrices
def sub2martix(x, y):
    # using list comprehension for makeing an empty matrix
    rows, cols = (len(x), len(x[0]))
    result = [[0 for i in range(cols)] for j in range(rows)]
    for r in range(len(x)):
        for c in range(len(x[0])):
            result[r][c] = x[r][c] - y[r][c]
    return result

# 8- sub two matrices
def mul2martix(x, y):
    # using list comprehension for makeing an empty matrix
    rows, cols = (len(x), len(x[0]))
    result = [[0 for i in range(cols)] for j in range(rows)]
    for r in range(len(x)):
        for c in range(len(x[0])):
            result[r][c] = x[r][c] * y[r][c]
    return result

# 9- sub two matrices
def div2martix(x, y):
    # using list comprehension for makeing an empty matrix
    rows, cols = (len(x), len(x[0]))
    result = [[0 for i in range(cols)] for j in range(rows)]
    for r in range(len(x)):
        for c in range(len(x[0])):
            result[r][c] = x[r][c] // y[r][c]
    return result

# test mathematic functions on 2 matrixs
print('addition is: ')
show(add2martix(matrix1, matrix2))
print('subtraction is: ')
show(sub2martix(matrix1, matrix2))
print('multiplication is: ')
show(mul2martix(matrix1, matrix2))
print('division is: ')
show(div2martix(matrix1, matrix2))

# 10- print the principal diagonal
def principalDiagonal(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j):
                result.append(matrix[i][j])
    return result

# 11- print the secondary diagonal
def secondaryDiagonal(matrix):
    result = []
    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if ((i + j) == (n - 1)):
                result.append(matrix[i][j])
    return result

# test principal and second diagonal in matrix
print("principal diagonal: ",principalDiagonal(matrix1))
print("secondary diagonal: ",secondaryDiagonal(matrix1))