# https://leetcode.com/problems/is-subsequence/description/?envType=problem-list-v2&envId=9colawc6

def isSubsequence(s: str, t: str) -> bool:
    characterMap = {}

    for char in t:
        if char in characterMap:
            characterMap[char] += 1
        else:
            characterMap[char] = 1
            
    for char in s:
        if char in characterMap and characterMap[char] > 0:
            characterMap[char] -= 1
        else:
            return False
    
    return True

print(isSubsequence("acb", "ahbgdc"))