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

'''
Fake - we provide implementation similar when it comes to behavior
to the real thing, but so as to have full control over collaborator.
We don't need to spy actions on interface boundary anymore, it's
enough to store state in fake object and assert it at the end of test.
'''
@pytest.fixture(autouse=True)
def ipc_receive_fake(monkeypatch):
    class ReceiveQueue():
        def __init__(self):
            self.datagrams = []
        def push(self, datagram):
            self.datagrams.append(datagram)
        def pop(self):
            return self.datagrams.pop(0)

    queue = ReceiveQueue()
    monkeypatch.setattr(ipc, 'receive', queue.pop)
    yield queue

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

    '''
    We use fake differently. It doesn't have "spying" ability, but here
    we don't need it. It might be easier and more clear to use queue
    object as a means to provide messages to receive, instead of using
    mock side_effect interface for this.
    '''
    def test_receive(self, ipc_receive_fake):
        ipc_receive_fake.push('\x00\x01\x00\x02' + 'abcdef')
        endpt = Endpoint(0x2)

        sender, payload = endpt.receive()

        assert sender == 1
        assert payload == 'abcdef'
