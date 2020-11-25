def solution(n):
    answer = ''
    if (n - 1) // 3 == 0:
        if (n - 1) % 3 == 0:
            answer = '1'
        elif (n - 1) % 3 == 1:
            answer = '2'
        elif (n - 1) % 3 == 2:
            answer = '4'
        return answer
    else:
        up = (n-1) // 3
        down = ((n-1) % 3) + 1
        return solution(up) + solution(down)

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(19))