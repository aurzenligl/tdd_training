import pytest
import sokoban

@pytest.fixture(autouse=True)
def mock_sokoban(mocker):
    mocker.patch.object(sokoban.__main__, 'Engine', autospec=True)
    mocker.patch.object(sokoban.__main__, 'Game', autospec=True)

def test_main_creates_engine_and_game():
    sokoban.main()

    assert sokoban.__main__.Engine.call_count == 1
    assert sokoban.__main__.Game.call_count == 1
