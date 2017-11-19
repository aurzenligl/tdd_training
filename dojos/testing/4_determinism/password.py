import random

'''
Let's test a piece of code which uses randomness.
And static data. How would we test this?
'''

class PasswordConfig(object):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    other = r'''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    at_least_one_capital = False

def gen_password(template):
    ''' Generates password string.

    :arg template:  string of characters 'x', '0', '.', representing
                    letters, numbers and other characters respectively

    Example:
        >>> gen_password('xxxxxx000.')
        'aBjOqK829!'
    '''

    def make_bucket(code, charset):
        count = template.count(code)
        return ''.join(random.choice(charset) for _ in range(count))

    alpha = make_bucket('x', PasswordConfig.alpha)
    numbers = make_bucket('0', PasswordConfig.numbers)
    other = make_bucket('.', PasswordConfig.other)

    if PasswordConfig.at_least_one_capital:
        while alpha.islower():
            alpha = make_bucket('x', PasswordConfig.alpha)

    code_to_buckets = {
        'x': iter(alpha),
        '0': iter(numbers),
        '.': iter(other)
    }

    def pick(c):
        return code_to_buckets[c].next()
    return ''.join(pick(c) for c in template)
