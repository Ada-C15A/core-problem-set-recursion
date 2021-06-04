# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError
    return factorial(num - 1) * num


# reverse
def reverse_word(word_string):
    if len(word_string) == 1 or len(word_string) == 0:
        return word_string

    last_letter = word_string[-1]
    rest_of_word = word_string[:-1]

    return last_letter + reverse_word(rest_of_word)


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count - 1) + 2


# is_nested_parens
def check_set(parens_pair):
    return parens_pair == ("(", ")")

def is_nested_parens(string_of_parens):
    if len(string_of_parens) == 0:
        return True
    elif string_of_parens[:1] != "(" or string_of_parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(string_of_parens[1:-1])

