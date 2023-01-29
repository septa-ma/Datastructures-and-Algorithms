# what is greedy?
# a method for solving optimization (minimization or maximization) problems by 
# taking decisions that result in the most evident and immediate benefit 
# irrespective of the final outcome.
# structure of all greedy algorithms: 
# - declare an empty result = 0.
# - make a greedy choice to select, If the choice is feasible 
#   add it to the final result.
# - return the result.

# job sequencing
# 1-sort all jobs in decreasing order of profit.
# 2-iterate on jobs in decreasing order of profit.
# for each job:
# - find a time slot i, put the job in this slot.
# - if no such i exists, then ignore the job.
def jobSeqencing(myJobs):
    # 1- sort jobs based on profits
    myJobs.sort(key=lambda x: x[2])
    result = []
    temp = []
    # 2- iteration on jobs
    for i in range(len(myJobs)-1, -1, -1):
        # - make an empty slot
        slot = myJobs[i][1] - myJobs[i-1][1]
        temp.append((myJobs[i][2], myJobs[i][1], myJobs[i][0]))
        # - if there is an empty slot fill it with the job
        if slot and temp:
            job = temp.pop(0)
            slot -= 1
            result.append(job[2])

    return result



myJobs = [ ['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]
           
print(jobSeqencing(myJobs))