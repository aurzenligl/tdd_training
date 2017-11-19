import random
from password import gen_password, PasswordConfig

class TestPassword(object):
    def test_randomness(self):
        pwd = gen_password('0' * 80)

        for num in '0123456789':
            assert num in pwd

    def test_alphas(self):
        random.seed(0)

        assert gen_password('xxxxxx') == 'RNvnAv'

    def test_numbers(self):
        assert gen_password('000000') == '734595'

    def test_alphas_without_capital(self):
        pwds = [gen_password('x') for _ in range(30)]

        assert any(pwd.islower() for pwd in pwds)

    def test_alphas_at_least_one_capital_single_letter(self):
        PasswordConfig.at_least_one_capital = True
        pwds = [gen_password('x') for _ in range(30)]

        assert all(pwd.isupper() for pwd in pwds)

    def test_alphas_at_least_one_capital_many_letters(self):
        pwds = [gen_password('xxx') for _ in range(30)]

        assert all(any(c.isupper() for c in pwd) for pwd in pwds)
        assert any(any(c.islower() for c in pwd) for pwd in pwds)

    def test_mixed_codes(self):
        pwd = gen_password('xxx...000')
        alpha = pwd[:3]
        other = pwd[3:6]
        numbers = pwd[6:]

        assert all(c in PasswordConfig.alpha for c in alpha)
        assert all(c in PasswordConfig.other for c in other)
        assert all(c in PasswordConfig.numbers for c in numbers)























































class BrokenPasswordTestsExplained(object):

    '''
    This test is "flaky". It fails once per 500 runs or so,
    although it's not immediately apparent it does so.
    Such tests are constant source of misery for programmers
    who are involved to solve problems in one part of project
    and experience failing tests in other part. Such fails are
    unrelated to programmer's changes, but he doesn't know this
    for a couple of minutes, hours or days.
    '''
    def test_randomness(self):
        pwd = gen_password('0' * 80)

        for num in '0123456789':
            assert num in pwd

    '''
    Any change in gen_password implementation will change the
    order of characters, even though seed is set. This is fragile.

    This test expects that gen_password uses "random" module.
    What if it doesn't? It could use random device or C extension
    module as source of randomness. Changing random seed in these
    cases is meaningless and test will (almost) every time.
    '''
    def test_alphas(self):
        random.seed(0)

        assert gen_password('xxxxxx') == 'RNvnAv'

    '''
    This test depends on previous one. If they're run multiple times
    or shuffled, it will fail constantly.
    '''
    def test_numbers(self):
        assert gen_password('000000') == '734595'

    '''
    This test is sort of ok, but may fail. Probability is extremely low,
    but it's possible. It's a decision to take whether:
        - fully deterministic tests are made with random seed
        - randomness is tested by statistical means
    '''
    def test_alphas_without_capital(self):
        pwds = [gen_password('x') for _ in range(30)]

        assert any(pwd.islower() for pwd in pwds)

    '''
    This test sets static variable. It doesn't unset it.
    This breaks isolation between tests.
    '''
    def test_alphas_at_least_one_capital_single_letter(self):
        PasswordConfig.at_least_one_capital = True
        pwds = [gen_password('x') for _ in range(30)]

        assert all(pwd.isupper() for pwd in pwds)

    '''
    This test uses static variable that previous one set.
    If it's run in different order, it will fail constantly.
    '''
    def test_alphas_at_least_one_capital_many_letters(self):
        pwds = [gen_password('xxx') for _ in range(30)]

        assert all(any(c.isupper() for c in pwd) for pwd in pwds)
        assert any(any(c.islower() for c in pwd) for pwd in pwds)

    '''
    Amazingly, this test is fully ok.
    '''
    def test_mixed_codes(self):
        pwd = gen_password('xxx...000')
        alpha = pwd[:3]
        other = pwd[3:6]
        numbers = pwd[6:]

        assert all(c in PasswordConfig.alpha for c in alpha)
        assert all(c in PasswordConfig.other for c in other)
        assert all(c in PasswordConfig.numbers for c in numbers)
