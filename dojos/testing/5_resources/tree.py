import os

def tree(path, sizes=True):
    def enum_last(list_):
        length = len(list_)
        islast = [False] * (length - 1) + [True] * bool(length)
        return [e for e in zip(list_, islast)]

    def printer(path, lasts):
        chunk_dir = '|   '
        chunk_dir_last = '    '
        chunk_file = '|-- '
        chunk_file_last = '`-- '

        for name, last in enum_last(os.listdir(path)):
            inner_path = os.path.join(path, name)
            isdir = os.path.isdir(inner_path)

            line = ''.join(chunk_dir_last if last else chunk_dir for last in lasts)
            line += chunk_file if not last else chunk_file_last
            line += name
            if not isdir and sizes:
                bytesize = os.stat(inner_path).st_size
                line += ' [%s]' % bytesize
            print(line)

            if isdir:
                printer(inner_path, lasts + [last])

    print(path)
    printer(path, [])
