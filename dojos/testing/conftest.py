def pytest_addoption(parser):
    parser.addoption('--repeat', type='int', metavar='REPEAT',
                     help='Run each test the specified number of times')

def pytest_generate_tests(metafunc):
    repeats = metafunc.config.option.repeat
    if repeats is not None:
        for i in range(repeats):
            metafunc.addcall()
