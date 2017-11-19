import sys
import struct

'''
IPC library allows to register to IPC bus and send/receive datagrams.
Datagram is a sequence of bytes composed of header and payload:

+-----------------------+-----------------+
|        header         |                 |
+-----------+-----------+     payload     |
|  sender   | receiver  |                 |
+-----+-----+-----+-----+-----------------+
|  0  |  1  |  2  |  3  |       ...       |
+-----------------------+-----------------+

sender - 2-byte unsigned big endian id of sender
receiver - 2-byte unsigned big endian id of receiver
payload - byte sequence of any length
'''

'''
Functions use OS or third party library, which you don't want or cannot
run in your tests. It's emphasised by them exiting on the spot.
'''

def register(id):
    '''Enables endpoint on the the IPC bus, allowing it to send and receive messages.

    :arg id: endpoint id, 16-bit unsingned integer, undefined behavior otherwise
    '''
    sys.exit()

def receive():
    '''Receives datagram.

    :returns:  Datagram bytestring.
    '''
    sys.exit()

def send(datagram):
    '''Sends datagram.

    :returns: False in case of bus error, True otherwise.
    '''
    sys.exit()

def encode(sender, receiver, payload):
    '''Creates datagram from parts.

    :arg sender:  endpoint id, 16-bit unsingned integer
    :arg receiver:  endpoint id, 16-bit unsingned integer
    :arg payload:  bytestring
    '''
    header = struct.pack('>HH', sender, receiver)
    datagram = header + payload
    return datagram

def decode(datagram):
    '''Splits datagram to parts.

    :returns:  3-tuple:
                 - sender id
                 - receiver id
                 - payload bytestring
    '''
    header, payload = datagram[:4], datagram[4:]
    sender, receiver = struct.unpack('>HH', header)
    return sender, receiver, payload
