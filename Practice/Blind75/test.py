def isPalindrome(s):
        
    s = s.lower()
    
    l, r = 0, len(s)-1
    
    
    while l <= r:
        if not s[l].isalnum():
            print("not al", s[l])
            l += 1
            
        if not s[r].isalnum():
            print("not al", s[r])
            r -= 1
        
        elif s[l] == s[r]:
            print(s[l], s[r])
            l += 1
            r -= 1
            
        elif s[l] 
    
    return True

isPalindrome("A man, a plan, a canal: Panama")