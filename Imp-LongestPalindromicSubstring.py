
def longestPalindrome(s: str) -> str:
    le = len(s)
    lstr = ""
    lstrlen = 0
    for i in range(len(s)):
        #odd length
        left,right = i,i
        while left >=0 and right < len(s) and s[left]==s[right]:
            if(right-left+1)>lstrlen:
                lstrlen=right-left+1
                lstr=s[left:right+1]
            left -= 1
            right += 1
        left,right = i, i+1
        while left >=0 and right < len(s) and s[left] == s[right]:
            if (right-left+1) > lstrlen:
                lstrlen = right-left+1
                lstr = s[left:right+1]
            left -= 1
            right += 1
    return lstr
def longestPalindrome1(s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res


print(longestPalindrome("malayalam"))
print(longestPalindrome1("malayalam")) #aacabbbbdkacaa"))