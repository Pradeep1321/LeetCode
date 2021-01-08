def xorOperation(n, start):
    outarr = []
    val= 0
    for i in range(n):
        val = val ^ (start+2*i)
    return  val


n = 5
start = 0

print(xorOperation(n,start))