# def solution(skill, skill_trees):
#     answer = 0
#     for i in range(len(skill_trees)):
#         # 하나의 스킬트리(문자열)에서 skill에 포함된 문자열이 있는지를 검색
#         # skill에 포함된 문자의 순서대로 값을 매긴다고 가정하면
#         # 만약에 현재 매기려는 값이 max_val보다 작으면 break
#         # 아니면 값을 max_val 값을 업데이트
#         # 문자열 하나를 break 없이 끝까지 돌았을 경우 answer +1
#         print("")
#         max_val = -1
#         for j in range(len(skill_trees[i])):
#             cur = -1
#             for k in range(len(skill)):
#                 if skill_trees[i][j] == skill[k]:
#                     cur = k
#                     break
#             print(j, skill_trees[i][j], cur, max_val)
#             if max_val == -1 and cur > 0:
#                 answer -= 1
#                 break
#             if cur < max_val:
#                 if cur > -1:
#                     answer -= 1
#                     break
#             else:
#                 max_val = cur
#         answer += 1
#         print(skill_trees[i], answer)
#
#     return answer

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        # 하나의 스킬트리(문자열)에서 skill에 포함된 문자열이 있는지를 검색
        # skill에 포함된 문자의 순서대로 값을 매긴다고 가정하면
        # 만약에 현재 매기려는 값이 max_val보다 작으면 break
        # 아니면 값을 max_val 값을 업데이트
        # 문자열 하나를 break 없이 끝까지 돌았을 경우 answer +1
        print("")
        max_val = -1
        for j in range(len(skill_trees[i])):
            cur = -1
            for k in range(len(skill)):
                if skill_trees[i][j] == skill[k]:
                    cur = k
                    break
            print(j, skill_trees[i][j], cur, max_val)
            if max_val == -1 and cur > 0:
                answer -= 1
                break
            if cur < max_val:
                if cur > -1:
                    answer -= 1
                    break
            else:
                max_val = cur
        answer += 1
        print(skill_trees[i], answer)

    return answer

# def solution(skill, skill_trees):
#     cnt = 0
#     for tree in skill_trees:
#         a = [tree.index(i) for i in skill if i in tree]
#         a_ = sorted(a)
#         if a == a_ and all(i in tree for i in skill[:len(a)]):
#             cnt += 1
#     return cnt
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CBD"]))