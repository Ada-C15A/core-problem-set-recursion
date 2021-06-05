# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(list, query):
    if len(list) == 0:
        return False
    if list[0] == query:
        return True
    return search(list[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] == text[len(text) - 1]:
        return is_palindrome(text[1:len(text) - 1])
    else:
        return False

# digit_match
def digit_match(num_1, num_2):
    string_1 = str(num_1)
    string_2 = str(num_2)

    if not string_1 or not string_2:
        return 0
    one_last = string_1[-1]
    two_last = string_2[-1]

    rest_of_1 = string_1[0:-1]
    rest_of_2 = string_2[0: -1]

    if one_last == two_last:
        return 1 + digit_match(rest_of_1, rest_of_2)
    else:
        return digit_match(rest_of_1, rest_of_2)

