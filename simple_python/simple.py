from http.cookiejar import uppercase_escaped_char


def is_even(number):
    return number % 2 == 0
print(is_even(10))
print(not not is_even(10))

print(f'\nNext ****************\n')

def has_capital_letters(string):
     return any(char.isupper() for char in string)
# print(has_capital_letters("Hello"))
def is_correct_password(password):
    length = len(password)
    return length >8 and has_capital_letters(password)
print(is_correct_password("dsasdasdasdaA"))
print(is_correct_password("dsaA"))
print(is_correct_password("DSA"))

print(f'\nNext ****************\n')

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
def is_not_palindrome(word):
    return not is_palindrome(word)
print (is_palindrome("addddA"))
print (is_not_palindrome("addddA"))
print('asdfg'[::-1])

print(f'\nNext ****************\n')

print(0 or False or '' or [] or 42 or "Hello")

print(f'Use new branch main-fix')