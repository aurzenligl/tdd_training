'''
Law of Demeter for functions requires that a method of an object may only invoke following entities:

    methods of self attibutes
        self.foo.bar()
    methods/attributes of self
        self.foo()
        self.foo
    methods/attributes of parameters
        param.foo()
        param.foo
    methods/attributes of objects instantiated by itself
        inst = Something()
        inst.foo()
        inst.foo
    methods/attributes of global variables in scope
        glo.foo()
        glo.foo
'''

import socket

class InnerResource():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def setopt(self, opt):
        self.socket.setsockopt(socket.SOL_SOCKET, opt, True)

class Resource():
    def __init__(self, items):
        self.inner = InnerResource()
        self.items = items
    def foo(self):
        pass  # do something with inner and items
    def bar(self):
        pass  # do something with inner and items

class OuterResource():
    def __init__(self, host):
        self.resource = Resource(['abc', 'def'])
        self.host = host
    def init(self):
        self.resource.foo()
        self.resource.inner.setopt(socket.SO_REUSEADDR)
        self.resource.bar()
        self.resource.inner.socket.bind((self.host, 0))
        self.resource.items.append('ghi')

out = OuterResource(host='localhost')
out.init()



















'''
Loose coupling may turn codebase into spaghetti code with every function having
access to every datum, inhibiting attempts to understand it and change it.

Objects should be able to encapsulate data enclosed within, without letting
other classes to access such data from outside. Such objects have full
responsibility for their data.

In Python we denote encapsulation by a leading underscore in member identifiers.
'''

import socket

'''
We gather that this class is supposed to hide socket.
Let's show only those methods which clients will want to call.
'''
class InnerResource():
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setopt(self, opt):
        self._socket.setsockopt(socket.SOL_SOCKET, opt, True)

    '''
    Bind takes only host, as this is what must flow from OuterResource's user.
    Port number is not a parameter, it's hardcoded to an ephemeral port.
    '''
    def bind(self, host):
        self._socket.bind((host, 0))

'''
We gather that this class is supposed to expose methods used
during OuterResource initialization. Let us expose only those and no data.
'''
class Resource():
    '''
    Host moved to Resource, as it's closer to socket being configured.
    '''
    def __init__(self, items, host):
        self._inner = InnerResource()
        self._items = items
        self._host = host

    def foo(self):
        '''
        Resource handles its component instead of OuterResource doing so.
        '''
        self._inner.setopt(socket.SO_REUSEADDR)
        pass  # do something with inner and items

    def bar(self):
        '''
        Instead of calling bind and appending item in OuterResource,
        its dependency takes over and handles itself.
        '''
        self._inner.bind(self._host)
        self._items.append('ghi')
        pass  # do something with inner and items

class OuterResource():
    def __init__(self, resource):
        self.resource = resource

    def init(self):
        self.resource.foo()
        self.resource.bar()

'''
Resource can be injected into OuterResource to reduce the coupling still.
'''
res = Resource(['abc', 'def'], host='localhost')
out = OuterResource(res)
out.init()

'''
Now we can:
    - refactor InnerResource without fear of destroying rest of the program
    - substitute Resource for any other Resource, as long as Resource API is in place
    - read/understand/test OuterResource, object containing a lot of state, without problems
'''
