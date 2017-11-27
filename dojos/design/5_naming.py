urlString = 'https://google.com'

pathUsedWhenPathStringAndDefaultPathStringAndDefault2PathStringIsNotFound = 'nevermind'

logPathString = "/tmp/log.txt";
logsPathString = "logs/subdir/output";

b_fileRead = True

class IBaseArray(object): pass

work = 0
jump = 2
parse = 42

flower = True

termination = False

findPath = 'foobarbaz'

class Map(object): pass
map = Map()
def id():
    return 4
open = True

class Date(object):
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

class Reader(object):
    def __init__(self, files):
        self.files = files
    def getContent(self):
        return ''.join(f.read() for f in self.files)
    def takeContent(self):
        return ''.join(line for f in files for line in f.readlines() if 'content' in line)

class FlowersAndTreesManager(object): pass

class FlowersContext(object): pass

class FlowersFactory(object): pass













'''Purpose of this variable is not revealed, only its type'''
urlString = 'https://google.com'

'''Name too long. One or two-word names are preferred. Single character names are also feasible'''
pathUsedWhenPathStringAndDefaultPathStringAndDefault2PathStringIsNotFound = 'nevermind'

'''Two distinct variables with different names: easy to mismatch'''
logPathString = "/tmp/log.txt";
logsPathString = "logs/subdir/output";

'''Unnecessary type information in names'''
b_fileRead = True
class IBaseArray(object): pass

'''
Different entities ought to follow different parts of speech.
Verbs: methods, nouns: classes and non-class, non-function variables.
Booleans names should be related to a yes/no question.
'''
'''These are verbs, probably not a good choice for int variable'''
work = 0
jump = 2
parse = 42
'''Flower roughly translates to yes/no.'''
flower = True
'''Termination could translate to yes/no.'''
termination = False
'''Sounds like a function or function object. It's not.'''
findPath = 'foobarbaz'

'''
Be careful not to override Python's builtins or frequently used module names,
like sys or os, or variable/function names already defined. This would
"shadow" them, i.e. hide original definition providing new one instead.

"id" is quite nasty, as this will work somewhat similar to id builtin.
Now this is True: id('foo') == id(5)
'''
class Map(object): pass
map = Map()
def id(x):
    return 4
open = True

'''Names should be pronouncible, easier to talk about code that way'''
class Date(object):
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

'''Two methods doing different things shouldn't be named alike'''
class Reader(object):
    def __init__(self, files):
        self.files = files
    def getContent(self):
        return ''.join(f.read() for f in self.files)
    def takeContent(self):
        return ''.join(line for f in files for line in f.readlines() if 'content' in line)

'''Class probably has two responsibilities'''
class FlowersAndTreesManager(object): pass

'''Context or Manager tells nothing about this class'''
class FlowersContext(object): pass

'''Factory is a well-known name derived from design pattern, this can be communicative'''
class FlowersFactory(object): pass
