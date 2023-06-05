def firstUniqChar(s):
    char_freq = {}

    # Count the frequency of each character
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    return -1

s = 'aabb'
print(firstUniqChar(s))
