# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if array == []:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    return (text[0] == text[-1]) and is_palindrome(text[1:-1])

# CHALLENGE FOR is_palindrome
def is_palindrome2(text):
    tlen = len(text)
    if tlen <= 1:
        return True
    if tlen <= 3:
        return (text[0] == text[-1])
    
    front_index = 1
    back_index = tlen - 2
    
    def chars_match(text, front_index, back_index):
        if front_index > len(text) // 2 or back_index < len(text) //2:
            return True
        return (text[front_index] == text[back_index]) and chars_match(text,front_index+1,back_index-1)

    return (text[0] == text[-1]) and chars_match(text, front_index, back_index)

# digit_match

def digit_match(num1,num2):
    n1 = str(num1)
    n2 = str(num2)
    if not n1 or not n2:
        return 0
    
    match = 1 if n1[-1] == n2[-1] else 0
    
    if len(n1) == 1 or len(n2) == 1:
        return match
    else:
        return match + digit_match(n1[:-1],n2[:-1])
    
