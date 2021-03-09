def solution(array, commands):
    answer = []
    for iter in range(len(commands)):
    # print(commands[0][0])
        i,j,k = commands[iter][0],commands[iter][1],commands[iter][2]
        array_split = array[i-1:j]
        array_split.sort()
        array_final = array_split[k-1]
        answer.append(array_final)
    return answer