class EpollReactor(object):

    @staticmethod
    def isAvailable():
        """Always returns True.
        """
        return False;










































'''
First of all, comment is exactly wrong. It returns False.

Documentation should describe the API, not the implementation.
Fact that currently, in this version, on this platform this function
returns False, doesn't mean that it always does so.
'''

class EpollReactor(object):

    @staticmethod
    def isAvailable():
        """Checks whether epoll reactor is available on given OS.

        When False, attempting to create reactor will raise.
        """
        return False;
