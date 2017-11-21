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

Sometimes a couple of free functions and built-in types is all that it takes...
'''

'sort and append are list methods. No need to wrap them in useless methods'
items = [1, 4, 9, 2]
items.append(6)
items.sort()

'''use free functions when you can. They're easily tested, have no state,
   they may process various data regardless of context and purpose'''
def flatten(nested_list):
    return [item for list_ in nested_list for item in list_]

def take_even(list_):
    it = iter(list_)
    return [pair[1] for pair in zip(it, it)]

'''extracting transformation to text allows to print...'''
def to_text(list_):
    return ''.join('%s\n' % item for item in list_)

import sys
sys.stdout.write(to_text(take_even(items)))

'''... as well as saving to file'''
def save(path, content):
    with open(path, 'w') as f:
        f.write(content)

save('/tmp/items_text', to_text(items))

'''if one needs to save as binary - there is a separate function for just that'''
def to_blob(list_):
    import struct
    return ''.join(struct.pack('>I', item) for item in list_)

save('/tmp/items_blob', to_blob(items))
