from collections import deque

def get_available_moves(map, cell): 
    x = [0,0,-1,1]
    open_moves=[]

    for i in range(0,4):
        try: 
            remove_wall = cell[2]
            if cell[0] + x[3-i] >= 0 and cell[1] + x[i] >=0:
                move = [cell[0] + x[3-i],cell[1] + x[i]]
                if map[move[0]][move[1]] == 0:
                    open_moves.append((move[0],move[1],remove_wall))
                if map[move[0]][move[1]] == 1  and remove_wall==1:
                    open_moves.append((move[0],move[1], 0))
        except IndexError:  #handles out of bound on map indexing
            pass
    return open_moves
    
    
def solution(map):
    cell = (0,0,1)  #start cell, third argument: 0 = wall removed, 1 = wall removal available
    move_queue = deque([cell])
    node_lengths = {cell:1}
    while move_queue:
        move = move_queue.popleft()
        if move[0] == len(map)-1 and move[1]==len(map[0])-1: return node_lengths[move]
        available_moves = get_available_moves(map,move)
        for node in available_moves:
            if node not in node_lengths:    #prevents cell revisits
                #print(node)
                node_lengths[node] = node_lengths[move] + 1
                move_queue.append(node)
            else: pass
           
    
# print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
