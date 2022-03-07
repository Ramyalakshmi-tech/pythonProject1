def isPalindrome(s):
    return s==s[::-1]

s=input("Enter string")
ans=isPalindrome(s)
if ans:
    print("yes")
else:
    print("No")