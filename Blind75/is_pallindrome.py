def isPalindrome(s):
    
    s = s.lower()
    left, right = 0, len(s)-1    
    
    while left <= right:

        if s[left].isalnum() and s[right].isalnum():
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break

        else:
            if s[left].isalnum():
                right -= 1
            else:
                left += 1

    if left <= right:
        return False
    else:
        return True
        

print(isPalindrome("A man, a plan, a canal: Panama"))