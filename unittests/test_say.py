import asyncio
import pytest

from say.say import say


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


def test_say(event_loop):
    expected = 'Hello!'
    assert expected == event_loop.run_until_complete(say('Hello!', 0))