# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Number must be greater than zero")
    elif n == 0:
        return 1
    return n * factorial(n - 1)


# reverse
def reverse(word):
    if len(word) <= 1:
        return word
    return word[-1] + reverse(word[1:-1]) + word[0]



# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    return False if not (parens[0] == '(' and parens[-1] == ')') else is_nested_parens(parens[1:-1])
'''
I'm curious about the solution for the Challenge. I don't really understand the hint. 
    It said: For an additional challenge, implement is_nested_parens 
    without creating new strings in the process of solving the problem.
    HINT said: Sometimes we create extra helper functions that can store more information 
    in their parameters than we might use in the main solution function.
'''
