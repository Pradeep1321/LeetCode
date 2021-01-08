def freqAlphabets(s):
    output = ''
    length = len(s)-1
    while length >= 0 :
        if s[length] == "#":
            output+=chr(int(s[(length-2):length])+96)
            length-=3
        else:
            output += chr(int(s[length]) + 96)
            length-=1
    output=output[::-1]
    return output

s = "10#11#12"
print(freqAlphabets(s))