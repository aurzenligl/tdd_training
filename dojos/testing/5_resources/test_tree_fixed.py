import pytest
from tree import tree

class TestTree(object):

    '''
    When it comes to filesystem, we have two options:
    - mock away calls related to filesystem and make them return file contents and stats,
    - prepare a tempdir with proper directory structure and ability to alter it.

    In this case, with Python's ease of filesystem manipulation,
    it's a crime to mock away calls to listdir/stat/isdir, etc.
    Such mocking in this case is going to make your tests unintelligible and rigid,
    because tree uses filesystem copiously and you don't want a change in implementation
    to render your carefully prepared mocks useless.

    Fixture tmpdir creates a temporary dir in /tmp (on unix-likes), which is unique per
    testcase and gets recycled during consecutive pytest run. You don't have to clean
    this directory during testcase, framework will do it for you.

    Additional bonus to solving resource testing problems that way is that we have a
    guarantee that code integrates with resource (filesystem, network, database),
    instead of a vague promise that it does, which mocks give (we may make mistakes
    by defining mocks). And we can debug resources using external tools, like
    shell (filesystem), wireshark (network) or database (other database applications).
    '''

    '''
    When it comes to stdout printing, we have two options again:
    - do away with printing and return string instead,
    - keep printing and use facility to redirect them to string which you can assert.
    Again, in Python second option is viable, we can use capsys fixture which does just this.
    '''
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

    '''
    We can prepare arbitrarily large "integration" test data in fixture
    and use it in multiple tests. After test execution (failure?) we may
    enter test directory and check state of this directory structure.
    '''
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
