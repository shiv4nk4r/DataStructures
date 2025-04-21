# https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=9colawc6

def firstUniqChar(s: str) -> int:
    occuranceTable = {}
    # Update occurance table
    for char in s:
        if char in occuranceTable:
            occuranceTable[char] = occuranceTable[char] + 1
        else:
            occuranceTable[char] = 1

    for i in range(0, len(s)):
        if occuranceTable[s[i]] == 1:
            return i
        
    return -1
        