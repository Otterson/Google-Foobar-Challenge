import itertools
import numpy as np
from copy import copy, deepcopy
count = 0

cell_true = [
    [1, 0,
    0, 0],
    [0, 1,
    0, 0],
    [0, 0,
    1, 0],
    [0, 0,
    0, 1]
]

cell_false = [
    [0, 0,
    0, 0],
    [1, 1,
    0, 0],
    [1, 0,
    1, 0],
    [1, 0,
    0, 1],
    [0, 1,
    1, 0],
    [0, 1,
    0, 1],
    [0, 0,
    1, 1],
    [1, 1,
    1, 0],
    [1, 1,
    0, 1],
    [1, 0,
    1, 1],
    [0, 1,
    1, 1],
    [1, 1,
    1, 1]
]

#this implementation is als more sophisticated brute force solution. Basically each group of values is checked for compatability with surrounding groups.
#if a possible configuration works with the surrounding cell, the function is recursively called for the next index and the function continues.
#if not, the function returns and the previous cell continues to list through the options.
#base case: the bottom right cell is called and if a match is found, it can be assumed that all other indices have matching possible options, therfore a match with the given matrix has been found
def check_subgrid(i,j,width, height, expanded):
    global count

    if expanded[i][j] == True:
        options = cell_true
        #print("grid[",i,"][",j,"] is True")
    else:
        options = cell_false
        #print("grid[",i,"][",j,"] is False")


    #if the top row is being evaluated then only the values on the left have to be checked for a match
    if i==0:
        if j==0:
            for option in options:
                expanded[0][0] = option
                check_subgrid(i, j+1, width, height, deepcopy(expanded))
        elif j<width:
            for option in options:
                
                if option[0] == expanded[i][j-1][1] and option[2] == expanded[i][j-1][3]:
                    expanded[i][j] = option
                    if j==(width-1):
                        check_subgrid(i+1,0, width, height, deepcopy(expanded))
                    else:
                        check_subgrid(i,j+1, width, height, deepcopy(expanded))
            return

    #Otherwise the top and left cells must be checked as well
    else:
        if j==0:
            for option in options:
                if (option[0] == expanded[i-1][j][2] and option[1] == expanded[i-1][j][3]):
                    expanded[i][j] = option
                    check_subgrid(i,j+1, width, height, deepcopy(expanded))
        elif j<width:
            for option in options:
                if (option[0] == expanded[i][j-1][1] and option[2] == expanded[i][j-1][3]) and (option[0] == expanded[i-1][j][2] and option[1] == expanded[i-1][j][3]):
                    expanded[i][j] = option
                    if j==width-1 and i==height-1:
                        count = count+1
                    elif j==width-1:
                        check_subgrid(i+1,0, width, height, deepcopy(expanded))

                    else:
                        check_subgrid(i,j+1, width, height, deepcopy(expanded))
            
        



def solution(g):
    global count
    count = 0
    width = len(g[0])
    height = len(g)

    check_subgrid(0,0, width, height, g)
    return count


print "Should be 11567:   ", solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
print "Should be 4:   ", solution([[True, False, True], [False, True, False], [True, False, True]])
print "Should be 254:   ", solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])