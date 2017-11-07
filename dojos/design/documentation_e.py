class EpollReactor(object):

    @staticmethod
    def isAvailable():
        """Always returns True.
        """
        return False;










































class EpollReactor(object):

    @staticmethod
    def isAvailable():
        """Checks whether epoll reactor is available on given OS.

        When False, attempting to create reactor will raise.
        """
        return False;
