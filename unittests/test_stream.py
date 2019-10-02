import pytest
from unittest.mock import patch, ANY
from asynctest import CoroutineMock

from stream.stream import stream_of_consciousness


@pytest.mark.asyncio
async def test_stream_of_consciousness_call_say_func():
    sentences = ['test']
    with patch('stream.stream.say', new=CoroutineMock()) as mocked_say:
        await stream_of_consciousness(sentences)
        mocked_say.assert_called_once_with(sentences[0], ANY)
