from itertools import permutations, combinations, chain

# Solves all pair shortest path via Floyd Warshall Algorithm 
def floydWarshall(graph): 
    dist = map(lambda i : map(lambda j : j , i) , graph) 
    V = len(graph)
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                dist[i][j] = min(dist[i][j] , 
                                  dist[i][k]+ dist[k][j] 
                                ) 
    for i in range(V): 
        if (dist[i][i] < 0): 
            return -1
    return dist



def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
  
def solution(times, time_limit):
    shortest_paths = floydWarshall(times)
    if shortest_paths == -1:
        return [num for num in range(0, len(times)-2)]
    #print shortest_paths
    num_bunnies = len(times)-2
    ids = []
    for num in range(num_bunnies):
        ids.append(num)
    subsets = powerset(ids)
    saved_bunnies = []
    for sub in subsets:
        for permutation in permutations(sub):
            subsum = 0
            prev = 0
            next = len(times)-1

            for bunny in permutation:
                next = bunny+1
                subsum += shortest_paths[prev][next]
                prev = next
            subsum += shortest_paths[prev][len(times)-1]

            if subsum <= time_limit and len(sub) > len(saved_bunnies):
                saved_bunnies = sub
                if len(saved_bunnies) == num_bunnies:
                    return list(saved_bunnies)
            else:
                pass
    return list(saved_bunnies)

if __name__ == '__main__':
    
    case1 = [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    print("\n\nCase 1: Provided test case 1.\nTime limit: 3")
    for row in case1:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case1, 0)))

    print("\n\nCase 2: Provided test case 2.\nTime limit: 1")
    case2 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
    for row in case2:
        print('', row)
    print("\n  Expected: [1, 2]\nCalculated:", str(solution(case2, 0)))

    print("\n\nCase 3: Infinite negative cycle.\nTime limit: 500")
    case3 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]]
    for row in case3:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case3, 0)))

    print("\n\nCase 4: Max bunnies. None rescuable.\nTime limit: 1")
    case4 = [[1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]]
    for row in case4:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case4, 1)))

    print("\n\nCase 5: One bunny.\nTime limit: 2")
    case5 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    for row in case5:
        print('', row)
    print("\n  Expected: [0]\nCalculated:", str(solution(case5, 2)))

    print("\n\nCase 6: Multiple revisits.\nTime limit: 10")
    case6 = [[0, 5, 11, 11, 1],
             [10, 0, 1, 5, 1],
             [10, 1, 0, 4, 0],
             [10, 1, 5, 0, 1],
             [10, 10, 10, 10, 0]]
    for row in case6:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case6, 10)))

    print("\n\nCase 7: Multiple Revisits 2.\nTime limit: 5")
    case7 = [[0, 10, 10, 10, 1],
             [0, 0, 10, 10, 10],
             [0, 10, 0, 10, 10],
             [0, 10, 10, 0, 10],
             [1, 1, 1, 1, 0]]
    for row in case7:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case7, 5)))

    print("\n\nCase 8: Time travel.\nTime limit: 1")
    case8 = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    for row in case8:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case8, 1)))

    print("\n\nCase 10: Backwards bunny path.\nTime limit: 6")
    case10 = [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]
    for row in case10:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case10, 6)))
    
       