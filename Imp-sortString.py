def sortString(s) :
    chars = [0] * 26
    for char in s:
        chars[ord(char) - ord('a')] += 1

    res = []

    while sum(chars)>0:
        for lo in range(len(chars)):
            if chars[lo] > 0:
                res.append(lo)
                chars[lo] -= 1

        for hi in range(len(chars) - 1, -1, -1):
            if chars[hi] > 0:
                res.append(hi)
                chars[hi] -= 1

    res = [chr(x + 97) for x in res]
    return "".join(res)

print(sortString("leetcode"))

