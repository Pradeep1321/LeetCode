import random
def generateTheString(n):
    output= ''
    if n % 2 == 0:
        ele1 = chr(random.randint(97,122))
        output = ele1*(n-1)
        ele2 = chr(random.randint(97, 122))
        while ele1 == ele2:
            ele2 = chr(random.randint(97, 122))
        output+=ele2
    else:
        ele1 = chr(random.randint(97,122))
        output = ele1 * n
    return output
n=4
print(generateTheString(n))

