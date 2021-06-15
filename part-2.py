# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    i = 0
    while len(array) > 0:
        if array[i] == query:
            array.remove(array[i])
            return True
        else:
            array.remove(array[i])
            return search(array, query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 2: return True
    if text[0] != text[-1]: return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    a_str = str(apples)
    b_str = str(oranges)
    
    if not a_str or not b_str:
        return 0
    
    a_last = a_str[-1]
    b_last = b_str[-1]
    
    a_rest = a_str[0:-1]
    b_rest = b_str[0:-1]
    
    if a_last == b_last:
        return 1 + digit_match(a_rest, b_rest)
    else:
        return digit_match(a_rest, b_rest) 

