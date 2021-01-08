def uniqueMorseRepresentations(words) :
    out=[]
    wod = ''
    count = 0
    abclist = []
    abclist.extend(range(97, 123))

    actual= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    wordmap = dict(zip(abclist,actual))

    for word in words:
        wod = ("".join([wordmap[(ord(s))] for s in word]))
        if wod not in out :
            out.append(wod)
            count+=1
        else:
            out.append(wod)
        print(out)
    return count



#words = ["gin", "zen", "gig", "msg"]
words = ["a"]
#words  = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
print(uniqueMorseRepresentations(words))