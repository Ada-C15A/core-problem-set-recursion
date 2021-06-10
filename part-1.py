# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    if n > 0:
        return n * factorial(n-1)
    

# reverse

def reverse(text):
    if len(text) <= 1:
        return text
    
    return text[-1] + reverse(text[:-1])

# bunny

def bunny(count):
    if count == 0:
        return 0
    if count == 1:
        return 2
    
    return 2 + bunny(count -1)

# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if len(parens) == 1:
        return False
    return (parens[0] == "(" and parens[-1] == ")") and is_nested_parens(parens[1:-1])

# CHALLENGE FOR is_nested_parens
def is_nested_parens2(parens):
    if len(parens) == 0:
        return True
    if len(parens) == 1:
        return False
    if len(parens) == 2:
        return (parens[0] == "(" and parens[-1] == ")")

    front_index = 1
    back_index = len(parens)-1
    
    def are_matched(parens,front_index,back_index):
        if len(parens) % 2 == 1:
            return False
        if front_index > len(parens) // 2 or back_index <= len(parens) // 2:
            return True
        return parens[front_index] == "(" and parens[back_index] == ")" and are_matched(parens, front_index+1, back_index-1)

    return (parens[0] == "(" and parens[-1] == ")") and are_matched(parens,front_index,back_index)