
y = []
xc = []

class Solution:
    global x
    global y
    global xc
    
    def isPalindrome(self, x: int) -> bool:
        self.x = abs(x)
        if x < 10:
            self.y.append(x)
            return y
        
        Solution.isPalindrome(x//10, y)
        self.y.append(x%10)
        
        self.xc.append((y[::-1]))
        
        if x < 0:
            print('{} is not palindrome.'.format(x))
        elif x > 0:
            if self.xc[0] == self.y:
                print('{} is a palindrome.'.format(x))
            else:
                print('{} is not a palindrome'.format(x))
        else:
            print('{} is not a palindrome'.format(x))

    
Solution.isPalindrome(12345)