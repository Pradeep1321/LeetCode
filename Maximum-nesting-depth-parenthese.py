def maxDepth(s):
    res = cur = 0
    for c in s:
        if c == '(':
            cur += 1
            res = max(res, cur)
        if c == ')':
            cur -= 1
    return res

s = "(1+(2*3+((8)/4))+1"
print(maxDepth(s))
