'''
Given a string s, find the length of the longest 
substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

def lengthOfLongestSubstr(s):
    charSet = set()
    l = 0
    res = 0

    #right  pointer keeps changing while going through every char
    for r in range((len(s))):
        #update window in set when run into a dupe
        while s[r] in charSet:
            #take left char and remove from set
            charSet.remove(s[l])
            # update left pointer
            l += 1
        #after removeing dupes add right most char to set
        charSet.add(s[r])
        # update result
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstr('abcabcbb'))