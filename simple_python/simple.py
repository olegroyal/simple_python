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
    return length > 8 and has_capital_letters(password)


print(is_correct_password("dsasdasdasdaA"))
print(is_correct_password("dsaA"))
print(is_correct_password("DSA"))

print(f'\nNext ****************\n')


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)


print(is_palindrome("addddA"))
print(is_not_palindrome("addddA"))
print('asdfg'[::-1])

print(f'\nNext ****************\n')

print(0 or False or '' or [] or 42 or "Hello")
print(f'Use new branch main-fix')
print(False or 232 or '')

print(f'\nNext ****************\n')


def is_even_log(number):
    return (number % 2 == 0 and 'Yes' or 'No')
print(is_even_log(11))

def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'
print(string_or_not('hello'))
print(string_or_not(3))

print(f'\nNext ****************\n')

def guess_number(number):
    if number == 42:
        return 'You win!'
    return 'Try again!'
print(guess_number('hello'))
print(guess_number(42))
print(guess_number(3))

print(f'\nNext ****************\n')

def normalize_url(address):
    source = 'https://'
    if address[:8] == source:
        return  address
    else:
        if address[:7] == 'http://':
            return source + address[7:]
        else:
            return source + address

print(normalize_url('aa.com'))


print(f'\nNext ****************\n')

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    elif last_char == '*':
        sentence_type = 'star'
    else:
        sentence_type = 'normal'
    return 'Sentence is ' + sentence_type
print(get_type_of_sentence('hello*'))

def who_is_this_house_to_starks(family):
    if family == 'Karstark' or  family == 'Tully':
        return  'friend'
    elif family == 'Lannister' or family == 'Frey':
        return 'enemy'
    return 'neutral'

print(who_is_this_house_to_starks('Karstark'))
print(who_is_this_house_to_starks('Tully'))
print(who_is_this_house_to_starks('Lannister'))
print(who_is_this_house_to_starks('Frey'))
print(who_is_this_house_to_starks('Neutral'))
print(who_is_this_house_to_starks('Frey'))


print(f'\nNext ****************\n')

def abs(number):
    if number >= 0:
        return number
    return -number
print(abs(2))
def abs1(number):
    return number if number >= 0 else -number
print(abs(-2))

def flip_flop(sent):
    return 'flop' if sent == 'flip' else 'flip'
print(flip_flop('flip'))


print(f'\nNext ****************\n')

def check_match(sent):
    match  sent:
        case 'flop':
            return 'flip'
        case 'flip':
            return 'flop'
        case _:
            return "new"

print(check_match('hello'))
print(check_match('flop'))

def count_item(count):
    result = ''
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = 'None'
    return result
print(count_item(1))
print(count_item(2))
print(count_item(3))

def get_number_explanation(number):
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'
print(get_number_explanation(8))
print(get_number_explanation(666))
print(get_number_explanation(42))
print(get_number_explanation(7))


print(f'\nNext ****************\n')

def print_numbers(number):
    i = number
    while i > 0 :
       print(i)
       i = i - 1
    print('finished!')

print_numbers(4)

print(f'\nNext ****************\n')