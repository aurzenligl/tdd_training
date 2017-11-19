import pytest
import random
from password import gen_password, PasswordConfig

'''
Since unit tests are white-box tests, we're allowed
to assume pseudo-randomness is going to be used.
If so, we can make tests deterministic by running them
with hardcoded seed always.
'''

@pytest.fixture(autouse=True)
def fixed_random_seed():
    '''
    We save the state of random number generator
    '''
    previous_state = random.getstate()

    '''
    Now all tests in this module using random module implicitly
    will be deterministic.
    '''
    random.seed(0)

    '''
    Yield fixture allows to do setup before yield and cleanup after yield,
    when we still have access to local variables defined above.
    '''
    yield

    '''
    We retrieve the state of random number generator after testcase.
    We don't want to break other tests in suite or parts of framework
    which may for whatever reason require different seed.
    '''
    random.setstate(previous_state)

@pytest.fixture(autouse=True)
def fixed_at_least_one_capital_false():
    '''
    Since we have other tests which may do something
    with this static variable, let's just clear this
    before and after the test.

    If we know that no tests in our suite misbehave,
    we can use monkeypatching when we change static
    state, it ensures that previous state is retained
    afterwards.
    '''
    PasswordConfig.at_least_one_capital = False
    yield
    PasswordConfig.at_least_one_capital = False

class TestPassword(object):
    @pytest.mark.parametrize('code, charset', [
        ('x', PasswordConfig.alpha),
        ('0', PasswordConfig.numbers),
        ('.', PasswordConfig.other)
    ], ids = [
        'alpha',
        'numbers',
        'other'
    ])
    def test_randomness(self, code, charset):
        pwd = gen_password(code * 10000)

        for char in charset:
            assert char in pwd

    def test_alphas_without_capital(self):
        pwds = [gen_password('x') for _ in range(30)]

        assert any(pwd.islower() for pwd in pwds)
        assert any(pwd.isupper() for pwd in pwds)

    def test_alphas_at_least_one_capital_single_letter_is_always_upper(self, monkeypatch):
        '''
        If such monkey-patching is used consistently, we don't
        need fixture clearing this static flag.
        '''
        monkeypatch.setattr(PasswordConfig, 'at_least_one_capital', True)

        for _ in range(30):
            assert gen_password('x').isupper()

    def test_alphas_at_least_one_capital_many_letters_one_is_always_upper(self, monkeypatch):
        def is_any_upper(str_):
            return any(c.isupper() for c in str_)

        monkeypatch.setattr(PasswordConfig, 'at_least_one_capital', True)

        for _ in range(30):
            assert is_any_upper(gen_password('xxxxx'))

    def test_alphas_at_least_one_capital_many_letters_all_but_one_can_be_lower(self, monkeypatch):
        def count_lower(str_):
            return sum(c.islower() for c in str_)

        monkeypatch.setattr(PasswordConfig, 'at_least_one_capital', True)

        pwds = [gen_password('xxx') for _ in range(30)]

        assert any(count_lower(pwd) == 2 for pwd in pwds)

    def test_mixed_codes(self):
        pwd = gen_password('xxx...000')
        alpha = pwd[:3]
        other = pwd[3:6]
        numbers = pwd[6:]

        assert all(c in PasswordConfig.alpha for c in alpha)
        assert all(c in PasswordConfig.other for c in other)
        assert all(c in PasswordConfig.numbers for c in numbers)
