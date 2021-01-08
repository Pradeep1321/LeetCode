def balancedStringSplit(s):
    count = 0
    lcount = 0
    rcount = 0
    for st in s:
        if st == 'R':
            lcount+=1
        else:
            rcount+=1
        if lcount == rcount:
            count+=1
    return count



s = "RLRRLLRLRL"
print(balancedStringSplit(s))
