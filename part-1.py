# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# reverse
def reverse(word):
    if word == "":
        return word
    else:
        return reverse(word[1:])+word[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    elif count == 1:
        return 2
    else:
        return bunny(count-1)+2


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True

    if len(parens) == 1:
        return False

    else:
        if parens[0] == "(" and parens[-1] == ")":
            return is_nested_parens(parens[1:-1])
        else:
            return False
