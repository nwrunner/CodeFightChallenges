'''
You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

Example

For n = 1, the output should be
climbingStairs(n) = 1;

For n = 2, the output should be
climbingStairs(n) = 2.

You can either climb 2 steps at once or climb 1 step two times.
n: 17, output = 2584
n: 13, output = 377
'''
def climbingStairs(n):
    
    # do it the "bad" way and reverse engineer the dynamic way
    if n <= 3:
        return n

    #return climbingStairs(n-1) + climbingStairs(n-2)
    prev = 3
    prev2 = 2
    for i in range(4,n+1):
        tmp = prev + prev2
        prev2 = prev
        prev = tmp
        
    return tmp

n = 13
print (climbingStairs(n), n)
