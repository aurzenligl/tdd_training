# TODO - remove previous implementation if not needed
#
# def flatten(list_):
#     res = []
#     for sublist in list_:
#         for elem in sublist:
#             res.append(elem)
#     return res

def flatten(list_):
    '''
    :arg list_:
    '''
    # sublists = [l for sublist in list_]
    return [item for sublist in list_ for item in sublist]


































'''
If tests pass, it means previous implementation is not needed now.
If it will be in future, version control system will remember.
'''

def flatten(list_):
    return [item for sublist in list_ for item in sublist]
