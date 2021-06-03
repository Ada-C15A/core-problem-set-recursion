# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, value):
    if not array: 
        return False
    return (array[0] == value or search(array[1:], value))


# is_palindrome
def is_palindrome(word):
    if len(word) in {0,1}:
        return True
    return (word[0] == word[-1] and is_palindrome(word[1:-1]))
'''
I'm curious about the challenge, but I don't really understand where in the solution 
in Learn (or in mine) new strings were being created.
Challenge says: 
For an additional challenge, implement is_palindrome without creating 
new strings in the process of solving the problem.
'''

# digit_match
# 2 solutiomns:
# My original solution - it works, but changes the requested methhod signature
def digit_match(num1, num2, count = 0):
    if num1//10 == 0 or num2//10 == 0:
        if num1%10 == num2%10:
            count += 1
        return count 

    if num1%10 == num2%10:
        count += 1
    return digit_match(num1//10, num2//10, count)

# Improved solution
def digit_match(num1, num2):
    if num1//10 == 0 or num2//10 == 0:
        return 1 if num1%10 == num2%10 else 0

    if num1%10 == num2%10:
        return 1 + digit_match(num1//10, num2//10)
    return digit_match(num1//10, num2//10)

