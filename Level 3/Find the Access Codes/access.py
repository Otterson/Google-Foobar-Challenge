
#
# def solution(l):
#     tuples = []
#     if len(l) <3:
#         return 0
#     else:
#         for i in range(0, len(l)):
#             for j in range(i+1,len(l)):
#                 if l[j] != l[i] and l[j]%l[i]==0 and l[i] <= l[j]:
#                     for k in range(j+1, len(l)):
#                         if l[k]%l[j]==0 and l[j]<=l[k]:
#                             tuples.append([l[i],l[j],l[k]])
#     print(tuples)
#     return len(tuples)


def solution(l):
    tuple_count = 0
    tuple_list = [ [l[0]] ]
    if len(l)<3: return 0
    for i in range(1, len(l)):
        #print(tuple_list)
        exists_base = False
        for tuple in tuple_list:
            if tuple[0] == l[i]: exists_base = True
            if len(tuple)==1:
                if l[i] % tuple[0] == 0:
                    tuple.append(l[i])
            elif len(tuple)==2:
                if l[i] % tuple[0]==0:
                    tuple_temp = list(tuple)
                    tuple_temp[1] = l[i]
                    #if tuple_temp not in tuple_list:
                    tuple_list.insert(0,tuple_temp)
                if l[i] % tuple[1]==0:
                    tuple_count+=1
                    tuple.append(l[i])
            elif len(tuple)==3:
                if l[i] % tuple[1] == 0:
                    tuple_temp = list(tuple)
                    tuple_temp[2] = l[i]
                    #if tuple_temp not in tuple_list:
                    tuple_count+=1
                    tuple_list.insert(0,tuple_temp)
        if not exists_base: tuple_list.append([l[i]])

    tuple_list.sort()
    for tuple in tuple_list:
        if len(tuple) == 3:
            print(tuple)
    return tuple_count

print(solution([1,1,1]))        #1
print(solution([1,1]))
print(solution([1,2,3,4,5,6]))  #3
print(solution([2,4,6,8,10,12,14,16]))
print(solution([2,4,8,8,5,10,15,20,22,24,30,16,1]))
print(solution([3,7,8,11,18]))
print(solution([1,2,4,8]))
print(solution([1,3,5,7,9,11,13,15,17,19,21]))
print(solution([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,10,10,10]))
print(solution([9,8,7,6,5,4,3,2,1]))
