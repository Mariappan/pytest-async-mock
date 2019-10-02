import asyncio
import random

from say.say import say


async def stream_of_consciousness(sentences):
    intervals = [1, 2, 5, 10]
    coros = []
    for sentence in sentences:
        when = random.choice(intervals)
        coros.append(say(sentence, when))

    for next_sentence in asyncio.as_completed(coros):
        print(await next_sentence)


if __name__ == '__main__':
    sentences = ['a', 'b', 'c']

    loop = asyncio.get_event_loop()
    loop.run_until_complete(stream_of_consciousness(sentences))
    loop.run_until_complete(stream_of_consciousness(sentences))
