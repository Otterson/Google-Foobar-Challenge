

def stingy(total_lambs):   #basically fibonacci
    pay = [1,1]
    counter = 2
    track_sum = 2
    if total_lambs ==1: return 1

    while True:
        if track_sum + pay[counter-2] + pay[counter-1] > total_lambs: break
        fib_pay = pay[counter-1] + pay[counter-2]
        pay.append(fib_pay)
        track_sum += fib_pay
        counter+=1

    print("Stingy("+str(total_lambs)+"): "+str(counter-1))

    return counter-1
        


def generous(total_lambs):     #2^n
    counter = 0
    track_sum = 0
    if total_lambs <= 2: return 1

    while True:
        track_sum += 2**counter
        if track_sum + 2**(counter+1) > total_lambs: break
        counter+=1
    print("Generous("+str(total_lambs)+"): "+str(counter))
    print("")
    return counter




def solution(total_lambs):

    diff = stingy(total_lambs)-generous(total_lambs)
    return diff


print("Solution(10): " + str(solution(10)))
print("Solution(143): " + str(solution(143)))
print("Solution(1): " + str(solution(1)))

print("Solution(2): " + str(solution(2)))
print("Solution(3): " + str(solution(3)))
print("Solution(4): " + str(solution(4)))


