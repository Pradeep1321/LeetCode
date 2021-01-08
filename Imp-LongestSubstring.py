def longestSubstring(s):
    window_start = 0
    max_length = 0
    char_map = {}
    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in char_map:
            window_start = max(window_start, char_map[right_char] + 1)
            print(window_start)

        char_map[right_char] = window_end
        print(char_map)

        max_length = max(max_length, window_end - window_start + 1)
        print(max_length)
        print("-------")

    return max_length
print(longestSubstring("abcccwefcghfijkccab"))

def lengthOfLongestSubstring1(s):
        result = 0
        lenS = len(s)
        for i in range(lenS):
            count = 0
            for j in range(i, lenS):
                if s[j] not in s[i:j]:
                    count += 1
                else:
                    break

            if count > result:
                result = count

        return result


print(lengthOfLongestSubstring1("abcccwefcghfijkccab"))