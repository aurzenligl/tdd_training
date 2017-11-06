import pytest
import app

@pytest.fixture(autouse=True)
def mock_sokoban(mocker):
    mocker.patch.object(app.__main__, 'Engine', autospec=True)
    mocker.patch.object(app.__main__, 'Game', autospec=True)

def test_main_creates_engine_and_game():
    app.main()

    assert app.__main__.Engine.call_count == 1
    assert app.__main__.Game.call_count == 1
