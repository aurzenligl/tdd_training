'''
Let's say you've got simple free function which does something.
How would we unit test it?
'''

def count_occurences(seq):
    '''
    :arg seq:  iterable of hashable values
    :returns:  dict keyed by unique input values with number of occurences as values
    '''
    occurences = {}
    for elem in seq:
        count = occurences.get(elem)
        occurences[elem] = (count + 1) if count is not None else 1
    return occurences
