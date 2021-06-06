# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if not n:
        return False
    if n==1 or n==0:
        return n
    else:
        facty = factorial(n-1)
        result = n*facty
        return result
        

def reverse(string):
    if len(string) == 0:
        return ''
    else:
        return reverse(string[1:]) + string[0]


# bunny
def bunny(count):
    bunny = count * 2
    return bunny


# is_nested_parens
def is_nested_parens(thing):
    if not thing:
        return
    is_nested_parens(thing[thing.find('(', 1):thing.rfind(')', 0, len(thing)-1)+1])
    return(thing)