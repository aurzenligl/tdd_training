'A class has one single responsibility and therefore one reason to change'

class ItemManager(object):
    def __init__(self, path, items_front, nested_items, nested_first=False, sort=True):
        self.path = path
        self.binary = False
        unnested = [item for items in nested_items for item in items]
        if nested_first:
            self.items = unnested + items_front
        else:
            self.items = items_front + unnested
        if sort:
            self.items.sort()

    def add(self, item):
        self.items.append(item)

    def sort(self):
        self.items.sort()

    def set_binary(self):
        self.binary = True

    def remove_even(self):
        it = iter(self.items)
        self.items = [pair[1] for pair in zip(it, it)]

    def print_even(self):
        it = iter(self.items)
        for even in [pair[1] for pair in zip(it, it)]:
            print(even)

    def save(self):
        with open(self.path, 'w') as f:
            for item in self.items:
                if self.binary:
                    import struct
                    f.write(struct.pack('>I', item))
                else:
                    f.write(str(item))



















'''
Class introduces a set of member variables which are accessible to all methods.
In order not to break encapsulation, one should limit the amount of state (variables) to bare minimum,
which is necessary, and use other classes to keep the rest of state.

Use class when you have an "invariant", i.e. a kind of contract each method of class has,
which demands object state to be kept consistent between method calls.
https://en.wikipedia.org/wiki/Class_invariant

Frequently such invariant does not exist and multiple loosely coupled data elements occupy
one big class for no good reason whatsoever.
'''

'''
Sometimes a couple of free functions and built-in types is all that it takes...

Use free functions when you can. They're easily tested, possess no state,
have minimal dependencies and may process various data regardless of context and purpose.
As long, of course, as you don't use global variables to hide state in.
'''

import sys
import struct

'''
Let's pick and name list-processing functions. They're useful as such.
They don't have any dependency to filesystem, filenames, binary serialization and whatnot.
'''
def flatten(nested_list):
    return [item for list_ in nested_list for item in list_]

def take_even(list_):
    it = iter(list_)
    return [pair[1] for pair in zip(it, it)]

'''
Let's take to-text and to-binary transformation functions out.
They don't manage list elements, only transform them to other format.
They don't need dependency to filesystem as well.
'''
def to_text(list_):
    return ''.join('%s\n' % item for item in list_)

def to_blob(list_):
    return ''.join(struct.pack('>I', item) for item in list_)

'''
The only function which cares about writing to filesystem
doesn't need to know how to manipulate lists and accepts
already preprated content.
'''
def save(path, content):
    with open(path, 'w') as f:
        f.write(content)

'''
Sort and append are list methods. No need to wrap them in useless methods,
which contibute only to codebase complexity.
'''

'''
Any usage scenario which ItemManager user has had (be it function, script or other class)
can be replaced with one-liner solutions, like the following:
'''
items = [1, 4, 9, 2]
items.append(6)  # append is a buint-in class method
items.sort()  # append is a buint-in class method
sys.stdout.write(to_text(take_even(items)))  # combination of free functions solve printing problem
save('/tmp/items_text', to_text(items))  # saving text to file is handled by combination of two functions
save('/tmp/items_blob', to_blob(items))  # saving binary data to file requires different, aptly named function
