def removeOuterParentheses(S):
    output = ''
    left=0
    right = 0
    for i in range(len(S)):
        if S[i] == "(":
            left+=1
        if S[i] == ")" and left >= 1:
            right+=1
        if left == right:
            output+=(S[i+1-(left+right-1):i])
            left=right=0
    return output




st = "()(()())(())(()(()))"

print(removeOuterParentheses(st))