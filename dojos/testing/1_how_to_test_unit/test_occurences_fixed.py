import pytest
from occurences import count_occurences

'''
Previous test had too much logic inside. It reimplemented function it
was supposed to test. If such test fails, you never know whether implementation
failed or test failed (was improperly written).

This test(s) can and should be much simpler.
'''

'''
Let's start by defining simple tests for simple scenarios.
Key is to define multiple tests which check different aspects of tested entity.
If they do all pass at the same time, we have a good reason to suspect that
entity may in fact work when combination of these different aspects is used.

Unit tests are about the only place when we can succeed in exhausting
majority of all possible and rather impossible use cases.
We cannot check all possible combinations of actions in application GUI
as this number is infinite (as the lenght of sequence of actions is infinite).

And it's ridiculously cheap to write/run/maintain such tests.
'''
def test_occurences_empty():
    assert count_occurences([]) == {}

def test_occurences_two_same():
    assert count_occurences([1, 1]) == {1: 2}

def test_occurences_two_different():
    assert count_occurences([1, 2]) == {1: 1, 2: 1}

'''
We haven't written in docstring that we need the same types.
Let's ensure that we can use different types.
'''
def test_occurences_heterogenous():
    x = 'abc'
    y = (7,8,9)
    z = complex(1.3, 0.2)
    assert count_occurences([z, y, y, z, x, z]) == {x: 1, y: 2, z: 3}

'''
What about special case values which hash but do not compare equal?
Whatever the behavior chosen, it shouldn't change. Chosen output,
dict, ensures nans will be counted. This test ensures that behavior
will stay if we e.g. change implementation of output type.
'''
def test_occurences_nans():
    nan = float('nan')
    assert count_occurences([nan, nan, nan]) == {nan: 3}

'''
We're supposed to accept any iterable, so let's try a couple.
Putting generator as input is valuable. It ensures that if someone
will have used our function with generator (month later), and we
will have refactored this function (year later) by using len(seq)
for whatever reason, user code won't be broken.

I've used multiple asserts here, which may be controversial.
Let me get back to how to rewrite this in later installment.
'''
def test_occurences_iterable_input():
    assert count_occurences((x for x in range(2))) == {0: 1, 1: 1}
    assert count_occurences((0, 1)) == {0: 1, 1: 1}
    assert count_occurences([0, 1]) == {0: 1, 1: 1}
    assert count_occurences({0: None, 1: None}) == {0: 1, 1: 1}
    assert count_occurences('foo') == {'f': 1, 'o': 2}

'''
Negative tests can and should be written to specify behavior in
case of wrong input and keep that behavior consistent.
In this case we're expecting exception in case of mutable element.
No specific exception, no emtpy dict return either, just exactly "some" exception.
'''
def test_occurences_disallows_mutable():
    with pytest.raises(Exception) as e:
        count_occurences([[]])

'''
You may have a feeling that some tests here are a case of overengineering.
You're probably right. There's no right answer to question: how much tests
should I write. You should gain some level of confidence in your code
quality that you and your users are comfortable with.
'''
