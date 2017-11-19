'''
Let's test a class which has a difficult dependency,
one that must be separated for it during testing.
How would we handle it?
'''

import struct
import ipc

class EndpointError(Exception):
    pass

class Endpoint(object):
    def __init__(self, id_):
        self.id = id_
        ipc.register(id_)

    def send(self, target, payload):
        datagram = ipc.encode(self.id, target, payload)
        result = ipc.send(datagram)
        if not result:
            raise EndpointError('message to id %s cannot be sent' % target)

    def receive(self):
        datagram = ipc.receive()
        sender, _, payload = ipc.decode(datagram)
        return sender, payload
