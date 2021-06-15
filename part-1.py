# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError ("Cannot use negative numbers")
    if n == 0:
        return 1

    return n * factorial(n - 1)


# reverse
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


# bunny
def bunny(count):
    if count == 1:
        return 2
    return count * 2


# is_nested_parens
def is_nested_parens(parens):
    while "()" in parens or "{}" in parens or '[]' in parens:
        parens = parens.replace("()", "").replace('{}', "").replace('[]', "")
    return parens == ''

