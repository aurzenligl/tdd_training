import os
import sys
from tree import tree

opj = os.path.join
mkdir = os.mkdir

def mkfile(path, content):
    with open(path, 'w') as f:
        f.write(content)

class Stdout(object):
    def __init__(self):
        self.value = ''

    def write(self, str_):
        self.value += str_

    def flush(self):
        pass

def count(seq, pred):
    return len([x for x in seq if pred(x)])

class TestTree(object):
    def test_tree(self, monkeypatch):
        rootnum = count(os.listdir(os.curdir), lambda path: path.startswith('tmp'))
        root = 'tmp_%s' % rootnum

        mkdir(root)
        mkfile(opj(root, 'foo'), 'x' * 10)
        mkfile(opj(root, 'bar'), 'x' * 1000)
        mkfile(opj(root, 'baz'), 'x' * 1)

        mkdir(opj(root, 'empty'))

        mkdir(opj(root, 'one'))
        mkfile(opj(root, 'one', 'foo'), 'x' * 3)
        mkfile(opj(root, 'one', 'bar'), 'x' * 4)

        mkdir(opj(root, 'two'))
        mkdir(opj(root, 'two', 'three'))
        mkfile(opj(root, 'two', 'three', 'data'), 'x' * 1234)

        stdout = Stdout()

        monkeypatch.setattr(sys, 'stdout', stdout)
        tree(root)
        monkeypatch.undo()

        assert stdout.value ==(
            'tmp_%s\n'
            '|-- bar [1000]\n'
            '|-- one\n'
            '|   |-- bar [4]\n'
            '|   `-- foo [3]\n'
            '|-- two\n'
            '|   `-- three\n'
            '|       `-- data [1234]\n'
            '|-- empty\n'
            '|-- foo [10]\n'
            '`-- baz [1]\n') % rootnum
