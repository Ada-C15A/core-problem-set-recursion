# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query: 
        return True
    return search(array[1:], query)
    

# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    if len(text) < 2 :
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    if not num1 or not num2:
        return False
    matching_pairs = 0
    matches = []
    while num1[-1] == num2[-1]:
        matches = matching_pairs - 1
        return digit_match(num1, num2)
    return matches
