# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr, query):
    if len(arr) == 0:
        return False
    if arr[0] == query or arr[-1] == query:
        return True
    else:
        return search(arr[1:-1], query)


# is_palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


# digit_match

def digit_match(apples, oranges):
    a_str = str(apples)
    o_str = str(oranges)

    if not a_str or not o_str:
        return 0

    if a_str[-1] == o_str[-1]:
        return 1 + digit_match(a_str[:-1], o_str[:-1])
    else:
        return digit_match(a_str[:-1], o_str[:-1])
