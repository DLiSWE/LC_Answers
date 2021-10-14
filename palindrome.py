# class checkpalindrome:
x = 12345
y = []
xc = []
class checkpally:
    global x
    global y
    global xc

    def listify(x, y):
        x = abs(x)
        if x < 10:
            y.append(x)
            return y
        
        checkpally.listify(x//10, y)
        y.append(x%10)

    def reverse(xc, y):
        xc.append((y[::-1]))
        return xc    

if __name__ == '__main__':
    checkpally.listify(x,y)
    checkpally.reverse(xc,y)
    # checkpally.checker(xc,x,y)
    if x < 0:
        print('{} is not palindrome.'.format(x))
    elif x > 0:
        if xc[0] == y:
            print('{} is a palindrome.'.format(x))
        else:
            print('{} is not a palindrome'.format(x))
    else:
        print('{} is not a palindrome'.format(x))



