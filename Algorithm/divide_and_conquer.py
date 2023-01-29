# what is divide and conquer?
# the problem is divided into smaller sub-problems and then each problem is solved
# independently. keep on dividing the subproblems into even smaller sub-problems
# till reach a stage where no more division is possible. The solution of all sub-
# problems is finally merged in order to obtain the solution of an original problem.
# divide-and-conquer approach has three-step process:
# 1- Divide/Break -> This involves dividing the problem into smaller sub-problems.
# breaking the problem into smaller sub-problems. sub-problems should represent a 
# part of the original problem. this step generally takes a recursive approach to 
# divide the problem until no sub-problem is further divisible.
# 2- Conquer/Solve -> Solve sub-problems by calling recursively until solved.
# This step receives a lot of smaller sub-problems to be solved. the problems are 
# solved on their own.
# - Merge/Combine -> Combine the sub-problems to get the final solution of the whole problem.
# when the smaller sub-problems are solved, this stage recursively combines them 
# until they formulate a solution of the original problem.
# popular problems that use this approach:
# - merge-sort 
# - quick-sort 
# - binary-search 
# - find-min-value 
# - find-max-value 
# Advantages:
# - the difficult problem can be solved easily.
# - it divides the entire problem into subproblems thus 
# it can be solved parallelly ensuring multiprocessing
# - efficiently uses cache memory without occupying much space
# - reduces time complexity of the problem
# Disadvantages:
# - it involves recursion which is sometimes slow
# - efficiency depends on the implementation of logic
# - it may crash the system if the recursion is performed rigorously

# find maximum value in a list
def maxValue(myList, index, lenght):
    max = 0
    if lenght-1 == 0:
        return
    # 1- divide problem into sub-problems
    if index >= lenght-2:
        if myList[index] > myList[index+1]:
            return myList[index]
        else:
            return myList[index+1]
    # 2- find the max value recursivly or solve the sub-problems recursivly      
    max = maxValue(myList, index+1, lenght)
    # 3- combine sub-problems to find the final result
    if myList[index] > max:
        return myList[index]
    else:
        return max

# find minimum value in a list
def minValue(myList, index, lenght):
    min = 0
    if lenght-1 == 0:
        return
    # 1- divide problem into sub-problems
    if index >= lenght-2:
        if myList[index] < myList[index+1]:
            return myList[index]
        else:
            return myList[index+1]
    # 2- find the min value recursivly or solve the sub-problems recursivly  
    min = minValue(myList, index+1, lenght)
    # 3- combine sub-problems to find the final result
    if myList[index] < min:
        return myList[index]
    else:
        return min

myList = [10, 80, 15, 75, 170, 19, 14, 100, 450, 97, 78]
print("max value is:", maxValue(myList, 0, len(myList)))
print("min value is:", minValue(myList, 0, len(myList)))