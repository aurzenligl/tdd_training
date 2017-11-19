import mock
import pytest
from endpoint import Endpoint, EndpointError
import ipc

'''
Stub - allows to ignore real implementation.
Use when it does not matter for caller what side-effects took place.
'''
@pytest.fixture(autouse=True)
def ipc_stub_register(mocker):
    mocker.patch('ipc.register')

'''
Mock - is used when certain return value or side-effect must be
supplied, otherwise caller won't work properly.
'''
@pytest.fixture(autouse=True)
def ipc_mock_send(mocker):
    mocker.patch('ipc.send')
    def send_mock(datagram):
        return True
    ipc.send.side_effect = send_mock

class TestEndpoint(object):

    '''
    We're using "stub" (no action taken by register implemetation at all),
    which also works as a "spy" (we may inspect count of calls and all arguments).
    '''
    def test_register(self):
        Endpoint(0x1)

        ipc.register.assert_called_once_with(0x1)

    '''
    Let's use mock to trick endpoint into thinking that send succeed.
    '''
    def test_send_success(self):
        endpt = Endpoint(0x1)

        endpt.send(0x2, 'abcdef')

        ipc.send.assert_called_once_with('\x00\x01\x00\x02' + 'abcdef')

    '''
    In order to test failure case we need to change mock behavior.
    '''
    def test_send_failure(self):
        def send_mock(datagram):
            return False
        ipc.send.side_effect = send_mock
        endpt = Endpoint(0x1)

        with pytest.raises(EndpointError) as e:
            endpt.send(0x2, 'abcdef')

        ipc.send.assert_called_once_with('\x00\x01\x00\x02' + 'abcdef')
        assert str(e.value) == 'message to id 2 cannot be sent'
