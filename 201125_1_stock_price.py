# def solution_failed(prices):
#     answer = []
#     for i in range(0, len(prices)):
#         cur = prices[i]
#         count = 0
#         for future in prices[i+1:len(prices)]:
#             # 현재 값이 미래 값보다 작거나 같으면 떨어지지 않은 것
#             if cur <= future:
#                 count += 1
#         answer.append(count)
#     return answer

# list의 slicing 시간(A[a:b])은 O(b-a)
# def solution_time_over(prices):
#     answer = []
#     n = len(prices)
#     for i in range(0, n):
#         cur = prices[i]
#         count = 0
#         for future in prices[i+1:n]:
#             # 현재 값이 미래 값보다 작거나 같으면 떨어지지 않은 것
#             if cur <= future:
#                 count += 1
#             else:
#                 count += 1
#                 break
#         answer.append(count)
#     return answer

# https://gurumee92.tistory.com/170
def solution1(prices):
    n = len(prices)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1

            if prices[i] > prices[j]:
                break

    return answer

def solution2(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성
    st = []
    # 3. 0 ~ n-1 초까지 순회
    for i in range(n):
        # 1. 스택 비지 않고, prices[top] > prices[i] 이라면 다음 반복
        # 1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 1-2. answer[top]에 i - top을 저장
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top
        # 2. 스택에 현재 시간 i 저장
        st.append(i)

    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        # 1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = st.pop()
        answer[top] = n - 1 - top

    return answer

print(solution1([1, 2, 3, 2, 3]))
print(solution2([1, 2, 3, 2, 3]))