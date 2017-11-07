# example based on code from Py library:
# https://github.com/pytest-dev/py/blob/master/py/_path/local.py

'Is this documentation style helpful?'

class LocalPath(object):
    """ Class derived from object.
    """

    def __init__(self, path=None, expanduser=False):
        """ Initializes LocalPath.

        :arg path: should be a path or None.

        :arg expanduser: Tells whether path should be expanded or not.
                         Can be True or False.
        """
        # ...

    def new(self, **kw):
        """ Method accepting keyword arguments.

        User can provide any number of keyword arguments while calling
        this method.

        :arg kw: keyword arguments.
        """
        # ...

    def __hash__(self):
        """ Override for hash magic method.

        Calculates hash from string.
        """
        return hash(self.strpath)














'''
Obvious, self-explanatory things shouldn't be mentioned.
Such comments obfuscate important stuff and make reader stop reading
them, even if they contain valuable information.

Documentation should mention:
    - class/function purpose
    - contract: preconditions, postconditions
    - non-obvious, important functional details, like performance or side-effects
'''

class LocalPath(object):
    """ Object oriented interface to os.path and other local filesystem
        related information.
    """

    def __init__(self, path=None, expanduser=False):
        """ Initialize and return a local Path instance.
        Path can be relative to the current directory.
        If path is None it defaults to the current working directory.
        If expanduser is True, tilde-expansion is performed.
        Note that Path instances always carry an absolute path.
        Note also that passing in a local path object will simply return
        the exact same path object. Use new() to get a new copy.
        """
        # ...

    def new(self, **kw):
        """ create a modified version of this path.
            the following keyword arguments modify various path parts::

              a:/some/path/to/a/file.ext
              xx                           drive
              xxxxxxxxxxxxxxxxx            dirname
                                xxxxxxxx   basename
                                xxxx       purebasename
                                     xxx   ext
        """
        # ...

    def __hash__(self):
        return hash(self.strpath)
