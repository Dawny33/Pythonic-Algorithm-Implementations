##Yippee, I've managed to pull off a one liner this time.

#Recursion implementation of a palindrome checker.

def palin_rec(target):
    return (not target) or (target.lower()[0] == target.lower()[-1] and palin_rec(target.lower()[1:-1]))


print palin_rec("Malayalam")