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
        sender, receiver = self.id, target
        header = struct.pack('>HH', sender, receiver)
        datagram = header + payload
        result = ipc.send(datagram)
        if not result:
            raise EndpointError('message to id %s cannot be sent' % target)

    def receive(self):
        datagram = ipc.receive()
        header, payload = datagram[:4], datagram[4:]
        sender, _ = struct.unpack('>HH', header)
        return sender, payload
