def toLowerCase(str):
    st = ''
    for i in str:
        if 64 < ord(i) < 91:
            st += (chr(ord(i) + 32))
        else:
            st += i
    return st

str= '"al&phaBET"'
print(toLowerCase(str))

