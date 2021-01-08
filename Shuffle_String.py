def restoreString(s,indices):
    test = dict()
    st =''
    for i in range(len(indices)):
        test[indices[i]]=s[i]
    st = "".join(test[key] for key in sorted(test.keys()))
    return st

def restoreString1(s,indices):
    answer = ""
    for i in range(len(s)):
        answer += s[indices.index(i)]
    return answer

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

restoreString1(s,indices)
