import pytest
from endpoint import Endpoint
import ipc

'''
Mocking is such a convenient tool in Python that it's easy to
abuse its power. Here we're controlling how many times "send"
implementation calls "encode". Since "encode" is a free function,
it's totally irrelevant whether it's called 0, 1, 2 or other
number of times. User doesn't care, ipc module doesn't care either.
Tester shouldn't too.
'''

class TestEndpoint(object):
    def test_send_encodes(self, mocker):
        mocker.patch('ipc.register')
        mocker.patch('ipc.send')
        mocker.patch('ipc.encode')
        def send_mock(datagram):
            return True
        ipc.send.side_effect = send_mock
        endpt = Endpoint(0x1)

        endpt.send(0x2, 'abcdef')

        ipc.encode.assert_called_once_with(0x1, 0x2, 'abcdef')
