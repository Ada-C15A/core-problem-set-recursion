# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    elif query not in array:
        return False
    
    return search(array[1:],query)
        
        


# is_palindrome
def is_palindrome(text):
    if len(text) == 0 or len(text) ==1:
        return True
    elif text[0] !=text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match

#  It has not passing the tests
def digit_match(num1, num2):
    counter = 0
    num1=list(str(num1))
    num2=list(str(num2))

    if num1.index(num1[-1]) == 0 or num2.index(num2[-1]) == 0:
        return counter 
    if num1[-1] == num2[-1]:
        counter+=1
    return digit_match(num1[::-1],num2[::-1])
