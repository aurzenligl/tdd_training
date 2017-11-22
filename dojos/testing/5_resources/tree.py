import os

'''
Let's see how we could test code using
filesystem and stdout stream.
'''

def tree(path, sizes=False):
    def enum_last(list_):
        length = len(list_)
        islast = [False] * (length - 1) + [True] * bool(length)
        return [e for e in zip(list_, islast)]

    def print_dir(dir_path, lasts):
        chunk_dir = '|   '
        chunk_dir_last = '    '
        chunk_file = '|-- '
        chunk_file_last = '`-- '

        for name, last in enum_last(sorted(os.listdir(dir_path))):
            inner_path = os.path.join(dir_path, name)
            isdir = os.path.isdir(inner_path)

            line = ''.join(chunk_dir_last if last else chunk_dir for last in lasts)
            line += chunk_file if not last else chunk_file_last
            line += name
            if not isdir and sizes:
                bytesize = os.stat(inner_path).st_size
                line += ' [%s]' % bytesize
            print(line)

            if isdir:
                print_dir(inner_path, lasts + [last])

    print(path)
    if os.path.isdir(path):
        print_dir(path, [])
