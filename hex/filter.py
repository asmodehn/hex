"""
DictStream filters
FastIn : stream of dicts
FastOut : stream of dicts
SlowIn : Configuration : Regular expression of dict filters
SlowOut : stream of dicts, that match the filters
This is a basic building block of Python Hexagonal Architecture
It can be seen as a filter on stream,
"""
import asyncio

import aioconsole


async def filter(d, filter_string):
    for key, val in d.items():
        if filter_string not in key:
            continue
        yield key, val

async def intrp(line, stdout):
    stdout.write(line)
    return line


async def userin():
    stdin, stdout = await aioconsole.get_standard_streams()
    async for line in stdin:
        await intrp(line)

async def sysin():
    # TODO : wait on network...




loop = asyncio.get_event_loop()
loop.run_until_complete(echo())


async def run(config={}):


    yield(d, config)

    pass






asyncio.run(run())