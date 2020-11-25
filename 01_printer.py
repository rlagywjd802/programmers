from _collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque(priorities)
    while queue:
        first = queue.popleft()
        location -= 1
        if len(queue) == 0:
            max_priority = -1
        else:
            max_priority = max(queue)
        if first < max_priority:
            queue.append(first)
            if location < 0:
                location = len(queue)-1
        else:
            if location == -1:
                return answer
            else:
                answer += 1

queue =  [(i,p) for i,p in enumerate([2, 1, 3, 2])]
print(queue)
# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 1))