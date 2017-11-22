import pytest
from tree import tree

class TestTree(object):

    def test_file(self, tmpdir, capsys):
        root = tmpdir.join('foo')
        root.write('', ensure=True)

        tree(str(root))

        stdout, _ = capsys.readouterr()
        assert stdout == '%s\n' % str(root)

    def test_empty_dir(self, tmpdir, capsys):
        root = tmpdir.join('root').ensure_dir()

        tree(str(root))

        stdout, _ = capsys.readouterr()
        assert stdout == '%s\n' % str(root)

    def test_dir_with_file(self, tmpdir, capsys):
        root = tmpdir.join('root').ensure_dir()
        root.join('foo').write('', ensure=True)

        tree(str(root))

        stdout, _ = capsys.readouterr()
        assert stdout == (
            '%s\n'
            '`-- foo\n') % str(root)

    def test_dir_with_two_files(self, tmpdir, capsys):
        root = tmpdir.join('root').ensure_dir()
        root.join('foo').write('', ensure=True)
        root.join('bar').write('', ensure=True)

        tree(str(root))

        stdout, _ = capsys.readouterr()
        assert stdout == (
            '%s\n'
            '|-- bar\n'
            '`-- foo\n') % str(root)

    def test_nested_dir(self, tmpdir, capsys):
        root = tmpdir.join('root').ensure_dir()
        root.join('one', 'foo').write('', ensure=True)

        tree(str(root))

        stdout, _ = capsys.readouterr()
        assert stdout == (
            '%s\n'
            '`-- one\n'
            '    `-- foo\n') % str(root)

    def test_two_nested_dirs_two_files_each(self, tmpdir, capsys):
        root = tmpdir.join('root').ensure_dir()
        root.join('one', 'foo').write('', ensure=True)
        root.join('one', 'bar').write('', ensure=True)
        root.join('two', 'baz').write('', ensure=True)
        root.join('two', 'xyz').write('', ensure=True)

        tree(str(root))

        stdout, _ = capsys.readouterr()
        assert stdout == (
            '%s\n'
            '|-- one\n'
            '|   |-- bar\n'
            '|   `-- foo\n'
            '`-- two\n'
            '    |-- baz\n'
            '    `-- xyz\n') % str(root)

    @pytest.fixture
    def testdir(self, tmpdir):
        root = tmpdir.join('root').ensure_dir()
        root.join('foo').write('x' * 10, ensure=True)
        root.join('bar').write('x' * 1000, ensure=True)
        root.join('baz').write('x' * 1, ensure=True)
        root.join('empty').ensure_dir()
        root.join('one', 'foo').write('x' * 3, ensure=True)
        root.join('one', 'bar').write('x' * 4, ensure=True)
        root.join('two', 'three', 'data').write('x' * 1234, ensure=True)
        return root

    def test_large_without_sizes(self, testdir, capsys):
        tree(str(testdir))

        stdout, _ = capsys.readouterr()
        assert stdout == (
            '%s\n'
            '|-- bar\n'
            '|-- baz\n'
            '|-- empty\n'
            '|-- foo\n'
            '|-- one\n'
            '|   |-- bar\n'
            '|   `-- foo\n'
            '`-- two\n'
            '    `-- three\n'
            '        `-- data\n') % str(testdir)

    def test_large_with_sizes(self, testdir, capsys):
        tree(str(testdir), sizes=True)

        stdout, _ = capsys.readouterr()
        assert stdout == (
            '%s\n'
            '|-- bar [1000]\n'
            '|-- baz [1]\n'
            '|-- empty\n'
            '|-- foo [10]\n'
            '|-- one\n'
            '|   |-- bar [4]\n'
            '|   `-- foo [3]\n'
            '`-- two\n'
            '    `-- three\n'
            '        `-- data [1234]\n') % str(testdir)
