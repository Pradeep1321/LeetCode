def maximum69Number (num) :
    ns = str(num)
    out=''
    i = 0
    while i <  len(ns):
        if (ns[i]) == '9':
            out=out+ns[i]
        else:
            out = out + '9'
            out=out+ns[i+1:]
            break
        i+=1
    return int(out)




num = 9996

print(maximum69Number(num))