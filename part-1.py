# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0 :
        raise ValueError
    elif n ==0 :
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    
    if text=="":
        return ""
    elif len(text)==0:
        return text
    slicing=slice(1,len(text))
    return reverse(text[slicing]) + text[0]
    
    


# bunny

def bunny(count):
    if count ==0:
        return 0
    elif count ==1:
        return 2
    return bunny(count-1) + 2

# is_nested_parens

def is_nested_parens(parens):
 
    parens_pair={
        ")":"("
    }
    
    if len(parens) == 0:
        return True
    
    elif parens[0] == parens_pair[")"]:
       
       
        return is_nested_parens(parens[1:-1])
    else:
      return False
