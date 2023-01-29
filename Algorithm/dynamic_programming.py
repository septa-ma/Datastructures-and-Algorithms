# what is dynamic programming?
# a method for solving optimization problems. a recursive solution that has 
# repeated calls for same inputs, but in Dynamic Programming. The idea is to
# simply store the results of subproblems, so that we do not have to re-compute 
# them when needed later. 
# + Memoization:
# is a specific form of caching that is used in dynamic programming.
# the purpose of caching is to improve the performance of our programs and keep 
# data accessible that can be used later.
# it basically stores the previously calculated result of the subproblem and 
# uses the stored result for the same subproblem.
# + techniques to solve Dynamic Programming Problems:
# - Top-Down Approach: 
# this approach follows the memoization technique. It consists of recursion and
# caching. In computation, recursion represents the process of calling functions
# repeatedly, whereas cache refers to the process of storing intermediate results.
# - Bottom-Up Approach: 
# this approach uses the tabulation technique to implement the dynamic programming 
# solution. it addresses the same problems as before, but without recursion. 
# in this approach, iteration replaces recursion.
# + tabulation or memoization?
# for problems requiring all subproblems to be solved, tabulation typically 
# outperforms memoization by a constant factor. this is because the tabulation 
# has no overhead of recursion which reduces the time for resolving the recursion 
# call stack from the stack memory.
# whenever a subproblem needs to be solved for the original problem to be solved, 
# memoization is preferable since a subproblem is solved lazily, only the 
# computations that are required are carried out.
# + steps to solve a Dynamic programming problem:
# 1- identify if it is a Dynamic programming problem:
#    all the problems that require maximizing or minimizing certain quantities or 
#    counting problems that say to count the arrangements under certain conditions 
#    or certain probability problems can be solved by using Dynamic Programming.
# 2- decide a state expression with the Least parameters:
#    Dynamic Programming problems are all about the state and its transition. 
#    this is the most basic step which must be done very carefully because the 
#    state transition depends on the choice of state definition you make.
#    a state is a collection of characteristics that can be used to specifically 
#    describe a given position or standing in a given challenge. to minimise state 
#    space, this set of parameters has to be as compact as feasible.
# 3- formulate state and transition relationships:
#    it's the hardest part of a solution based on dynamic programming
#    and requires a lot of intuition, observation, and practice.
#    - decide a state for the given problem. 
#    - take a parameter N to decide the state as it uniquely identifies 
#      any subproblem. 
#    - Derive a transition relation between any two states.
#    - Now, need to compute state(N). 
# 4- do tabulation (or memorization):
#    it's the simplest portion of a solution based on dynamic programming. 
#    simply storing the state solution will allow us to access it from memory 
#    the next time that state is needed.

# fibonachi 
def fibonachi(n):
    # decision state or base-case, fib: [0 -> 0, 1 -> 1]
    state = [0, 1]
    for i in range(2, n+1):
        state.append(state[i-1] + state[i-2])
    return state[n]

print(fibonachi(10))
