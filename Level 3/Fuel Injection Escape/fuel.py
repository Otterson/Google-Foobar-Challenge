def solution(input):
    input = int(input)
    count = 0
    while input >1:
        if input%2==0:
            input /=2
        else:
            if input==3 or input %4==1:
                input = input-1
            else:
                input = input+1
        count+=1
    return count


print(solution('15')) #5
print(solution('4'))  #2
print(solution('37')) #7
print(solution('18')) #5
print(solution('22')) #6
print(solution('1048574'))
print(solution('179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137214'))      #1025
