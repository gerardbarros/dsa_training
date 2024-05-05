'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "left, right
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

def validPalindrome(str):
# Solution using built in methods
    # newStr = ''

    # for char in str:
    #     if char.isalnum():
    #         newStr += char.lower()
    # return newStr == newStr[::-1]

# Solution using pointers:
# def validPalindrome(str):
    l,r = 0, len(str) - 1

    while l < r:
        while l and not alphaNum(str[l]):
            l += 1
        while r > l and not alphaNum(str[r]):
            r -= 1
        if str[l].lower() != str[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

def alphaNum(char):
    return (ord('A') <= ord(char) <= ord('Z') or 
        ord('a') <= ord(char) <= ord('z') or 
        ord('0') <= ord(char) <= ord('9'))


print(validPalindrome('A man, a plan, a canal: Panama'))
print(validPalindrome('Racecar'))
print(validPalindrome('Taco cat'))
print(validPalindrome('Sphinx'))