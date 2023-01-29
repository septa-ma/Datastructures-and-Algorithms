# what is recursion?
# it is a consept of programming not data structure or algorithm just a way that we solve a problem.
# a function calls itself directly or indirectly is called recursion.
# a way of taking a problem and breaking it down into subproblems and then each of
# those subproblems is generally broken down into more and more subproblems.
# we need to have a base case if don't have it recursion runs for ever.
# tree and graph traversing use this consept.
# you can code all the recursion problems with iterative.
# Recursion:                                                        Iteration:
# 1- terminates when the base case becomes true.	                terminates when the condition becomes false.
# 2- used with functions.	                                        used with loops.
# 3- every recursive call needs extra space in the stack memory.	every iteration does not require any extra space.
# 4- smaller code size.	                                            larger code size.

# 1- calculate n! recursively
def factoriel(number):
    if number <= 1:
        return 1
    else:
        return number * factoriel(number-1)

print(factoriel(5))

# 2- fibonachi recursively
def fibonachi(number):
    if number == 0:
        return 0
    if number == 1 or number == 2:
        return 1
    else:
        return fibonachi(number - 1) + fibonachi(number - 2)

n = 8
for i in range(0, n):
    print(fibonachi(i), end=" ")