# code example based on pytest project:
# https://github.com/pytest-dev/pytest/blob/master/_pytest/python.py

def slice_items(items, ignore, scoped_argkeys_cache):
    if scoped_argkeys_cache:  # checking for None, exit function otherwise
        it = iter(items)  # making an iterator out of items
        for i, item in enumerate(it):  # enumerating to have an index of element
            # getting keys associated to item from argkeys dictionary
            argkeys = scoped_argkeys_cache.get(item)
            # checking against None to account for empty list
            if argkeys is not None:
                # checking if there are non-ignored keys
                argkeys = argkeys.difference(ignore)
                # if non-ignored key is found, we're going to return from the function
                if argkeys:
                    # take the first key from the list
                    slicing_argkey = argkeys.pop()
                    # split items to three parts, before item,
                    # with same argkey and others
                    items_before = items[:i]
                    items_same = [item]
                    items_other = []
                    # now slice the remainder of the list
                    for item in it:
                        # continue iteration from the partition point element
                        argkeys = scoped_argkeys_cache.get(item)
                        # check if item has the same dependency as partition point
                        if argkeys and slicing_argkey in argkeys and \
                            slicing_argkey not in ignore:
                            items_same.append(item)  # if so, add it to same items list
                        else:
                            items_other.append(item)  # otherwise to other items
                    newignore = ignore.copy()  # copy list not to return reference to input argument
                    newignore.add(slicing_argkey)  # extend ignore-list with newly added partition-point item
                    # return partitioned list
                    return (items_before, items_same, items_other, newignore)
    # return not-partitioned list
    return items, None, None, None











'''
Comments should be used scarcely, when implementation complexity or inability
to express some external constraints mandates them. When used properly,
they can be quite helpful in explaining what's going on.
'''

def slice_items(items, ignore, scoped_argkeys_cache):
    # we pick the first item which uses a fixture instance in the
    # requested scope and which we haven't seen yet.  We slice the input
    # items list into a list of items_nomatch, items_same and
    # items_other
    if scoped_argkeys_cache:  # do we need to do work at all?
        it = iter(items)
        # first find a slicing key
        for i, item in enumerate(it):
            argkeys = scoped_argkeys_cache.get(item)
            if argkeys is not None:
                argkeys = argkeys.difference(ignore)
                if argkeys:  # found a slicing key
                    slicing_argkey = argkeys.pop()
                    items_before = items[:i]
                    items_same = [item]
                    items_other = []
                    # now slice the remainder of the list
                    for item in it:
                        argkeys = scoped_argkeys_cache.get(item)
                        if argkeys and slicing_argkey in argkeys and \
                            slicing_argkey not in ignore:
                            items_same.append(item)
                        else:
                            items_other.append(item)
                    newignore = ignore.copy()
                    newignore.add(slicing_argkey)
                    return (items_before, items_same, items_other, newignore)
    return items, None, None, None
