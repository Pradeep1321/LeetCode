def convert(s: str, numRows: int) -> str:
    nested_list=dict()
    i = 0
    j=0
    if (len(s)<=2) or numRows == 1 :
        return s
    while j < (len(s)) and (len(s)) > numRows:
        while i>= 0 and i < numRows and j< len(s):
                nested_list.setdefault(i,[]).append(s[j])
                i=i+1
                j=j+1
        i=i-2
        while i>= 0 and i <= numRows and j < len(s):
                nested_list.setdefault(i, []).append(s[j])
                i=i-1
                j=j+1
        i=i+2
    flat = []
    for i in (nested_list.values()):
        for j in i:
            flat.append(j)

    return "".join(flat)

print(convert("abc",2))