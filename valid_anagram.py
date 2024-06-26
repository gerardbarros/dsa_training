'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''

#create hash set and determine if character in set1 is already in set2. if it is they are an anagram
#check length 

def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for char in countS:
        if countS[char] != countT.get(char, 0):
            return False
        
    return True
    #can also use Counter(s) == Counter(t) since python can count chars for you in an arr
    '''
    Follow up: 
        return sorted(s) == sorted(t)
        not the most efficient solution 
    '''