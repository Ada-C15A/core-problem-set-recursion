# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if not array: 
        return False
    if array[-1] == query:
        return True
    
    return search(array[:-1], query)


# is_palindrome

def is_palindrome(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    
    if string[0] != string[-1]:
        return False
    
    return is_palindrome(string[1:-1])


# digit_match

def digit_match(apples, oranges):
    # if not apples or not oranges:
        # return 0
        # Why does this check need to be done after it is turned
        # into a string? can't do it here on like 2... 
    string_apple = str(apples)
    string_oranges = str(oranges)
    
    if not string_apple or not string_oranges:
        return 0
    
    if string_apple[-1] == string_oranges[-1]:
        return 1 + digit_match(string_apple[:-1], string_oranges[:-1])
    
    return digit_match(string_apple[:-1], string_oranges[:-1])
    